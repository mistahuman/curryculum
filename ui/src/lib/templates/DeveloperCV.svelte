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

<div class="cv dev-cv">
	<!-- Sidebar -->
	<aside class="sidebar">
		<!-- Contacts -->
		<section class="sidebar-section">
			<h2 class="sidebar-title">Contact</h2>
			<ul class="contact-list">
				{#if p.email}<li><span class="icon">✉</span>{p.email}</li>{/if}
				{#if p.phone}<li><span class="icon">☎</span>{p.phone}</li>{/if}
				{#if p.address}<li><span class="icon">⌂</span>{p.address}</li>{/if}
				{#if p.github}<li><span class="icon">⌥</span>github.com/{p.github}</li>{/if}
				{#if p.linkedin}<li><span class="icon">in</span>linkedin.com/in/{p.linkedin}</li>{/if}
			</ul>
		</section>

		<!-- Tech Skills -->
		{#if data.skills.tech_skills.length > 0}
			<section class="sidebar-section">
				<h2 class="sidebar-title">Tech Skills</h2>
				<ul class="skill-list">
					{#each data.skills.tech_skills as s, i (i)}
						<li>
							<div class="skill-head">
								<span class="skill-name">{s.degree}</span>
								{#if s.years > 0}<span class="skill-years">{s.years}y</span>{/if}
							</div>
							<div class="skill-dots">{dots(s.level)}</div>
						</li>
					{/each}
				</ul>
			</section>
		{/if}

		<!-- Languages -->
		{#if data.skills.lang_skills.length > 0}
			<section class="sidebar-section">
				<h2 class="sidebar-title">Languages</h2>
				<ul class="skill-list">
					{#each data.skills.lang_skills as l, i (i)}
						<li>
							<div class="skill-head">
								<span class="skill-name">{l.lang}</span>
								<span class="lang-lvl">{l.overall_lvl}</span>
							</div>
							{#if l.speaking_lvl || l.writing_lvl}
								<div class="lang-details">
									{#if l.speaking_lvl}S: {l.speaking_lvl}{/if}
									{#if l.speaking_lvl && l.writing_lvl} | {/if}
									{#if l.writing_lvl}W: {l.writing_lvl}{/if}
								</div>
							{/if}
						</li>
					{/each}
				</ul>
			</section>
		{/if}

		<!-- Soft Skills -->
		{#if data.skills.soft_skills.length > 0}
			<section class="sidebar-section">
				<h2 class="sidebar-title">Soft Skills</h2>
				<div class="tags">
					{#each data.skills.soft_skills.filter((s) => s.degree) as s}
						<span class="tag">{s.degree}</span>
					{/each}
				</div>
			</section>
		{/if}
	</aside>

	<!-- Main Content -->
	<main class="main-content">
		<header class="header">
			<h1>{p.name} <span class="text-accent">{p.surname}</span></h1>
			{#if p.job_title}<p class="job-title">{p.job_title}</p>{/if}
		</header>

		<!-- Work Experience -->
		{#if data.experience.length > 0}
			<section class="main-section">
				<h2 class="section-title">Experience</h2>
				<div class="timeline">
					{#each data.experience as exp, i (i)}
						<div class="timeline-item">
							<div class="timeline-marker"></div>
							<div class="timeline-content">
								<div class="flex-between">
									<h3 class="entry-title">{exp.job_title}</h3>
									<span class="entry-date">
										{fmtDate(exp.start_date)} – {exp.end_date ? fmtDate(exp.end_date) : 'Present'}
									</span>
								</div>
								<p class="entry-subtitle">
									{exp.company}{#if exp.company_type} · {exp.company_type}{/if}
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
				</div>
			</section>
		{/if}

		<!-- Education -->
		{#if data.education.length > 0}
			<section class="main-section">
				<h2 class="section-title">Education</h2>
				<div class="timeline">
					{#each data.education as edu, i (i)}
						<div class="timeline-item">
							<div class="timeline-marker"></div>
							<div class="timeline-content">
								<div class="flex-between">
									<h3 class="entry-title">{edu.degree}</h3>
									<span class="entry-date">
										{#if edu.start_date}{fmtYear(edu.start_date)} – {/if}{edu.graduation_year}
									</span>
								</div>
								<p class="entry-subtitle">{edu.institution}</p>
								{#if edu.grade}<p class="entry-desc">Grade: {edu.grade}</p>{/if}
							</div>
						</div>
					{/each}
				</div>
			</section>
		{/if}

		<!-- Projects / Certifications (combined if small) -->
		{#if data.certifications.length > 0 || data.publications.length > 0}
			<div class="grid-2-cols">
				{#if data.certifications.length > 0}
					<section class="main-section">
						<h2 class="section-title">Certifications</h2>
						<ul class="simple-list">
							{#each data.certifications as c, i (i)}
								{#if c.title}
									<li>
										{c.title}{#if c.released_at} <span class="muted">({c.released_at})</span>{/if}
									</li>
								{/if}
							{/each}
						</ul>
					</section>
				{/if}

				{#if data.publications.length > 0}
					<section class="main-section">
						<h2 class="section-title">Publications</h2>
						<ul class="simple-list pub-list">
							{#each data.publications as pub, i (i)}
								{#if pub.title}
									<li>
										{#if pub.authors}<span class="pub-authors">{pub.authors}.</span>{/if}
										<em>"{pub.title}"</em>.
										{#if pub.journal}<span class="pub-journal">{pub.journal}.</span>{/if}
									</li>
								{/if}
							{/each}
						</ul>
					</section>
				{/if}
			</div>
		{/if}
	</main>
</div>

<style>
	/* ── Dev CV Base ──────────────────────────────────── */
	.dev-cv {
		--bg-sidebar: #0f172a; /* Slate 900 */
		--text-sidebar: #e2e8f0; /* Slate 200 */
		--text-sidebar-muted: #94a3b8; /* Slate 400 */
		--accent-sidebar: #38bdf8; /* Sky 400 */
		
		--bg-main: #ffffff;
		--text-main: #334155; /* Slate 700 */
		--text-main-muted: #64748b; /* Slate 500 */
		--heading-main: #0f172a; /* Slate 900 */
		--accent-main: #0284c7; /* Sky 600 */
		--border-color: #cbd5e1; /* Slate 300 */

		font-family: 'JetBrains Mono', 'Fira Code', 'Inter', monospace, sans-serif;
		font-size: 9.5pt;
		line-height: 1.5;
		color: var(--text-main);
		background: var(--bg-main);
		max-width: 210mm;
		min-height: 297mm;
		margin: 0 auto;
		display: flex;
		box-sizing: border-box;
	}

	/* Force non-monospace for regular reading text if preferred, 
	   but keeping a clean sans-serif like Inter for the main part is good.
	   Let's use Inter for main, and maybe monospace for headers/sidebar to give a dev feel. */
	.dev-cv {
		font-family: 'Inter', system-ui, sans-serif;
	}

	/* ── Sidebar ──────────────────────────────────────── */
	.sidebar {
		width: 32%;
		background: var(--bg-sidebar);
		color: var(--text-sidebar);
		padding: 12mm 8mm;
		display: flex;
		flex-direction: column;
		gap: 24px;
	}

	.sidebar-section {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	.sidebar-title {
		font-family: 'JetBrains Mono', monospace;
		font-size: 11pt;
		font-weight: 700;
		color: var(--accent-sidebar);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		margin: 0;
		padding-bottom: 6px;
		border-bottom: 1px dashed rgba(255, 255, 255, 0.2);
	}

	.contact-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 8px;
		font-size: 9pt;
	}

	.contact-list .icon {
		display: inline-block;
		width: 18px;
		color: var(--accent-sidebar);
	}

	.skill-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.skill-head {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		margin-bottom: 2px;
	}

	.skill-name {
		font-weight: 600;
		font-size: 9.5pt;
	}

	.skill-years, .lang-lvl {
		font-size: 8.5pt;
		color: var(--text-sidebar-muted);
		font-family: 'JetBrains Mono', monospace;
	}

	.lang-lvl {
		color: var(--accent-sidebar);
		font-weight: 700;
	}

	.lang-details {
		font-size: 8pt;
		color: var(--text-sidebar-muted);
	}

	.skill-dots {
		color: var(--accent-sidebar);
		font-size: 7.5pt;
		letter-spacing: 2px;
	}

	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
	}

	.tag {
		background: rgba(255,255,255,0.1);
		color: var(--text-sidebar);
		padding: 3px 8px;
		border-radius: 4px;
		font-size: 8.5pt;
		font-weight: 500;
	}

	/* ── Main Content ─────────────────────────────────── */
	.main-content {
		width: 68%;
		padding: 14mm 14mm;
		display: flex;
		flex-direction: column;
		gap: 24px;
	}

	.header h1 {
		font-size: 32pt;
		font-weight: 800;
		color: var(--heading-main);
		margin: 0 0 4px;
		line-height: 1.1;
		letter-spacing: -0.02em;
	}

	.text-accent {
		color: var(--accent-main);
	}

	.job-title {
		font-family: 'JetBrains Mono', monospace;
		font-size: 13pt;
		font-weight: 600;
		color: var(--text-main-muted);
		margin: 0;
	}

	.main-section {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	.section-title {
		font-size: 14pt;
		font-weight: 800;
		color: var(--heading-main);
		margin: 0;
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.section-title::after {
		content: '';
		flex: 1;
		height: 2px;
		background: var(--border-color);
		opacity: 0.5;
	}

	/* Timeline */
	.timeline {
		display: flex;
		flex-direction: column;
		gap: 16px;
		border-left: 2px solid var(--border-color);
		padding-left: 16px;
		margin-left: 6px;
	}

	.timeline-item {
		position: relative;
	}

	.timeline-marker {
		position: absolute;
		left: -23px; /* 16px padding + 2px border / 2 + marker size */
		top: 6px;
		width: 10px;
		height: 10px;
		border-radius: 50%;
		background: var(--bg-main);
		border: 2px solid var(--accent-main);
	}

	.flex-between {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		gap: 12px;
		margin-bottom: 2px;
	}

	.entry-title {
		font-size: 11.5pt;
		font-weight: 700;
		color: var(--heading-main);
		margin: 0;
	}

	.entry-date {
		font-family: 'JetBrains Mono', monospace;
		font-size: 8.5pt;
		color: var(--text-main-muted);
		flex-shrink: 0;
	}

	.entry-subtitle {
		font-size: 10pt;
		font-weight: 600;
		color: var(--accent-main);
		margin: 0 0 6px 0;
	}

	.entry-desc {
		margin: 0;
		font-size: 9.5pt;
		line-height: 1.6;
	}

	.achievements {
		margin: 8px 0 0 0;
		padding-left: 18px;
		font-size: 9.5pt;
	}

	.achievements li {
		margin-bottom: 4px;
	}

	.achievements li::marker {
		color: var(--accent-main);
	}

	.grid-2-cols {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 20px;
	}

	.simple-list {
		margin: 0;
		padding-left: 16px;
		font-size: 9.5pt;
	}
	
	.simple-list li {
		margin-bottom: 6px;
	}

	.pub-authors {
		font-weight: 600;
	}

	.muted {
		color: var(--text-main-muted);
	}

	/* ── Print ───────────────────────────────────────── */
	@media print {
		.dev-cv {
			max-width: none;
			min-height: auto;
		}
		
		/* Ensure background colors print */
		.sidebar {
			-webkit-print-color-adjust: exact;
			print-color-adjust: exact;
		}
	}
</style>
