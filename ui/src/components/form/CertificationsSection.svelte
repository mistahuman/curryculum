<script lang="ts">
  import { cvStore } from '$lib/stores/cv.svelte';
  import { emptyCertification } from '$lib/types/cv';
  import { Trash2, Plus } from 'lucide-svelte';
</script>

<div class="space-y-3">
  {#each cvStore.data.certifications as cert, i}
    <div
      class="card preset-filled-surface-100-900 border border-surface-200-800 overflow-hidden p-0"
    >
      <div class="flex items-end gap-4 p-4">
        <label class="label flex-1" for="cert-{i}-title">
          <span class="label-text">Certification Title</span>
          <input
            id="cert-{i}-title"
            class="input"
            type="text"
            bind:value={cvStore.data.certifications[i].title}
            placeholder="AWS Solutions Architect Associate"
          />
        </label>
        <label class="label w-36" for="cert-{i}-date">
          <span class="label-text">Year / Date</span>
          <input
            id="cert-{i}-date"
            class="input"
            type="text"
            bind:value={cvStore.data.certifications[i].released_at}
            placeholder="2024"
          />
        </label>
        <button
          class="btn-icon hover:preset-tonal-error mb-0.5 shrink-0"
          onclick={() => cvStore.data.certifications.splice(i, 1)}
          title="Remove"><Trash2 size={14} /></button
        >
      </div>
    </div>
  {/each}

  <button
    class="btn preset-outlined-surface-300-700 w-full"
    onclick={() => cvStore.data.certifications.push(emptyCertification())}
  >
    <Plus size={16} /> Add Certification
  </button>
</div>
