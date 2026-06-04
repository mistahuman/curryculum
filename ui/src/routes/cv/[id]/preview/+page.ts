import { cvApi } from '$lib/api/cv';
import { error } from '@sveltejs/kit';

export const load = async ({ params }) => {
	try {
		const profile = await cvApi.get(params.id);
		return { profile };
	} catch {
		error(404, 'CV not found');
	}
};
