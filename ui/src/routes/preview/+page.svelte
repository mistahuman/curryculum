<script lang="ts">
	import { cvStore } from '$lib/stores/cv.svelte';
	import { templates, getTemplate } from '$lib/templates/registry';
	import { ArrowLeft, Download, LoaderCircle } from 'lucide-svelte';
	import { resolve } from '$app/paths';
	import { browser } from '$app/environment';

	let selectedId = $state('modern');
	const selected = $derived(getTemplate(selectedId));
	const TemplateComponent = $derived(selected.component);

	let isExporting = $state(false);

	async function downloadPDF() {
		if (!browser) return;
		isExporting = true;
		
		try {
			// Dynamic import since html2pdf.js requires window/document
			const html2pdf = (await import('html2pdf.js')).default;
			
			// Select the wrapper that contains the true A4 dimensions and CSS
			const el = document.querySelector('.cv-wrapper');
			if (!el) return;

			const name = cvStore.data.personal_info.name || 'cv';
			const surname = cvStore.data.personal_info.surname || '';
			const filename = `${name}_${surname}_cv`.trim().replace(/\s+/g, '_').toLowerCase() + '.pdf';

			const opt = {
				margin: 0,
				filename: filename,
				image: { type: 'jpeg', quality: 1 },
				// html2canvas settings: scale 2 for high-res text
				html2canvas: { scale: 2, useCORS: true },
				jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
			};

			await html2pdf().set(opt).from(el).save();
		} catch (e) {
			console.error('Error generating PDF:', e);
			alert('Si è verificato un errore durante la generazione del PDF.');
		} finally {
			isExporting = false;
		}
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
		<button 
			class="btn preset-filled-primary-500 btn-sm" 
			onclick={downloadPDF}
			disabled={isExporting}
		>
			{#if isExporting}
				<LoaderCircle size={14} class="animate-spin" /> Generazione...
			{:else}
				<Download size={14} /> Scarica PDF
			{/if}
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

	/* We ensure the wrapper occupies full A4 area so html2pdf captures it perfectly */
	.cv-wrapper {
		width: 100%;
		height: 100%;
	}
</style>
