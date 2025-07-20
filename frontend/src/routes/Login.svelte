<script>
  import { post } from '$lib/api';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();
  let username = '', password = '', msg = '';

  const submit = async () => {
    try {
      const data = await post('login', { username, password });

      // 백엔드가 { user: {...}, msg: ... } 형태로 보낸다고 가정
      if (data.user) {
        dispatch('loggedin', { user: data.user });   // ★ 이벤트
      } else {
        msg = data.msg ?? 'Login succeeded but no user payload';
      }
    } catch (err) {
      msg = err.message;
    }
  };
</script>

<h2>Login</h2>
<input bind:value={username} placeholder="username" />
<input type="password" bind:value={password} placeholder="password" />
<button on:click={submit}>Login</button>
<p>{msg}</p>
