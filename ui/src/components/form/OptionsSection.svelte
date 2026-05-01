<script lang="ts">
  import { cvStore } from '$lib/stores/cv.svelte';
</script>

<form class="max-w-sm space-y-4">
  <label class="label" for="opt-lang">
    <span class="label-text">CV Language (for PDF output)</span>
    <select id="opt-lang" class="select" bind:value={cvStore.data.options.cvlanguage}>
      <option value="en">English</option>
      <option value="it">Italiano</option>
      <option value="de">Deutsch</option>
      <option value="fr">Français</option>
      <option value="es">Español</option>
    </select>
    <p class="text-xs opacity-50 mt-1">
      Controls section labels and date formats in the LaTeX PDF output.
    </p>
  </label>
</form>
