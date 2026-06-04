import type { CVProfile, CVProfileSummary, CreateCVProfile } from '$lib/types/cv';

const BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
	const res = await fetch(`${BASE_URL}${path}`, {
		headers: { 'Content-Type': 'application/json', ...init?.headers },
		...init
	});
	if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
	if (res.status === 204) return undefined as T;
	return res.json();
}

export const cvApi = {
	list: () => request<CVProfileSummary[]>('/cv/'),

	get: (id: string) => request<CVProfile>(`/cv/${id}`),

	create: (payload: CreateCVProfile) =>
		request<CVProfile>('/cv/', { method: 'POST', body: JSON.stringify(payload) }),

	update: (id: string, payload: Partial<CVProfile>) =>
		request<CVProfile>(`/cv/${id}`, { method: 'PUT', body: JSON.stringify(payload) }),

	delete: (id: string) => request<void>(`/cv/${id}`, { method: 'DELETE' }),

	exportJson: async (id: string, filename: string) => {
		const res = await fetch(`${BASE_URL}/cv/${id}/export`);
		if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
		const blob = await res.blob();
		const url = URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = filename;
		a.click();
		URL.revokeObjectURL(url);
	},

	importJson: (payload: CreateCVProfile) =>
		request<CVProfile>('/cv/import', { method: 'POST', body: JSON.stringify(payload) })
};
