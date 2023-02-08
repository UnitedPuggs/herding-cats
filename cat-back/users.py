from supabase import create_client, Client
import os
import dataclasses
from quart import Quart, g, request, abort, make_response
from quart_schema import (
    tag,
    validate_request,
    QuartSchema,
    validate_response,
)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Quart(__name__)
QuartSchema(app)


@dataclasses.dataclass
class User:
    username: str
    password: str

# ------------------ #
#   Error Handling   #
# ------------------ #
@app.errorhandler(404)
async def not_found(e):
    return {"error": f"Not found: {e.description}"}

# ------------------ #
#       Routes       #
# ------------------ #
@app.route("/user/login/<string:username>", methods=["GET"])
@tag("user")
async def login(username):
    #Just something super basic for now, will probably use the reponse from this to create some sorta hashed cookie in sveltekit
    try:
        data = supabase.table("users").select("*").eq("username", username).execute()
        assert len(data.data) > 0
    except:
        abort(404, f"User {username}")

    return {"Logged in": data.data}, 200
