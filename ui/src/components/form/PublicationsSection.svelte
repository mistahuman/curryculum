<script lang="ts">
  import { cvStore } from '$lib/stores/cv.svelte';
  import { emptyPublication } from '$lib/types/cv';
  import { Trash2, Plus } from 'lucide-svelte';
</script>

<div class="space-y-4">
  {#each cvStore.data.publications as pub, i}
    <div
      class="card preset-filled-surface-100-900 border border-surface-200-800 divide-y divide-surface-200-800 overflow-hidden p-0"
    >
      <header class="flex items-center gap-2 px-4 py-2 bg-surface-200-800">
        <p class="flex-1 text-sm font-semibold truncate opacity-80">
          {pub.title || 'New Publication'}
        </p>
        <button
          class="btn-icon hover:preset-tonal-error"
          onclick={() => cvStore.data.publications.splice(i, 1)}
          title="Remove"
        >
          <Trash2 size={14} />
        </button>
      </header>
      <article class="p-4 space-y-4">
        <label class="label" for="pub-{i}-title">
          <span class="label-text">Title</span>
          <input
            id="pub-{i}-title"
            class="input"
            type="text"
            bind:value={cvStore.data.publications[i].title}
            placeholder="Paper or book title"
          />
        </label>
        <label class="label" for="pub-{i}-authors">
          <span class="label-text">Authors</span>
          <input
            id="pub-{i}-authors"
            class="input"
            type="text"
            bind:value={cvStore.data.publications[i].authors}
            placeholder="Rossi M., Bianchi L."
          />
        </label>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <label class="label" for="pub-{i}-journal">
            <span class="label-text">Journal / Conference</span>
            <input
              id="pub-{i}-journal"
              class="input"
              type="text"
              bind:value={cvStore.data.publications[i].journal}
              placeholder="Nature, ACM, IEEE, ..."
            />
          </label>
          <label class="label" for="pub-{i}-details">
            <span class="label-text">Details (volume, year, DOI)</span>
            <input
              id="pub-{i}-details"
              class="input"
              type="text"
              bind:value={cvStore.data.publications[i].details}
              placeholder="Vol. 1, pp. 1–10, 2024"
            />
          </label>
        </div>
      </article>
    </div>
  {/each}

  <button
    class="btn preset-outlined-surface-300-700 w-full"
    onclick={() => cvStore.data.publications.push(emptyPublication())}
  >
    <Plus size={16} /> Add Publication
  </button>
</div>
