<script lang="ts">
	import { resolve } from '$app/paths';
	import { cvApi } from '$lib/api/cv';
	import { uiStore } from '$lib/stores/ui.svelte';
	import type { CVProfile } from '$lib/types/cv';
	import { ArrowLeft, Eye, Save, Plus, Trash2, Download, User, Briefcase, GraduationCap, Wrench, Award } from 'lucide-svelte';

	let { data } = $props();

	let cv = $state<CVProfile>(JSON.parse(JSON.stringify(data.profile)));
	let saving = $state(false);
	let savedJson = $state(JSON.stringify(data.profile));
	let dirty = $derived(JSON.stringify(cv) !== savedJson);
	let activeTab = $state<'personal' | 'experience' | 'education' | 'skills' | 'extra'>('personal');

	const tabs = [
		{ id: 'personal', label: 'Personal', icon: User },
		{ id: 'experience', label: 'Experience', icon: Briefcase },
		{ id: 'education', label: 'Education', icon: GraduationCap },
		{ id: 'skills', label: 'Skills', icon: Wrench },
		{ id: 'extra', label: 'Extra', icon: Award }
	] as const;

	async function save() {
		saving = true;
		try {
			await cvApi.update(cv.id, cv);
			savedJson = JSON.stringify(cv);
			uiStore.toast('Saved', 'success');
		} catch {
			uiStore.toast('Save failed', 'error');
		} finally {
			saving = false;
		}
	}

	async function exportJson() {
		try {
			await cvApi.exportJson(cv.id, `cv-${cv.label.toLowerCase().replace(/\s+/g, '-')}.json`);
		} catch {
			uiStore.toast('Export failed', 'error');
		}
	}

	function addExperience() {
		cv.experience.push({ job_title: '', company: '', company_type: '', start_date: undefined, end_date: undefined, description: '' });
	}
	function addEducation() { cv.education.push({ degree: '', institution: '', graduation_year: undefined }); }
	function addTechSkill() { cv.tech_skills.push({ name: '', level: '' }); }
	function addSoftSkill() { cv.soft_skills.push({ name: '' }); }
	function addLangSkill() { cv.lang_skills.push({ lang: '', overall_lvl: '' }); }
	function addCertification() { cv.certifications.push({ title: '', issuer: '', year: undefined, url: '' }); }
	function addPublication() { cv.publications.push({ title: '', venue: '', year: undefined, url: '' }); }
</script>

