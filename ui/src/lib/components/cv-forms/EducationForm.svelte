<script lang="ts">
    import { cvState, type Education } from '$lib/state/cvState.svelte';

    function addEducation() {
        const newEdu: Education = {
            id: crypto.randomUUID(),
            degree: '',
            institution: '',
            graduation_year: ''
        };
        cvState.education = [...cvState.education, newEdu];
    }

    function removeEducation(id: string) {
        cvState.education = cvState.education.filter(edu => edu.id !== id);
    }
</script>

<div class="space-y-6">
    <div class="flex items-center justify-between">
        <h3 class="h3 font-bold">Education</h3>
        <button type="button" class="btn variant-filled-primary" onclick={addEducation}>
            + Add Education
        </button>
    </div>

    {#if cvState.education.length === 0}
        <p class="text-surface-500-400-token">No education added yet.</p>
    {/if}

    <div class="space-y-4">
        {#each cvState.education as edu (edu.id)}
            <div class="card p-4 space-y-4 relative variant-ghost-surface">
                <button 
                    type="button" 
                    class="btn-icon btn-icon-sm variant-filled-error absolute top-2 right-2"
                    onclick={() => removeEducation(edu.id)}
                    aria-label="Remove Education"
                >
                    ✕
                </button>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <label class="label">
                        <span>Degree / Major</span>
                        <input class="input" type="text" bind:value={edu.degree} placeholder="B.Sc. Computer Science" />
                    </label>
                    <label class="label">
                        <span>Institution</span>
                        <input class="input" type="text" bind:value={edu.institution} placeholder="University of Examples" />
                    </label>
                    <label class="label md:col-span-2">
                        <span>Graduation Year</span>
                        <input class="input" type="number" bind:value={edu.graduation_year} placeholder="2024" />
                    </label>
                </div>
            </div>
        {/each}
    </div>
</div>
