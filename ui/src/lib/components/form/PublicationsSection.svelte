<script lang="ts">
	import { cvStore } from '$lib/stores/cv.svelte';
	import { emptyPublication } from '$lib/types/cv';
	import { Trash2, Plus } from 'lucide-svelte';
</script>

<div class="space-y-4">
	{#each cvStore.data.publications as pub, i (i)}
		<div
			class="divide-y divide-surface-200-800 overflow-hidden card border border-surface-200-800 preset-filled-surface-100-900 p-0"
		>
			<header class="flex items-center gap-2 bg-surface-200-800 px-4 py-2">
				<p class="flex-1 truncate text-sm font-semibold opacity-80">
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
			<article class="space-y-4 p-4">
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
				<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
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
		class="btn w-full preset-outlined-surface-300-700"
		onclick={() => cvStore.data.publications.push(emptyPublication())}
	>
		<Plus size={16} /> Add Publication
	</button>
</div>
