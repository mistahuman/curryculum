<script lang="ts">
  import type { Snippet } from 'svelte';

  let {
    title = '',
    children,
  }: {
    title?: string;
    children?: Snippet;
  } = $props();
</script>

<div class="card preset-filled-surface-100-900 border-[1px] border-surface-200-800 w-full p-4">
  <header class="h3 text-center">
    {title}
  </header>
  <hr class="divider" />
  <article class="p-4">
    {@render children?.()}
  </article>
</div>
