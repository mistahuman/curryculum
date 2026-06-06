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

	const contacts = $derived(
		[
			cv.personal_info.email,
			cv.personal_info.phone,
			cv.personal_info.address,
			cv.personal_info.linkedin ? `linkedin.com/in/${cv.personal_info.linkedin}` : '',
			cv.personal_info.github ? `github.com/${cv.personal_info.github}` : ''
		].filter(Boolean)
	);
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

	<!-- Top accent bar -->
	<div class="h-1 bg-indigo-500"></div>

	<!-- Header -->
	<div class="flex items-start gap-6 bg-indigo-900 px-10 py-8 text-white">
		{#if cv.personal_info.photo_url}
			<img
				src={cv.personal_info.photo_url}
				alt="Photo"
				class="h-24 w-24 shrink-0 rounded-full object-cover ring-2 ring-indigo-400/40"
			/>
		{/if}
		<div class="min-w-0 flex-1">
			<h1 class="text-3xl font-bold tracking-tight">
				{cv.personal_info.name} {cv.personal_info.surname}
			</h1>
			{#if cv.experience.length > 0}
				<p class="mt-1 text-indigo-300 font-medium">{cv.experience[0].job_title}</p>
			{/if}
			{#if contacts.length > 0}
				<div class="mt-3 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-indigo-200">
					{#each contacts as item, i}
						{#if i > 0}<span class="text-indigo-600 select-none">·</span>{/if}
						<span>{item}</span>
					{/each}
				</div>
			{/if}
		</div>
	</div>

	<div class="flex">
		<!-- Left column -->
		<div class="w-[36%] shrink-0 space-y-6 bg-indigo-50 px-6 py-8">

			{#if cv.tech_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Technical Skills</h2>
					<ul class="mt-3 space-y-2">
						{#each cv.tech_skills as skill}
							<li class="flex items-center justify-between gap-2 text-sm">
								<span class="font-medium text-gray-800">{skill.name}</span>
								{#if skill.level}
									<span class="skill-badge">{skill.level}</span>
								{/if}
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.soft_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Soft Skills</h2>
					<div class="mt-3 flex flex-wrap gap-1.5">
						{#each cv.soft_skills as skill}
							<span class="rounded-full bg-indigo-100 px-2.5 py-0.5 text-xs font-medium text-indigo-800">
								{skill.name}
							</span>
						{/each}
					</div>
				</section>
			{/if}

			{#if cv.lang_skills.length > 0}
				<section>
					<h2 class="cv-section-title">Languages</h2>
					<ul class="mt-3 space-y-1.5">
						{#each cv.lang_skills as lang}
							<li class="flex items-center justify-between text-sm">
								<span class="font-medium text-gray-800">{lang.lang}</span>
								<span class="skill-badge">{lang.overall_lvl}</span>
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.certifications.length > 0}
				<section>
					<h2 class="cv-section-title">Certifications</h2>
					<ul class="mt-3 space-y-2.5">
						{#each cv.certifications as cert}
							<li class="text-sm">
								<p class="font-semibold text-gray-800">{cert.title}</p>
								<p class="text-slate-500">{cert.issuer}{cert.year ? ` · ${cert.year}` : ''}</p>
							</li>
						{/each}
					</ul>
				</section>
			{/if}

			{#if cv.personal_info.nationality || cv.personal_info.birthday}
				<section>
					<h2 class="cv-section-title">About</h2>
					<ul class="mt-3 space-y-1 text-sm">
						{#if cv.personal_info.nationality}
							<li>
								<span class="text-slate-400">Nationality </span>{cv.personal_info.nationality}
							</li>
						{/if}
						{#if cv.personal_info.birthday}
							<li>
								<span class="text-slate-400">Born </span>{cv.personal_info.birthday}
							</li>
						{/if}
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
							<div class="border-l-2 border-indigo-200 pl-3">
								<div class="flex items-start justify-between gap-2">
									<div>
										<p class="font-semibold text-gray-900">{exp.job_title}</p>
										<p class="text-sm text-slate-600">
											{exp.company}{exp.company_type ? ` · ${exp.company_type}` : ''}
										</p>
									</div>
									<p class="shrink-0 text-xs text-indigo-400 font-medium">
										{formatDate(exp.start_date)}{exp.end_date
											? ` – ${formatDate(exp.end_date)}`
											: ' – present'}
									</p>
								</div>
								{#if exp.description}
									<p class="mt-1.5 text-sm leading-relaxed text-slate-600">{exp.description}</p>
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
									<p class="font-semibold text-gray-900">{edu.degree}</p>
									<p class="text-sm text-slate-600">{edu.institution}</p>
								</div>
								{#if edu.graduation_year}
									<p class="shrink-0 text-xs text-indigo-400 font-medium">{edu.graduation_year}</p>
								{/if}
							</div>
						{/each}
					</div>
				</section>
			{/if}

			{#if cv.publications.length > 0}
				<section>
					<h2 class="cv-section-title-main">Publications</h2>
					<div class="mt-3 space-y-2.5">
						{#each cv.publications as pub}
							<div>
								<p class="text-sm font-semibold text-gray-900">{pub.title}</p>
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
		font-size: 0.6rem;
		font-weight: 700;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: #3730a3;
		border-bottom: 1px solid #c7d2fe;
		padding-bottom: 4px;
	}
	.cv-section-title-main {
		font-size: 0.65rem;
		font-weight: 700;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: #1e1b4b;
		border-bottom: 2px solid #4338ca;
		padding-bottom: 4px;
	}
	.skill-badge {
		display: inline-block;
		background-color: #e0e7ff;
		color: #3730a3;
		font-size: 0.65rem;
		font-weight: 600;
		padding: 1px 6px;
		border-radius: 4px;
		white-space: nowrap;
	}
	@media print {
		:global(.no-print) {
			display: none !important;
		}
		.cv-page {
			margin: 0;
			box-shadow: none;
		}
	}
</style>
