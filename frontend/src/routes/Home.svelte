<script>
  export let currentUser = {};
</script>

<h2>Welcome, {currentUser.name ?? currentUser.username}!</h2>
<p>You are now logged in.</p>