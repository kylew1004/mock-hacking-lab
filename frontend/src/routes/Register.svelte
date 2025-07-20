<script>
  import { post } from '$lib/api';
  let name = '', username = '', password = '', msg = '';
  const submit = async () => {
    const data = await post('register', { name, username, password });
    msg = data.msg ?? data.detail;
  };
</script>

<h2>Register</h2>
<input bind:value={name}  placeholder="name (opt)" />
<input bind:value={username} placeholder="username" />
<input type="password" bind:value={password} placeholder="password" />
<button on:click={submit}>Register</button>
<p>{msg}</p>
