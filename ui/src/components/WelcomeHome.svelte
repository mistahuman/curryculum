<script lang="ts">
  import { ChevronRight as IconChevron } from 'lucide-svelte';
  import Logo from './generic/Logo.svelte';
</script>

<div class="grid grid-cols-1 gap-20">
  <!-- Mascot -->
  <div class="flex justify-center items-center">
    <div class="relative size-48 md:size-64 aspect-square justify-center items-center flex">
      <Logo width="200" height="200" />
    </div>
  </div>
  <!-- Hero Text -->
  <div class="self-center text-center space-y-4">
    <h1 class="heading-font-family text-3xl md:text-4xl font-bold xl:text-balance">
      mistahuman's template svelte-skeleton
    </h1>
    <p class="xl:text-balance">
      For building <strong class="text-primary-900-100">github pages</strong>
      <u>easily</u>.
    </p>
    <a
      href="https://github.com/mistahuman/template-astro-svelte-skeleton"
      class="btn preset-tonal-primary"
    >
      <span>visit code</span>
      <IconChevron class="size-4" />
    </a>
  </div>
</div>
