<script>
//This will be the component for the modal for logging in
    export let username;
    export let password;

    let userdata;

    async function verifyUser() {
        fetch("http://api.herding.cat/user/login/" + username)
        .catch(err => console.log(err))
        alert("cum");
    }
</script>

<div id="login" class="hidden flex-col z-20">
    <form on:submit={ verifyUser }>
        <input type="text" bind:value={username} placeholder="username here">
        <input type="password" bind:value={password} placeholder="password here">
        <button type="submit">login</button>
    </form>
</div>