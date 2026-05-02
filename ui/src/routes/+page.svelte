<script lang="ts">
	import Logo from '$lib/components/icons/Logo.svelte';
	import Footer from '$lib/components/generic/Footer.svelte';
	import { FileText, Eye, Printer, ChevronRight } from 'lucide-svelte';
	import { resolve } from '$app/paths';

	const features = [
		{
			Icon: FileText,
			title: 'Compilazione guidata',
			desc: 'Sezioni dedicate per esperienze, formazione, competenze, lingue e molto altro.'
		},
		{
			Icon: Eye,
			title: 'Anteprima live',
			desc: 'Vedi il risultato finale in tempo reale mentre compili i tuoi dati.'
		},
		{
			Icon: Printer,
			title: 'Export PDF',
			desc: 'Stampa direttamente dal browser oppure scarica il CV in HTML.'
		}
	];
</script>

<!-- ── Hero ─────────────────────────────────────────────────────────────── -->
<section
	class="gradient-homepage-one flex min-h-[calc(100vh-70px)] flex-col items-center justify-center gap-10 px-4 text-center"
>
	<Logo width="72" height="72" />

	<div class="space-y-4">
		<h1 class="text-5xl font-bold tracking-tight md:text-7xl">
			Curry<span class="text-primary-500">culum</span>
		</h1>
		<p class="mx-auto max-w-sm text-lg opacity-60">
			Il tuo CV professionale, curato e sempre a portata di mano.
		</p>
	</div>

	<a class="btn preset-filled-primary-500 px-8 text-base" href={resolve('/editor')}>
		Crea il tuo CV <ChevronRight size={18} />
	</a>
</section>

<!-- ── Features ─────────────────────────────────────────────────────────── -->
<section class="container mx-auto max-w-4xl px-6 py-20">
	<div class="grid grid-cols-1 gap-4 md:grid-cols-3">
		{#each features as { Icon, title, desc } (title)}
			<div class="card space-y-3 border border-surface-200-800 preset-filled-surface-100-900 p-6">
				<div
					class="flex size-10 items-center justify-center rounded-lg bg-primary-500/10 text-primary-500"
				>
					<Icon size={20} />
				</div>
				<h3 class="font-semibold">{title}</h3>
				<p class="text-sm opacity-60">{desc}</p>
			</div>
		{/each}
	</div>
</section>

<!-- ── Footer ────────────────────────────────────────────────────────────── -->
<Footer />
