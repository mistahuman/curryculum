<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { cvApi } from '$lib/api/cv';
	import { uiStore } from '$lib/stores/ui.svelte';
	import type { CreateCVProfile } from '$lib/types/cv';
	import { FileText, Plus, Upload, Download, Trash2, Pencil, Eye } from 'lucide-svelte';

	let { data } = $props();

	let newLabel = $state('');
	let showNewForm = $state(false);
	let importInput: HTMLInputElement;

	async function createProfile() {
		if (!newLabel.trim()) return;
		try {
			const profile = await cvApi.create({ label: newLabel.trim() });
			newLabel = '';
			showNewForm = false;
			goto(resolve(`/cv/${profile.id}`));
		} catch {
			uiStore.toast('Error creating CV', 'error');
		}
	}

	async function deleteProfile(id: string, label: string) {
		if (!confirm(`Delete "${label}"?`)) return;
		try {
			await cvApi.delete(id);
			await invalidateAll();
			uiStore.toast('CV deleted', 'success');
		} catch {
			uiStore.toast('Error deleting CV', 'error');
		}
	}

	async function exportProfile(id: string, label: string) {
		try {
			await cvApi.exportJson(id, `cv-${label.toLowerCase().replace(/\s+/g, '-')}.json`);
		} catch {
			uiStore.toast('Export failed', 'error');
		}
	}

	function handleImport(e: Event) {
		const file = (e.target as HTMLInputElement).files?.[0];
		if (!file) return;
		const reader = new FileReader();
		reader.onload = async (ev) => {
			try {
				const payload = JSON.parse(ev.target?.result as string) as CreateCVProfile;
				if (!payload.label) payload.label = file.name.replace('.json', '');
				await cvApi.importJson(payload);
				await invalidateAll();
				uiStore.toast(`Imported "${payload.label}"`, 'success');
			} catch {
				uiStore.toast('Import failed — invalid JSON', 'error');
			}
		};
		reader.readAsText(file);
		(e.target as HTMLInputElement).value = '';
	}
</script>

<div class="container mx-auto max-w-4xl space-y-8 px-4 py-10">
	<div class="flex items-center justify-between">
		<div>
			<h1 class="h2 font-bold">My CVs</h1>
			<p class="text-surface-600-400 mt-1 text-sm">
				{data.profiles.length} profile{data.profiles.length !== 1 ? 's' : ''}
			</p>
		</div>
		<div class="flex gap-2">
			<input bind:this={importInput} type="file" accept=".json" class="hidden" onchange={handleImport} />
			<button class="btn preset-tonal" onclick={() => importInput.click()}>
				<Upload size={16} /><span>Import JSON</span>
			</button>
			<button class="btn preset-filled-primary-500" onclick={() => (showNewForm = true)}>
				<Plus size={16} /><span>New CV</span>
			</button>
		</div>
	</div>

	{#if showNewForm}
		<div class="card bg-surface-100-900 space-y-3 p-4">
			<p class="font-medium">New CV profile</p>
			<div class="flex gap-2">
				<input
					class="input flex-1"
					type="text"
					placeholder="e.g. Software Engineer 2025"
					bind:value={newLabel}
					onkeydown={(e) => e.key === 'Enter' && createProfile()}
					autofocus
				/>
				<button class="btn preset-filled-primary-500" onclick={createProfile} disabled={!newLabel.trim()}>
					Create
				</button>
				<button class="btn preset-tonal" onclick={() => { showNewForm = false; newLabel = ''; }}>
					Cancel
				</button>
			</div>
		</div>
	{/if}

	{#if data.profiles.length === 0 && !showNewForm}
		<div class="flex flex-col items-center gap-4 py-20 text-center">
			<FileText size={48} class="text-surface-400" />
			<p class="text-surface-500 text-lg">No CVs yet</p>
			<button class="btn preset-filled-primary-500" onclick={() => (showNewForm = true)}>
				<Plus size={16} /><span>Create your first CV</span>
			</button>
		</div>
	{:else}
		<div class="space-y-3">
			{#each data.profiles as profile (profile.id)}
				<div class="card bg-surface-100-900 flex items-center gap-4 p-4">
					<div class="bg-primary-500/10 text-primary-500 flex size-10 shrink-0 items-center justify-center rounded-lg">
						<FileText size={20} />
					</div>
					<div class="min-w-0 flex-1">
						<p class="truncate font-semibold">{profile.label}</p>
						{#if profile.name || profile.surname}
							<p class="text-surface-500 text-sm">{profile.name} {profile.surname}</p>
						{/if}
					</div>
					<div class="flex shrink-0 gap-1">
						<a class="btn-icon preset-tonal" href={resolve(`/cv/${profile.id}/preview`)} title="Preview">
							<Eye size={16} />
						</a>
						<a class="btn-icon preset-tonal" href={resolve(`/cv/${profile.id}`)} title="Edit">
							<Pencil size={16} />
						</a>
						<button class="btn-icon preset-tonal" onclick={() => exportProfile(profile.id, profile.label)} title="Export JSON">
							<Download size={16} />
						</button>
						<button class="btn-icon hover:preset-filled-error-500" onclick={() => deleteProfile(profile.id, profile.label)} title="Delete">
							<Trash2 size={16} />
						</button>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
