import { cvApi } from '$lib/api/cv';

export const load = async () => {
	const profiles = await cvApi.list();
	return { profiles };
};
