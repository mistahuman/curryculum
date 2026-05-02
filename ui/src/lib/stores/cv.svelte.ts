import type { CVData } from '$lib/types/cv';
import { DEFAULT_CV_DATA } from '$lib/types/cv';
import { browser } from '$app/environment';

const STORAGE_KEY = 'curryculum-cv-data';

function loadInitial(): CVData {
	if (!browser) return structuredClone(DEFAULT_CV_DATA);
	try {
		const stored = localStorage.getItem(STORAGE_KEY);
		if (stored) {
			// Merge with defaults so new fields added later don't break old saved data
			const parsed = JSON.parse(stored) as Partial<CVData>;
			return { ...structuredClone(DEFAULT_CV_DATA), ...parsed };
		}
	} catch {
		// ignore parse errors
	}
	return structuredClone(DEFAULT_CV_DATA);
}

class CVStore {
	data = $state<CVData>(loadInitial());

	save() {
		if (!browser) return;
		try {
			localStorage.setItem(STORAGE_KEY, JSON.stringify($state.snapshot(this.data)));
		} catch {
			// ignore quota errors
		}
	}

	exportJSON() {
		if (!browser) return;
		const json = JSON.stringify($state.snapshot(this.data), null, 2);
		const blob = new Blob([json], { type: 'application/json' });
		const url = URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = `${this.data.code || 'cv'}.json`;
		document.body.appendChild(a);
		a.click();
		document.body.removeChild(a);
		URL.revokeObjectURL(url);
	}

	async importJSON(file: File): Promise<void> {
		const text = await file.text();
		const parsed = JSON.parse(text) as Partial<CVData>;
		const merged = { ...structuredClone(DEFAULT_CV_DATA), ...parsed };
		// Replace data in-place to keep proxy alive
		Object.assign(this.data, merged);
		this.save();
	}

	reset() {
		Object.assign(this.data, structuredClone(DEFAULT_CV_DATA));
		this.save();
	}
}

export const cvStore = new CVStore();
