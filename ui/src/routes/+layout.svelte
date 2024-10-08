<script lang="ts">
  import '../styles/global.css';
  import Header from '@components/generic/Header.svelte';
  import Footer from '@components/generic/Footer.svelte';

  let { children } = $props();
</script>

<div class="grid min-h-screen grid-rows-[auto_1fr_auto]">
  <Header />
  <main class="bg-surface-50-950">
    {@render children()}
  </main>
  <Footer />
</div>
