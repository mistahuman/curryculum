<script lang="ts">
  import { Menu, X } from 'lucide-svelte';

  interface NavLink {
    href: string;
    label: string;
    target?: string;
  }

  let { navigation = [] }: { navigation?: NavLink[] } = $props();
  let open = $state(false);

  function toggle() {
    open = !open;
  }
</script>

<!-- Hamburger Menu -->
<button class="xl:hidden btn-icon" onclick={toggle}>
  <Menu size={20} />
</button>

<!-- Drawer Panel -->
<div
  class="xl:hidden preset-filled-surface-100-900 shadow-xl fixed top-0 left-0 bottom-0 h-screen z-50 w-[320px] p-4 pb-24 space-y-10 overflow-y-auto transition-transform duration-100"
  class:-translate-x-[320px]={!open}
  class:translate-x-0={open}
>
  <!-- Header -->
  <header class="flex justify-between items-center">
    <h2 class="h3">mistahuman's GitHub Pages</h2>
    <button class="btn-icon" onclick={toggle}>
      <X size={20} />
    </button>
  </header>
  <!-- Navigation -->
  <nav class="flex flex-col gap-2">
    {#each navigation as link}
      <a class="anchor hover:underline" href={link.href} target={link.target} onclick={toggle}>
        {link.label}
      </a>
    {/each}
  </nav>
</div>
