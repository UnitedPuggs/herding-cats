<script>
    import Login from "./Login.svelte"

    function showLogin() {
        if(document.getElementById("login").style.display == "flex")
            document.getElementById("login").style.display = "none";
        else
            document.getElementById("login").style.display = "flex";
    }
</script>

<svelte:head>
    <title>Cat herding for the pros!</title>
</svelte:head>

<body class="bg-gradient-to-r from-indigo-400 to-purple-500">
<div id="main-container" class="font-mono">
    <div id="navbar" class="flex flex-wrap flex-row justify-end m-8">
        <button class="text-white bg-blue-300 px-1 mx-1 rounded-md drop-shadow-md hover:opacity-80" on:click={ showLogin }>Login</button>
        <Login />
        <p class="text-white">&nbsp;or&nbsp;</p>
        <button class="text-white bg-blue-300 px-1 mx-1 rounded-md drop-shadow-md hover:opacity-80">Create an account</button>
    </div>
    <div id="center" class="h-[32rem] flex flex-wrap justify-center items-center">
        <button class="text-white bg-violet-400 px-24 py-10 rounded-lg drop-shadow-lg hover:opacity-80 hover:drop-shadow-xl">Start herding your cats!</button>
    </div>
</div>
</body>