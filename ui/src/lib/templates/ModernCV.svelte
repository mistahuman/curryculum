<script lang="ts">
	import type { CVData } from '$lib/types/cv';

	let { data }: { data: CVData } = $props();

	const p = $derived(data.personal_info);

	function fmtDate(d: string | null | undefined): string {
		if (!d) return 'Present';
		const dt = new Date(d + 'T00:00:00');
		return dt.toLocaleDateString('en', { month: 'short', year: 'numeric' });
	}

	function fmtYear(d: string | null | undefined): string {
		if (!d) return '';
		return new Date(d + 'T00:00:00').getFullYear().toString();
	}

	function dots(level: number, max = 5): string {
		return '●'.repeat(Math.max(0, Math.min(level, max))) + '○'.repeat(Math.max(0, max - level));
	}
</script>

<div class="cv">
	<!-- ── Header ─────────────────────────────────────── -->
	<header class="cv-header">
		<div class="cv-header-name">
			<h1>
				<span class="name-light">{p.name}</span>
				<span class="name-bold">{p.surname}</span>
			</h1>
			{#if p.job_title}<p class="job-title">{p.job_title}</p>{/if}
		</div>
		<ul class="cv-contact">
			{#if p.email}<li><span class="icon">✉</span>{p.email}</li>{/if}
			{#if p.phone}<li><span class="icon">☎</span>{p.phone}</li>{/if}
			{#if p.address}<li><span class="icon">⌂</span>{p.address}</li>{/if}
			{#if p.github}<li><span class="icon">⌥</span>github.com/{p.github}</li>{/if}
			{#if p.linkedin}<li><span class="icon">in</span>linkedin.com/in/{p.linkedin}</li>{/if}
		</ul>
	</header>

	<!-- ── Work Experience ───────────────────────────── -->
	{#if data.experience.length > 0}
		<section>
			<h2 class="section-title">Work Experience</h2>
			{#each data.experience as exp, i (i)}
				<div class="entry">
					<div class="entry-date">
						{fmtDate(exp.start_date)} –<br />{exp.end_date ? fmtDate(exp.end_date) : 'Present'}
					</div>
					<div class="entry-body">
						<p class="entry-title">{exp.job_title}</p>
						<p class="entry-subtitle">
							{exp.company}{#if exp.company_type}
								· {exp.company_type}{/if}
						</p>
						{#if exp.description}<p class="entry-desc">{exp.description}</p>{/if}
						{#if exp.achievements.length > 0}
							<ul class="achievements">
								{#each exp.achievements as a, j (j)}{#if a}<li>{a}</li>{/if}{/each}
							</ul>
						{/if}
					</div>
				</div>
			{/each}
		</section>
	{/if}

	<!-- ── Education ─────────────────────────────────── -->
	{#if data.education.length > 0}
		<section>
			<h2 class="section-title">Education</h2>
			{#each data.education as edu, i (i)}
				<div class="entry">
					<div class="entry-date">
						{#if edu.start_date}{fmtYear(edu.start_date)} –<br />{/if}
						{edu.graduation_year}
					</div>
					<div class="entry-body">
						<p class="entry-title">{edu.degree}</p>
						<p class="entry-subtitle">{edu.institution}</p>
						{#if edu.grade}<p class="entry-desc">Grade: {edu.grade}</p>{/if}
					</div>
				</div>
			{/each}
		</section>
	{/if}

	<!-- ── Technical Skills ──────────────────────────── -->
	{#if data.skills.tech_skills.length > 0}
		<section>
			<h2 class="section-title">Technical Skills</h2>
			<div class="skill-grid">
				{#each data.skills.tech_skills as s, i (i)}
					<div class="skill-row">
						<span class="skill-name">{s.degree}</span>
						<span class="skill-dots">{dots(s.level)}</span>
						{#if s.years > 0}<span class="skill-years">{s.years}y</span>{/if}
					</div>
				{/each}
			</div>
		</section>
	{/if}

	<!-- ── Languages ─────────────────────────────────── -->
	{#if data.skills.lang_skills.length > 0}
		<section>
			<h2 class="section-title">Languages</h2>
			<div class="lang-grid">
				{#each data.skills.lang_skills as l, i (i)}
					<div class="lang-row">
						<span class="lang-name">{l.lang}</span>
						<span class="lang-lvl">{l.overall_lvl}</span>
						{#if l.speaking_lvl || l.writing_lvl}
							<span class="lang-detail">
								{#if l.speaking_lvl}Speaking: {l.speaking_lvl}{/if}
								{#if l.writing_lvl}
									· Writing: {l.writing_lvl}{/if}
							</span>
						{/if}
					</div>
				{/each}
			</div>
		</section>
	{/if}

	<!-- ── Soft Skills ────────────────────────────────── -->
	{#if data.skills.soft_skills.length > 0}
		<section>
			<h2 class="section-title">Soft Skills</h2>
			<p class="soft-skills-list">
				{data.skills.soft_skills
					.filter((s) => s.degree)
					.map((s) => s.degree)
					.join(' · ')}
			</p>
		</section>
	{/if}

	<!-- ── Driving ────────────────────────────────────── -->
	{#if data.skills.driving_skills.length > 0}
		<section>
			<h2 class="section-title">Driving License</h2>
			<p class="soft-skills-list">
				{data.skills.driving_skills
					.filter((d) => d.driving_license)
					.map((d) => d.driving_license)
					.join(', ')}
			</p>
		</section>
	{/if}

	<!-- ── Certifications ─────────────────────────────── -->
	{#if data.certifications.length > 0}
		<section>
			<h2 class="section-title">Certifications</h2>
			<ul class="simple-list">
				{#each data.certifications as c, i (i)}
					{#if c.title}
						<li>
							{c.title}{#if c.released_at}
								<span class="muted">({c.released_at})</span>{/if}
						</li>
					{/if}
				{/each}
			</ul>
		</section>
	{/if}

	<!-- ── Publications ───────────────────────────────── -->
	{#if data.publications.length > 0}
		<section>
			<h2 class="section-title">Publications</h2>
			<ul class="pub-list">
				{#each data.publications as pub, i (i)}
					{#if pub.title}
						<li>
							{#if pub.authors}<span class="pub-authors">{pub.authors}.</span>{/if}
							<em>"{pub.title}"</em>.
							{#if pub.journal}<span class="pub-journal">{pub.journal}.</span>{/if}
							{#if pub.details}<span class="muted">{pub.details}</span>{/if}
						</li>
					{/if}
				{/each}
			</ul>
		</section>
	{/if}

	<!-- ── Cover Letter ───────────────────────────────── -->
	{#if data.letter.is_active && data.letter.content}
		<section>
			<h2 class="section-title">Cover Letter</h2>
			{#if data.letter.company.name}
				<div class="letter-company">
					<p>{data.letter.company.name}</p>
					{#if data.letter.company.address}<p>{data.letter.company.address}</p>{/if}
					{#if data.letter.company.city}<p>{data.letter.company.city}</p>{/if}
				</div>
			{/if}
			<p class="letter-body">{data.letter.content}</p>
		</section>
	{/if}
</div>

<style>
	/* ── Reset & base ─────────────────────────────────── */
	.cv {
		--accent: #0f172a; /* Slate 900 for a more elegant, professional look */
		--text: #334155;   /* Slate 700 */
		--heading: #0f172a;
		--muted: #64748b;  /* Slate 500 */
		--border: #e2e8f0; /* Slate 200 */
		--date-w: 110px;

		font-family: 'Inter', system-ui, -apple-system, sans-serif;
		font-size: 10pt;
		line-height: 1.6;
		color: var(--text);
		background: white;
		max-width: 210mm;
		margin: 0 auto;
		padding: 14mm 20mm 18mm;
		box-sizing: border-box;
	}

	/* ── Header ──────────────────────────────────────── */
	.cv-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		gap: 20px;
		padding-bottom: 16px;
		border-bottom: 3px solid var(--accent);
		margin-bottom: 24px;
	}

	h1 {
		font-size: 28pt;
		font-weight: 800;
		margin: 0 0 6px;
		line-height: 1.1;
		letter-spacing: -0.02em;
	}

	.name-light {
		color: var(--heading);
		font-weight: 300;
	}

	.name-bold {
		color: var(--accent);
		font-weight: 800;
	}

	.job-title {
		margin: 0;
		font-size: 12pt;
		color: var(--muted);
		font-weight: 500;
		letter-spacing: 0.01em;
	}

	.cv-contact {
		list-style: none;
		margin: 0;
		padding: 0;
		font-size: 9pt;
		color: var(--text);
		text-align: right;
		line-height: 1.8;
	}

	.icon {
		display: inline-block;
		width: 16px;
		text-align: center;
		margin-right: 6px;
		color: var(--muted);
	}

	/* ── Sections ────────────────────────────────────── */
	section {
		margin-bottom: 20px;
	}

	.section-title {
		font-size: 12pt;
		font-weight: 700;
		color: var(--heading);
		margin: 0 0 12px;
		padding-bottom: 4px;
		border-bottom: 1px solid var(--border);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		break-after: avoid;
	}

	/* ── Timeline entries ────────────────────────────── */
	.entry {
		display: grid;
		grid-template-columns: var(--date-w) 1fr;
		gap: 12px 16px;
		margin-bottom: 16px;
		break-inside: avoid;
	}

	.entry-date {
		font-size: 8.5pt;
		color: var(--muted);
		text-align: right;
		padding-top: 2px;
		line-height: 1.5;
		font-weight: 500;
	}

	.entry-title {
		margin: 0;
		font-weight: 700;
		font-size: 11pt;
		color: var(--heading);
	}

	.entry-subtitle {
		margin: 2px 0 4px;
		color: var(--accent);
		font-size: 10pt;
		font-weight: 500;
	}

	.entry-desc {
		margin: 4px 0 0;
		font-size: 9.5pt;
		color: var(--text);
	}

	.achievements {
		margin: 6px 0 0 0;
		padding-left: 18px;
		font-size: 9.5pt;
		color: var(--text);
	}

	.achievements li {
		margin-bottom: 4px;
	}
	.achievements li::marker {
		color: var(--muted);
	}

	/* ── Tech skills ─────────────────────────────────── */
	.skill-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
		gap: 6px 24px;
	}

	.skill-row {
		display: flex;
		align-items: baseline;
		gap: 8px;
		font-size: 9.5pt;
	}

	.skill-name {
		min-width: 90px;
		font-weight: 600;
		color: var(--heading);
	}

	.skill-dots {
		color: var(--accent);
		letter-spacing: 2px;
		font-size: 8pt;
	}

	.skill-years {
		color: var(--muted);
		font-size: 8pt;
	}

	/* ── Languages ───────────────────────────────────── */
	.lang-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
		gap: 6px 24px;
	}

	.lang-row {
		display: flex;
		align-items: baseline;
		gap: 8px;
		font-size: 9.5pt;
	}

	.lang-name {
		min-width: 80px;
		font-weight: 600;
		color: var(--heading);
	}

	.lang-lvl {
		color: var(--accent);
		font-weight: 700;
		min-width: 40px;
	}

	.lang-detail {
		color: var(--muted);
		font-size: 8.5pt;
	}

	/* ── Soft skills ─────────────────────────────────── */
	.soft-skills-list {
		margin: 0;
		font-size: 9.5pt;
		color: var(--text);
		line-height: 1.6;
	}

	/* ── Lists ───────────────────────────────────────── */
	.simple-list {
		margin: 0;
		padding-left: 18px;
		font-size: 9.5pt;
	}

	.simple-list li {
		margin-bottom: 4px;
	}
	.simple-list li::marker {
		color: var(--muted);
	}

	.pub-list {
		margin: 0;
		padding-left: 18px;
		font-size: 9.5pt;
	}

	.pub-list li {
		margin-bottom: 6px;
	}
	.pub-list li::marker {
		color: var(--muted);
	}

	.pub-authors {
		font-weight: 600;
		color: var(--heading);
	}

	.pub-journal {
		font-style: italic;
	}

	.muted {
		color: var(--muted);
	}

	/* ── Cover letter ────────────────────────────────── */
	.letter-company {
		font-size: 9.5pt;
		margin-bottom: 16px;
	}

	.letter-company p {
		margin: 2px 0;
	}

	.letter-body {
		font-size: 10pt;
		line-height: 1.8;
		white-space: pre-line;
	}

	/* ── Print ───────────────────────────────────────── */
	@media print {
		.cv {
			padding: 0;
			max-width: none;
		}
	}
</style>
