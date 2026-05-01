<script lang="ts">
  import '../styles/global.css';
  import Header from '@components/generic/Header.svelte';
  import Footer from '@components/generic/Footer.svelte';

  let { children } = $props();
</script>

<div class="flex flex-col min-h-screen">
  <Header />
  <main class="flex-1 flex flex-col min-h-0">
    {@render children()}
  </main>
  <Footer />
</div>
