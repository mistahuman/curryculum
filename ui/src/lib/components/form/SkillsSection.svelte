<script lang="ts">
	import { RatingGroup } from '@skeletonlabs/skeleton-svelte';
	import { cvStore } from '$lib/stores/cv.svelte';
	import { emptyTechSkill, emptySoftSkill, emptyLangSkill, emptyDrivingSkill } from '$lib/types/cv';
	import { Trash2, Plus } from 'lucide-svelte';

	const CEF_LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'Native'];
	const s = $derived(cvStore.data.skills);
</script>

<div class="space-y-4">
	<!-- ── Technical Skills ─────────────────────────────── -->
	<section class="space-y-3 card border border-surface-200-800 preset-filled-surface-100-900 p-5">
		<p class="text-xs font-bold tracking-widest uppercase opacity-50">Technical Skills</p>
		<hr class="divider" />

		{#each s.tech_skills as skill, i (i)}
			<div
				class="flex items-center gap-3 rounded-container border border-surface-200-800 bg-surface-100-900 p-3"
			>
				<input
					class="input min-w-0 flex-1"
					type="text"
					bind:value={cvStore.data.skills.tech_skills[i].degree}
					placeholder="e.g. Python"
				/>
				<!-- Rating -->
				<RatingGroup
					class="shrink-0"
					count={5}
					value={skill.level}
					onValueChange={(d) => {
						cvStore.data.skills.tech_skills[i].level = d.value ?? 0;
					}}
				>
					<RatingGroup.Control class="flex flex-row items-center gap-0.5">
						<RatingGroup.Context>
							{#snippet children(ratingGroup)}
								{#each ratingGroup().items as index (index)}
									<RatingGroup.Item {index} />
								{/each}
							{/snippet}
						</RatingGroup.Context>
					</RatingGroup.Control>
					<RatingGroup.HiddenInput name="skill-level-{i}" />
				</RatingGroup>
				<div class="flex shrink-0 items-center gap-1.5">
					<input
						class="input w-14 text-center"
						type="number"
						bind:value={cvStore.data.skills.tech_skills[i].years}
						min="0"
						max="50"
						placeholder="0"
					/>
					<span class="text-xs opacity-40">yrs</span>
				</div>
				<button
					class="btn-icon shrink-0 hover:preset-tonal-error"
					onclick={() => cvStore.data.skills.tech_skills.splice(i, 1)}
				>
					<Trash2 size={13} />
				</button>
			</div>
		{/each}

		<button
			class="btn w-full preset-outlined-surface-300-700"
			onclick={() => cvStore.data.skills.tech_skills.push(emptyTechSkill())}
		>
			<Plus size={14} /> Add Technical Skill
		</button>
	</section>

	<!-- ── Soft Skills ───────────────────────────────────── -->
	<section class="space-y-3 card border border-surface-200-800 preset-filled-surface-100-900 p-5">
		<p class="text-xs font-bold tracking-widest uppercase opacity-50">Soft Skills</p>
		<hr class="divider" />

		{#each s.soft_skills as _sk, i (i)}
			<div class="flex items-center gap-2">
				<input
					class="input flex-1"
					type="text"
					bind:value={cvStore.data.skills.soft_skills[i].degree}
					placeholder="e.g. Team Leadership"
				/>
				<button
					class="btn-icon hover:preset-tonal-error"
					onclick={() => cvStore.data.skills.soft_skills.splice(i, 1)}
				>
					<Trash2 size={13} />
				</button>
			</div>
		{/each}

		<button
			class="btn w-full preset-outlined-surface-300-700"
			onclick={() => cvStore.data.skills.soft_skills.push(emptySoftSkill())}
		>
			<Plus size={14} /> Add Soft Skill
		</button>
	</section>

	<!-- ── Languages ────────────────────────────────────── -->
	<section class="space-y-3 card border border-surface-200-800 preset-filled-surface-100-900 p-5">
		<p class="text-xs font-bold tracking-widest uppercase opacity-50">Languages</p>
		<hr class="divider" />

		{#each s.lang_skills as lang, i (i)}
			<div
				class="divide-y divide-surface-200-800 overflow-hidden card border border-surface-200-800 preset-filled-surface-100-900 p-0"
			>
				<header class="flex items-center gap-2 bg-surface-200-800 px-4 py-2">
					<p class="flex-1 text-sm font-semibold opacity-80">
						{lang.lang || 'Language'}{#if lang.overall_lvl}
							<span class="opacity-50">· {lang.overall_lvl}</span>{/if}
					</p>
					<button
						class="btn-icon hover:preset-tonal-error"
						onclick={() => cvStore.data.skills.lang_skills.splice(i, 1)}
					>
						<Trash2 size={14} />
					</button>
				</header>
				<article class="grid grid-cols-2 gap-4 p-4 md:grid-cols-3">
					<label class="label" for="lang-{i}-name">
						<span class="label-text">Language</span>
						<input
							id="lang-{i}-name"
							class="input"
							type="text"
							bind:value={cvStore.data.skills.lang_skills[i].lang}
							placeholder="Italian"
						/>
					</label>
					<label class="label" for="lang-{i}-overall">
						<span class="label-text">Overall Level</span>
						<select
							id="lang-{i}-overall"
							class="select"
							bind:value={cvStore.data.skills.lang_skills[i].overall_lvl}
						>
							<option value="">—</option>
							{#each CEF_LEVELS as l (l)}<option value={l}>{l}</option>{/each}
						</select>
					</label>
					<label class="label" for="lang-{i}-speaking">
						<span class="label-text">Speaking</span>
						<select
							id="lang-{i}-speaking"
							class="select"
							bind:value={cvStore.data.skills.lang_skills[i].speaking_lvl}
						>
							<option value="">—</option>
							{#each CEF_LEVELS as l (l)}<option value={l}>{l}</option>{/each}
						</select>
					</label>
					<label class="label" for="lang-{i}-writing">
						<span class="label-text">Writing</span>
						<select
							id="lang-{i}-writing"
							class="select"
							bind:value={cvStore.data.skills.lang_skills[i].writing_lvl}
						>
							<option value="">—</option>
							{#each CEF_LEVELS as l (l)}<option value={l}>{l}</option>{/each}
						</select>
					</label>
					<label class="label" for="lang-{i}-listening">
						<span class="label-text">Listening</span>
						<select
							id="lang-{i}-listening"
							class="select"
							bind:value={cvStore.data.skills.lang_skills[i].listening_lvl}
						>
							<option value="">—</option>
							{#each CEF_LEVELS as l (l)}<option value={l}>{l}</option>{/each}
						</select>
					</label>
					<label class="label" for="lang-{i}-comprehension">
						<span class="label-text">Comprehension</span>
						<select
							id="lang-{i}-comprehension"
							class="select"
							bind:value={cvStore.data.skills.lang_skills[i].comprehension_level}
						>
							<option value="">—</option>
							{#each CEF_LEVELS as l (l)}<option value={l}>{l}</option>{/each}
						</select>
					</label>
				</article>
			</div>
		{/each}

		<button
			class="btn w-full preset-outlined-surface-300-700"
			onclick={() => cvStore.data.skills.lang_skills.push(emptyLangSkill())}
		>
			<Plus size={14} /> Add Language
		</button>
	</section>

	<!-- ── Driving License ──────────────────────────────── -->
	<section class="space-y-3 card border border-surface-200-800 preset-filled-surface-100-900 p-5">
		<p class="text-xs font-bold tracking-widest uppercase opacity-50">Driving License</p>
		<hr class="divider" />

		{#each s.driving_skills as _drv, i (i)}
			<div class="flex items-center gap-2">
				<input
					class="input flex-1"
					type="text"
					bind:value={cvStore.data.skills.driving_skills[i].driving_license}
					placeholder="e.g. B"
				/>
				<button
					class="btn-icon hover:preset-tonal-error"
					onclick={() => cvStore.data.skills.driving_skills.splice(i, 1)}
				>
					<Trash2 size={13} />
				</button>
			</div>
		{/each}

		<button
			class="btn w-full preset-outlined-surface-300-700"
			onclick={() => cvStore.data.skills.driving_skills.push(emptyDrivingSkill())}
		>
			<Plus size={14} /> Add License Category
		</button>
	</section>
</div>
