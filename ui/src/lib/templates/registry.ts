import type { Component } from 'svelte';
import type { CVData } from '$lib/types/cv';
import ModernCV from './ModernCV.svelte';

// ─── Template interface ───────────────────────────────────────────────────────
// Each CV template is a Svelte component that receives `data: CVData` as a prop
// and renders the full CV as HTML.
// To add a new template: create a Svelte component and add an entry here.

export interface CVTemplate {
	id: string;
	label: string;
	description: string;
	component: Component<{ data: CVData }>;
}

// ─── Registry ────────────────────────────────────────────────────────────────

export const templates: CVTemplate[] = [
	{
		id: 'modern',
		label: 'ModernCV',
		description: 'Classic two-column timeline layout with color-accented section headers.',
		component: ModernCV
	}
	// Add new templates here ↓
	// { id: 'europass', label: 'Europass', description: '...', component: EuropassCV },
];

export function getTemplate(id: string): CVTemplate {
	return templates.find((t) => t.id === id) ?? templates[0];
}
