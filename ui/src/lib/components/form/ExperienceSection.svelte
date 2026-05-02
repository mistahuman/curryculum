<script lang="ts">
	import { cvStore } from '$lib/stores/cv.svelte';
	import { emptyExperience } from '$lib/types/cv';
	import { Trash2, Plus } from 'lucide-svelte';

	const list = $derived(cvStore.data.experience);

	function addAchievement(i: number) {
		cvStore.data.experience[i].achievements.push('');
	}

	function removeAchievement(expIdx: number, aIdx: number) {
		cvStore.data.experience[expIdx].achievements.splice(aIdx, 1);
	}
</script>

<div class="space-y-4">
	{#each list as exp, i (i)}
		<div
			class="divide-y divide-surface-200-800 overflow-hidden card border border-surface-200-800 preset-filled-surface-100-900 p-0"
		>
			<!-- Card header -->
			<header class="flex items-center gap-2 bg-surface-200-800 px-4 py-2">
				<p class="flex-1 truncate text-sm font-semibold opacity-80">
					{exp.job_title || 'New Experience'}{#if exp.company}
						<span class="opacity-50">@ {exp.company}</span>{/if}
				</p>
				<button
					class="btn-icon hover:preset-tonal-error"
					onclick={() => cvStore.data.experience.splice(i, 1)}
					title="Remove"><Trash2 size={14} /></button
				>
			</header>

			<article class="space-y-4 p-4">
				<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
					<label class="label" for="exp-{i}-title">
						<span class="label-text">Job Title</span>
						<input
							id="exp-{i}-title"
							class="input"
							type="text"
							bind:value={cvStore.data.experience[i].job_title}
							placeholder="Software Engineer"
						/>
					</label>
					<label class="label" for="exp-{i}-company">
						<span class="label-text">Company</span>
						<input
							id="exp-{i}-company"
							class="input"
							type="text"
							bind:value={cvStore.data.experience[i].company}
							placeholder="ACME Corp"
						/>
					</label>
					<label class="label" for="exp-{i}-type">
						<span class="label-text">Company Type</span>
						<input
							id="exp-{i}-type"
							class="input"
							type="text"
							bind:value={cvStore.data.experience[i].company_type}
							placeholder="IT / Finance / ..."
						/>
					</label>
				</div>

				<!-- Dates -->
				<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
					<label class="label" for="exp-{i}-start">
						<span class="label-text">Start Date</span>
						<input
							id="exp-{i}-start"
							class="input"
							type="date"
							bind:value={cvStore.data.experience[i].start_date}
						/>
					</label>
					<div class="label">
						<span class="label-text">End Date</span>
						<div class="flex items-center gap-3">
							<input
								id="exp-{i}-end"
								class="input flex-1"
								type="date"
								value={exp.end_date ?? ''}
								disabled={exp.end_date === null}
								oninput={(e) => {
									cvStore.data.experience[i].end_date =
										(e.target as HTMLInputElement).value || null;
								}}
							/>
							<label class="flex cursor-pointer items-center gap-1.5 text-sm whitespace-nowrap">
								<input
									type="checkbox"
									checked={exp.end_date === null}
									onchange={(e) => {
										cvStore.data.experience[i].end_date = (e.target as HTMLInputElement).checked
											? null
											: '';
									}}
								/>
								Present
							</label>
						</div>
					</div>
				</div>

				<!-- Description -->
				<label class="label" for="exp-{i}-desc">
					<span class="label-text">Description</span>
					<textarea
						id="exp-{i}-desc"
						class="textarea rounded-container"
						rows="3"
						bind:value={cvStore.data.experience[i].description}
						placeholder="Describe your role and responsibilities..."
					></textarea>
				</label>

				<!-- Achievements -->
				<div class="space-y-2">
					<span class="label-text">Key Achievements</span>
					{#each exp.achievements as _ach, ai (ai)}
						<div class="flex items-center gap-2">
							<input
								class="input flex-1"
								type="text"
								bind:value={cvStore.data.experience[i].achievements[ai]}
								placeholder="e.g. Led migration to microservices, reducing latency by 40%"
							/>
							<button
								class="btn-icon hover:preset-tonal-error"
								onclick={() => removeAchievement(i, ai)}
								title="Remove"
							>
								<Trash2 size={13} />
							</button>
						</div>
					{/each}
					<button class="btn w-full preset-tonal text-sm" onclick={() => addAchievement(i)}>
						<Plus size={14} /> Add Achievement
					</button>
				</div>
			</article>
		</div>
	{/each}

	<button
		class="btn w-full preset-outlined-surface-300-700"
		onclick={() => cvStore.data.experience.push(emptyExperience())}
	>
		<Plus size={16} /> Add Work Experience
	</button>
</div>
