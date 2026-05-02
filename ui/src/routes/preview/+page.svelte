<script lang="ts">
	import { cvStore } from '$lib/stores/cv.svelte';
	import { templates, getTemplate } from '$lib/templates/registry';
	import { Printer, ArrowLeft, Download } from 'lucide-svelte';
	import { resolve } from '$app/paths';
	import { browser } from '$app/environment';

	let selectedId = $state('modern');
	const selected = $derived(getTemplate(selectedId));
	const TemplateComponent = $derived(selected.component);

	function printCV() {
		if (browser) window.print();
	}

	function exportHTML() {
		if (!browser) return;
		const el = document.querySelector('.cv-wrapper');
		if (!el) return;
		const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>CV – ${cvStore.data.personal_info.name} ${cvStore.data.personal_info.surname}</title>
  <style>* { box-sizing: border-box; } body { margin: 0; background: white; }</style>
</head>
<body>${el.innerHTML}</body>
</html>`;
		const blob = new Blob([html], { type: 'text/html' });
		const url = URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = `${cvStore.data.code || 'cv'}.html`;
		document.body.appendChild(a);
		a.click();
		document.body.removeChild(a);
		URL.revokeObjectURL(url);
	}
</script>

<!-- ── Toolbar ─────────────────────────────────── (hidden on print) ── -->
<div
	class="no-print flex shrink-0 flex-wrap items-center gap-3 border-b border-surface-200-800 bg-surface-50-950 px-4 py-2"
>
	<a class="btn preset-outlined-surface-300-700 btn-sm" href={resolve('/editor')}>
		<ArrowLeft size={14} /> Editor
	</a>

	<!-- Template selector -->
	<div class="flex items-center gap-2">
		<span class="text-xs font-bold tracking-widest uppercase opacity-40">Template</span>
		<div class="flex gap-1">
			{#each templates as t (t.id)}
				<button
					class="btn btn-sm"
					class:preset-filled-primary-500={selectedId === t.id}
					class:preset-outlined-surface-300-700={selectedId !== t.id}
					onclick={() => (selectedId = t.id)}
					title={t.description}
				>
					{t.label}
				</button>
			{/each}
		</div>
	</div>

	<div class="ml-auto flex gap-2">
		<button class="btn preset-outlined-surface-300-700 btn-sm" onclick={exportHTML}>
			<Download size={14} /> HTML
		</button>
		<button class="btn preset-filled-primary-500 btn-sm" onclick={printCV}>
			<Printer size={14} /> Print / PDF
		</button>
	</div>
</div>

<!-- ── Preview area ─────────────────────────────────────────────────── -->
<div class="preview-bg no-print">
	<div class="paper">
		<div class="cv-wrapper">
			<TemplateComponent data={cvStore.data} />
		</div>
	</div>
</div>

<!-- Print: render only the CV, no wrapper ─────────────────────────── -->
<div class="print-only cv-wrapper">
	<TemplateComponent data={cvStore.data} />
</div>

<style>
	.preview-bg {
		flex: 1;
		overflow-y: auto;
		overflow-x: auto;
		padding: 32px 24px;
		background: color-mix(in oklab, var(--color-surface-300) 30%, transparent);
		display: flex;
		justify-content: center;
		align-items: flex-start;
	}

	.paper {
		background: white;
		box-shadow: 0 8px 32px rgb(0 0 0 / 0.18);
		width: 210mm;
		min-height: 297mm;
		flex-shrink: 0;
	}

	@media print {
		.no-print {
			display: none !important;
		}
		.print-only {
			display: block !important;
		}

		:global(body) {
			background: white;
		}
	}

	.print-only {
		display: none;
	}
</style>
