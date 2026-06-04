<script lang="ts">
	import { resolve } from '$app/paths';
	import { ArrowLeft, Pencil, Printer } from 'lucide-svelte';
	import type { CVProfile } from '$lib/types/cv';

	let { data } = $props();
	const cv: CVProfile = data.profile;

	function formatDate(d?: string) {
		if (!d) return '';
		return new Date(d).toLocaleDateString('en', { month: 'short', year: 'numeric' });
	}
</script>

<div class="no-print sticky top-0 z-50 flex items-center justify-between border-b bg-surface-50/90 px-6 py-3 backdrop-blur dark:bg-surface-950/90">
	<div class="flex items-center gap-3">
		<a class="btn-icon preset-tonal" href={resolve(`/cv/${cv.id}`)}>
			<ArrowLeft size={18} />
		</a>
		<span class="font-medium">{cv.label}</span>
	</div>
	<div class="flex gap-2">
		<a class="btn preset-tonal" href={resolve(`/cv/${cv.id}`)}>
			<Pencil size={16} /><span>Edit</span>
		</a>
		<button class="btn preset-filled-primary-500" onclick={() => window.print()}>
			<Printer size={16} /><span>Print / PDF</span>
		</button>
	</div>
</div>

<div class="cv-page mx-auto my-8 max-w-[210mm] bg-white text-gray-900 shadow-xl print:my-0 print:shadow-none">

	<!-- Header -->
	<div class="flex items-start gap-6 bg-slate-800 px-10 py-8 text-white">
		{#if cv.personal_info.photo_url}
			<img src={cv.personal_info.photo_url} alt="Photo" class="h-24 w-24 shrink-0 rounded-full object-cover ring-2 ring-white/30" />
		{/if}
		<div class="min-w-0 flex-1">
			<h1 class="text-3xl font-bold tracking-tight">
				{cv.personal_info.name} {cv.personal_info.surname}
			</h1>
			{#if cv.experience.length > 0}
				<p class="mt-1 text-slate-300">{cv.experience[0].job_title}</p>
			{/if}
			<div class="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm text-slate-300">
				{#if cv.personal_info.email}<span>{cv.personal_info.email}</span>{/if}
				{#if cv.personal_info.phone}<span>{cv.personal_info.phone}</span>{/if}
				{#if cv.personal_info.address}<span>{cv.personal_info.address}</span>{/if}
				{#if cv.personal_info.linkedin}<span>linkedin.com/in/{cv.personal_info.linkedin}</span>{/if}
				{#if cv.personal_info.github}<span>github.com/{cv.personal_info.github}</span>{/if}
			</div>
		</div>
	</div>

	<div class="flex">
		<!-- Left column -->
		<div class="w-[38%] shrink-0 space-y-6 bg-slate-50 px-6 py-8">

			{#if cv.tech_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Technical Skills</h2>
					<ul class="mt-2 space-y-2">
						{#each cv.tech_skills as skill}
							<li class="flex justify-between text-sm">
								<span class="font-medium">{skill.name}</span>
								<span class="text-slate-500 text-xs">{skill.level}</span>
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.soft_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Soft Skills</h2>
					<div class="mt-2 flex flex-wrap gap-1">
						{#each cv.soft_skills as skill}
							<span class="rounded bg-slate-200 px-2 py-0.5 text-xs font-medium text-slate-700">{skill.name}</span>
						{/each}
					</div>
				</section>
			{/if}

			{#if cv.lang_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Languages</h2>
					<ul class="mt-2 space-y-1">
						{#each cv.lang_skills as lang}
							<li class="flex justify-between text-sm">
								<span class="font-medium">{lang.lang}</span>
								<span class="text-slate-500">{lang.overall_lvl}</span>
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.certifications.length > 0}
				<section>
					<h2 class="cv-section-title">Certifications</h2>
					<ul class="mt-2 space-y-2">
						{#each cv.certifications as cert}
							<li class="text-sm">
								<p class="font-medium">{cert.title}</p>
								<p class="text-slate-500">{cert.issuer}{cert.year ? ` · ${cert.year}` : ''}</p>
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.personal_info.nationality || cv.personal_info.birthday}
				<section>
					<h2 class="cv-section-title">About</h2>
					<ul class="mt-2 space-y-1 text-sm">
						{#if cv.personal_info.nationality}<li><span class="text-slate-500">Nationality </span>{cv.personal_info.nationality}</li>{/if}
						{#if cv.personal_info.birthday}<li><span class="text-slate-500">Born </span>{cv.personal_info.birthday}</li>{/if}
					</ul>
				</section>
			{/if}
		</div>

		<!-- Right column -->
		<div class="flex-1 space-y-7 px-8 py-8">

			{#if cv.experience.length > 0}
				<section>
					<h2 class="cv-section-title-main">Experience</h2>
					<div class="mt-3 space-y-5">
						{#each cv.experience as exp}
							<div>
								<div class="flex items-start justify-between gap-2">
									<div>
										<p class="font-semibold">{exp.job_title}</p>
										<p class="text-sm text-slate-600">{exp.company}{exp.company_type ? ` · ${exp.company_type}` : ''}</p>
									</div>
									<p class="shrink-0 text-xs text-slate-400">
										{formatDate(exp.start_date)}{exp.end_date ? ` – ${formatDate(exp.end_date)}` : ' – present'}
									</p>
								</div>
								{#if exp.description}
									<p class="mt-1 text-sm leading-relaxed text-slate-600">{exp.description}</p>
								{/if}
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if cv.education.length > 0}
				<section>
					<h2 class="cv-section-title-main">Education</h2>
					<div class="mt-3 space-y-3">
						{#each cv.education as edu}
							<div class="flex items-start justify-between gap-2">
								<div>
									<p class="font-semibold">{edu.degree}</p>
									<p class="text-sm text-slate-600">{edu.institution}</p>
								</div>
								{#if edu.graduation_year}
									<p class="shrink-0 text-xs text-slate-400">{edu.graduation_year}</p>
								{/if}
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if cv.publications.length > 0}
				<section>
					<h2 class="cv-section-title-main">Publications</h2>
					<div class="mt-3 space-y-2">
						{#each cv.publications as pub}
							<div>
								<p class="text-sm font-semibold">{pub.title}</p>
								<p class="text-xs text-slate-500">{pub.venue}{pub.year ? ` · ${pub.year}` : ''}</p>
							</div>
						{/each}
					</div>
				</section>
			{/if}
		</div>
	</div>
</div>

<style>
	.cv-section-title {
		font-size: 0.65rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: #475569;
		border-bottom: 1px solid #e2e8f0;
		padding-bottom: 4px;
	}
	.cv-section-title-main {
		font-size: 0.7rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: #1e293b;
		border-bottom: 2px solid #1e293b;
		padding-bottom: 4px;
	}
	@media print {
		:global(.no-print) { display: none !important; }
		.cv-page { margin: 0; box-shadow: none; }
	}
</style>