<div class="container mx-auto max-w-4xl space-y-6 px-4 py-8">

	<!-- Top bar -->
	<div class="flex items-center justify-between gap-4">
		<div class="flex items-center gap-3">
			<a class="btn-icon preset-tonal" href={resolve('/cv')} title="Back">
				<ArrowLeft size={18} />
			</a>
			<input
				class="input h-auto border-none bg-transparent p-0 text-xl font-bold focus:ring-0"
				type="text"
				bind:value={cv.label}
				placeholder="CV label"
			/>
		</div>
		<div class="flex items-center gap-2">
			<button class="btn preset-tonal" onclick={exportJson}>
				<Download size={16} /><span class="hidden sm:inline">Export JSON</span>
			</button>
			<a class="btn preset-tonal" href={resolve(`/cv/${cv.id}/preview`)}>
				<Eye size={16} /><span class="hidden sm:inline">Preview</span>
			</a>
			<div class="relative">
				<button class="btn preset-filled-primary-500" onclick={save} disabled={saving}>
					<Save size={16} /><span>{saving ? 'Saving…' : 'Save'}</span>
				</button>
				{#if dirty && !saving}
					<span class="bg-warning-500 absolute -right-1 -top-1 size-2 rounded-full"></span>
				{/if}
			</div>
		</div>
	</div>

	<!-- Tabs -->
	<div class="border-surface-200-800 flex gap-0.5 border-b">
		{#each tabs as tab (tab.id)}
			{@const Icon = tab.icon}
			<button
				class="flex items-center gap-1.5 px-4 py-2.5 text-sm font-medium transition-colors {activeTab === tab.id
					? 'border-primary-500 text-primary-500 -mb-px border-b-2'
					: 'text-surface-500 hover:text-surface-900 dark:hover:text-surface-100'}"
				onclick={() => (activeTab = tab.id)}
			>
				<Icon size={14} />
				<span class="hidden sm:inline">{tab.label}</span>
			</button>
		{/each}
	</div>

	<!-- PERSONAL INFO -->
	{#if activeTab === 'personal'}
		<div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
			<label class="label">
				<span class="label-text">First name</span>
				<input class="input" type="text" bind:value={cv.personal_info.name} />
			</label>
			<label class="label">
				<span class="label-text">Last name</span>
				<input class="input" type="text" bind:value={cv.personal_info.surname} />
			</label>
			<label class="label">
				<span class="label-text">Email</span>
				<input class="input" type="email" bind:value={cv.personal_info.email} />
			</label>
			<label class="label">
				<span class="label-text">Phone</span>
				<input class="input" type="tel" bind:value={cv.personal_info.phone} />
			</label>
			<label class="label">
				<span class="label-text">Date of birth</span>
				<input class="input" type="date" bind:value={cv.personal_info.birthday} />
			</label>
			<label class="label">
				<span class="label-text">Nationality</span>
				<input class="input" type="text" bind:value={cv.personal_info.nationality} />
			</label>
			<label class="label sm:col-span-2">
				<span class="label-text">Address</span>
				<input class="input" type="text" bind:value={cv.personal_info.address} />
			</label>
			<label class="label">
				<span class="label-text">GitHub username</span>
				<input class="input" type="text" bind:value={cv.personal_info.github} />
			</label>
			<label class="label">
				<span class="label-text">LinkedIn username</span>
				<input class="input" type="text" bind:value={cv.personal_info.linkedin} />
			</label>
			<label class="label sm:col-span-2">
				<span class="label-text">Photo URL</span>
				<input class="input" type="url" bind:value={cv.personal_info.photo_url} />
			</label>
		</div>
	{/if}

	<!-- EXPERIENCE -->
	{#if activeTab === 'experience'}
		<div class="space-y-4">
			{#each cv.experience as exp, i (i)}
				<div class="card bg-surface-100-900 space-y-3 p-4">
					<div class="flex items-start justify-between gap-2">
						<div class="min-w-0 flex-1">
							{#if exp.job_title || exp.company}
								<p class="truncate text-sm font-semibold">{exp.job_title || exp.company}</p>
								{#if exp.job_title && exp.company}
									<p class="text-surface-500 truncate text-xs">{exp.company}</p>
								{/if}
							{:else}
								<p class="text-surface-400 text-sm italic">Experience #{i + 1}</p>
							{/if}
						</div>
						<button class="btn-icon btn-sm hover:preset-filled-error-500 shrink-0" onclick={() => cv.experience.splice(i, 1)}>
							<Trash2 size={14} />
						</button>
					</div>
					<div class="border-surface-200-800 border-t pt-3">
						<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
							<label class="label">
								<span class="label-text">Job title</span>
								<input class="input" type="text" bind:value={exp.job_title} />
							</label>
							<label class="label">
								<span class="label-text">Company</span>
								<input class="input" type="text" bind:value={exp.company} />
							</label>
							<label class="label">
								<span class="label-text">Company type</span>
								<input class="input" type="text" placeholder="e.g. Startup, Enterprise" bind:value={exp.company_type} />
							</label>
							<div class="grid grid-cols-2 gap-3">
								<label class="label">
									<span class="label-text">Start</span>
									<input class="input" type="date" bind:value={exp.start_date} />
								</label>
								<label class="label">
									<span class="label-text">End</span>
									<input class="input" type="date" bind:value={exp.end_date} />
								</label>
							</div>
							<label class="label sm:col-span-2">
								<span class="label-text">Description</span>
								<textarea class="textarea" rows="3" bind:value={exp.description}></textarea>
							</label>
						</div>
					</div>
				</div>
			{/each}
			<button class="btn preset-tonal w-full" onclick={addExperience}>
				<Plus size={16} /><span>Add experience</span>
			</button>
		</div>
	{/if}

	<!-- EDUCATION -->
	{#if activeTab === 'education'}
		<div class="space-y-4">
			{#each cv.education as edu, i (i)}
				<div class="card bg-surface-100-900 space-y-3 p-4">
					<div class="flex items-start justify-between gap-2">
						<div class="min-w-0 flex-1">
							{#if edu.degree || edu.institution}
								<p class="truncate text-sm font-semibold">{edu.degree || edu.institution}</p>
								{#if edu.degree && edu.institution}
									<p class="text-surface-500 truncate text-xs">{edu.institution}</p>
								{/if}
							{:else}
								<p class="text-surface-400 text-sm italic">Education #{i + 1}</p>
							{/if}
						</div>
						<button class="btn-icon btn-sm hover:preset-filled-error-500 shrink-0" onclick={() => cv.education.splice(i, 1)}>
							<Trash2 size={14} />
						</button>
					</div>
					<div class="border-surface-200-800 border-t pt-3">
						<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
							<label class="label">
								<span class="label-text">Degree</span>
								<input class="input" type="text" bind:value={edu.degree} />
							</label>
							<label class="label">
								<span class="label-text">Institution</span>
								<input class="input" type="text" bind:value={edu.institution} />
							</label>
							<label class="label">
								<span class="label-text">Graduation year</span>
								<input class="input" type="number" bind:value={edu.graduation_year} />
							</label>
						</div>
					</div>
				</div>
			{/each}
			<button class="btn preset-tonal w-full" onclick={addEducation}>
				<Plus size={16} /><span>Add education</span>
			</button>
		</div>
	{/if}

	<!-- SKILLS -->
	{#if activeTab === 'skills'}
		<div class="space-y-8">
			<section class="space-y-3">
				<h3 class="h4 font-semibold">Technical skills</h3>
				<div class="space-y-2">
					{#each cv.tech_skills as skill, i (i)}
						<div class="flex gap-2">
							<input class="input flex-1" type="text" placeholder="Skill name" bind:value={skill.name} />
							<input class="input w-32" type="text" placeholder="Level" bind:value={skill.level} />
							<button class="btn-icon hover:preset-filled-error-500" onclick={() => cv.tech_skills.splice(i, 1)}>
								<Trash2 size={14} />
							</button>
						</div>
					{/each}
				</div>
				<button class="btn preset-tonal" onclick={addTechSkill}>
					<Plus size={16} /><span>Add tech skill</span>
				</button>
			</section>

			<section class="space-y-3">
				<h3 class="h4 font-semibold">Soft skills</h3>
				<div class="flex flex-wrap gap-2">
					{#each cv.soft_skills as skill, i (i)}
						<div class="flex items-center gap-1 rounded-full border px-3 py-1">
							<input class="w-28 border-none bg-transparent text-sm focus:outline-none" type="text" bind:value={skill.name} />
							<button onclick={() => cv.soft_skills.splice(i, 1)} class="text-surface-400 hover:text-error-500">
								<Trash2 size={12} />
							</button>
						</div>
					{/each}
				</div>
				<button class="btn preset-tonal" onclick={addSoftSkill}>
					<Plus size={16} /><span>Add soft skill</span>
				</button>
			</section>

			<section class="space-y-3">
				<h3 class="h4 font-semibold">Languages</h3>
				<div class="space-y-2">
					{#each cv.lang_skills as lang, i (i)}
						<div class="flex gap-2">
							<input class="input flex-1" type="text" placeholder="Language" bind:value={lang.lang} />
							<input class="input w-32" type="text" placeholder="Level (B2, C1…)" bind:value={lang.overall_lvl} />
							<button class="btn-icon hover:preset-filled-error-500" onclick={() => cv.lang_skills.splice(i, 1)}>
								<Trash2 size={14} />
							</button>
						</div>
					{/each}
				</div>
				<button class="btn preset-tonal" onclick={addLangSkill}>
					<Plus size={16} /><span>Add language</span>
				</button>
			</section>
		</div>
	{/if}

	<!-- EXTRA -->
	{#if activeTab === 'extra'}
		<div class="space-y-8">
			<section class="space-y-3">
				<h3 class="h4 font-semibold">Certifications</h3>
				<div class="space-y-3">
					{#each cv.certifications as cert, i (i)}
						<div class="card bg-surface-100-900 space-y-3 p-4">
							<div class="flex items-start justify-between gap-2">
								<div class="min-w-0 flex-1">
									{#if cert.title}
										<p class="truncate text-sm font-semibold">{cert.title}</p>
										{#if cert.issuer}<p class="text-surface-500 text-xs">{cert.issuer}</p>{/if}
									{:else}
										<p class="text-surface-400 text-sm italic">Certification #{i + 1}</p>
									{/if}
								</div>
								<button class="btn-icon hover:preset-filled-error-500 shrink-0" onclick={() => cv.certifications.splice(i, 1)}>
									<Trash2 size={14} />
								</button>
							</div>
							<div class="border-surface-200-800 grid grid-cols-1 gap-3 border-t pt-3 sm:grid-cols-2">
								<label class="label"><span class="label-text">Title</span><input class="input" type="text" bind:value={cert.title} /></label>
								<label class="label"><span class="label-text">Issuer</span><input class="input" type="text" bind:value={cert.issuer} /></label>
								<label class="label"><span class="label-text">Year</span><input class="input" type="number" bind:value={cert.year} /></label>
								<label class="label"><span class="label-text">URL</span><input class="input" type="url" bind:value={cert.url} /></label>
							</div>
						</div>
					{/each}
				</div>
				<button class="btn preset-tonal" onclick={addCertification}>
					<Plus size={16} /><span>Add certification</span>
				</button>
			</section>

			<section class="space-y-3">
				<h3 class="h4 font-semibold">Publications</h3>
				<div class="space-y-3">
					{#each cv.publications as pub, i (i)}
						<div class="card bg-surface-100-900 space-y-3 p-4">
							<div class="flex items-start justify-between gap-2">
								<div class="min-w-0 flex-1">
									{#if pub.title}
										<p class="truncate text-sm font-semibold">{pub.title}</p>
										{#if pub.venue}<p class="text-surface-500 text-xs">{pub.venue}</p>{/if}
									{:else}
										<p class="text-surface-400 text-sm italic">Publication #{i + 1}</p>
									{/if}
								</div>
								<button class="btn-icon hover:preset-filled-error-500 shrink-0" onclick={() => cv.publications.splice(i, 1)}>
									<Trash2 size={14} />
								</button>
							</div>
							<div class="border-surface-200-800 grid grid-cols-1 gap-3 border-t pt-3 sm:grid-cols-2">
								<label class="label"><span class="label-text">Title</span><input class="input" type="text" bind:value={pub.title} /></label>
								<label class="label"><span class="label-text">Venue</span><input class="input" type="text" bind:value={pub.venue} /></label>
								<label class="label"><span class="label-text">Year</span><input class="input" type="number" bind:value={pub.year} /></label>
								<label class="label"><span class="label-text">URL</span><input class="input" type="url" bind:value={pub.url} /></label>
							</div>
						</div>
					{/each}
				</div>
				<button class="btn preset-tonal" onclick={addPublication}>
					<Plus size={16} /><span>Add publication</span>
				</button>
			</section>
		</div>
	{/if}

</div>
