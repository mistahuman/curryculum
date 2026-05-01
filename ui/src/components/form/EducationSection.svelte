<script lang="ts">
  import { cvStore } from '$lib/stores/cv.svelte';
  import { emptyEducation } from '$lib/types/cv';
  import { Trash2, Plus } from 'lucide-svelte';

  const list = $derived(cvStore.data.education);
</script>

<div class="space-y-4">
  {#each list as edu, i}
    <div
      class="card preset-filled-surface-100-900 border border-surface-200-800 divide-y divide-surface-200-800 overflow-hidden p-0"
    >
      <header class="flex items-center gap-2 px-4 py-2 bg-surface-200-800">
        <p class="flex-1 text-sm font-semibold truncate opacity-80">
          {edu.degree || 'New Degree'}{#if edu.institution}
            <span class="opacity-50">– {edu.institution}</span>{/if}
        </p>
        <button
          class="btn-icon hover:preset-tonal-error"
          onclick={() => cvStore.data.education.splice(i, 1)}
          title="Remove"><Trash2 size={14} /></button
        >
      </header>

      <article class="p-4 space-y-4">
        <div class="grid grid-cols-1 gap-4">
          <label class="label" for="edu-{i}-degree">
            <span class="label-text">Degree / Qualification</span>
            <input
              id="edu-{i}-degree"
              class="input"
              type="text"
              bind:value={cvStore.data.education[i].degree}
              placeholder="BSc Computer Science"
            />
          </label>
          <label class="label" for="edu-{i}-inst">
            <span class="label-text">Institution</span>
            <input
              id="edu-{i}-inst"
              class="input"
              type="text"
              bind:value={cvStore.data.education[i].institution}
              placeholder="Politecnico di Milano"
            />
          </label>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <label class="label" for="edu-{i}-start">
            <span class="label-text">Start Date</span>
            <input
              id="edu-{i}-start"
              class="input"
              type="date"
              bind:value={cvStore.data.education[i].start_date}
            />
          </label>
          <label class="label" for="edu-{i}-year">
            <span class="label-text">Graduation Year</span>
            <input
              id="edu-{i}-year"
              class="input"
              type="number"
              bind:value={cvStore.data.education[i].graduation_year}
              min="1950"
              max="2100"
            />
          </label>
          <label class="label" for="edu-{i}-grade">
            <span class="label-text">Grade / GPA</span>
            <input
              id="edu-{i}-grade"
              class="input"
              type="text"
              bind:value={cvStore.data.education[i].grade}
              placeholder="110/110 · First Class · 4.0"
            />
          </label>
        </div>
      </article>
    </div>
  {/each}

  <button
    class="btn preset-outlined-surface-300-700 w-full"
    onclick={() => cvStore.data.education.push(emptyEducation())}
  >
    <Plus size={16} /> Add Education
  </button>
</div>
