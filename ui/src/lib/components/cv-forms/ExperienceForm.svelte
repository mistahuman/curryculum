<script lang="ts">
    import { cvState, type Experience } from '$lib/state/cvState.svelte';

    function addExperience() {
        const newExp: Experience = {
            id: crypto.randomUUID(),
            job_title: '',
            company: '',
            company_type: '',
            start_date: '',
            end_date: '',
            description: ''
        };
        cvState.experience = [...cvState.experience, newExp];
    }

    function removeExperience(id: string) {
        cvState.experience = cvState.experience.filter(exp => exp.id !== id);
    }
</script>

<div class="space-y-6">
    <div class="flex items-center justify-between">
        <h3 class="h3 font-bold">Work Experience</h3>
        <button type="button" class="btn variant-filled-primary" onclick={addExperience}>
            + Add Experience
        </button>
    </div>

    {#if cvState.experience.length === 0}
        <p class="text-surface-500-400-token">No experience added yet.</p>
    {/if}

    <div class="space-y-4">
        {#each cvState.experience as exp (exp.id)}
            <div class="card p-4 space-y-4 relative variant-ghost-surface">
                <button 
                    type="button" 
                    class="btn-icon btn-icon-sm variant-filled-error absolute top-2 right-2"
                    onclick={() => removeExperience(exp.id)}
                    aria-label="Remove Experience"
                >
                    ✕
                </button>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <label class="label">
                        <span>Job Title</span>
                        <input class="input" type="text" bind:value={exp.job_title} placeholder="Software Engineer" />
                    </label>
                    <label class="label">
                        <span>Company</span>
                        <input class="input" type="text" bind:value={exp.company} placeholder="Acme Corp" />
                    </label>
                    <label class="label">
                        <span>Company Type</span>
                        <input class="input" type="text" bind:value={exp.company_type} placeholder="Technology" />
                    </label>
                    <div class="grid grid-cols-2 gap-2">
                        <label class="label">
                            <span>Start Date</span>
                            <input class="input" type="date" bind:value={exp.start_date} />
                        </label>
                        <label class="label">
                            <span>End Date</span>
                            <input class="input" type="date" bind:value={exp.end_date} />
                        </label>
                    </div>
                </div>
                <label class="label mt-4">
                    <span>Description</span>
                    <textarea class="textarea" rows="3" bind:value={exp.description} placeholder="Describe your responsibilities..."></textarea>
                </label>
            </div>
        {/each}
    </div>
</div>
