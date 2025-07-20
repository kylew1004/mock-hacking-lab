<script>
  import Login from './routes/Login.svelte';
  import Register from './routes/Register.svelte';
  import Home from './routes/Home.svelte';

  let mode = 'login';          // 'login' | 'register' | 'home'
  let currentUser = null;      // { name, username }

  const handleLoggedIn = (e) => {
    currentUser = e.detail.user;
    mode = 'home';             // ★ 로그인 성공 → 홈 화면
  };
</script>

<h1>Mock Hacking Site</h1>

<!-- ‘home’ 모드에서는 네비게이션 버튼 숨김 -->
{#if mode !== 'home'}
  <nav>
    <button on:click={() => (mode = 'login')}>Login</button>
    <button on:click={() => (mode = 'register')}>Register</button>
  </nav>
{/if}

{#if mode === 'login'}
  <Login on:loggedin={handleLoggedIn} />
{:else if mode === 'register'}
  <Register />
{:else if mode === 'home'}
  <Home {currentUser} />
{/if}
