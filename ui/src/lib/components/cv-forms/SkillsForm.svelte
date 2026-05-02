<script lang="ts">
    import { cvState, type SkillItem } from '$lib/state/cvState.svelte';

    function addTechSkill() {
        cvState.skills.tech_skills = [...cvState.skills.tech_skills, { id: crypto.randomUUID(), degree: '' }];
    }
    function removeTechSkill(id: string) {
        cvState.skills.tech_skills = cvState.skills.tech_skills.filter(s => s.id !== id);
    }

    function addSoftSkill() {
        cvState.skills.soft_skills = [...cvState.skills.soft_skills, { id: crypto.randomUUID(), degree: '' }];
    }
    function removeSoftSkill(id: string) {
        cvState.skills.soft_skills = cvState.skills.soft_skills.filter(s => s.id !== id);
    }

    function addLangSkill() {
        cvState.skills.lang_skills = [...cvState.skills.lang_skills, { 
            id: crypto.randomUUID(), 
            lang: '', 
            speaking_lvl: '', 
            writing_lvl: '', 
            listening_lvl: '', 
            comprehension_level: '', 
            overall_lvl: '' 
        }];
    }
    function removeLangSkill(id: string) {
        cvState.skills.lang_skills = cvState.skills.lang_skills.filter(s => s.id !== id);
    }

    function addDrivingSkill() {
        cvState.skills.driving_skills = [...cvState.skills.driving_skills, { id: crypto.randomUUID(), driving_license: '' }];
    }
    function removeDrivingSkill(id: string) {
        cvState.skills.driving_skills = cvState.skills.driving_skills.filter(s => s.id !== id);
    }
</script>

<div class="space-y-8">
    <!-- Tech Skills -->
    <div class="space-y-4">
        <div class="flex items-center justify-between">
            <h3 class="h3 font-bold">Tech Skills</h3>
            <button type="button" class="btn variant-filled-primary btn-sm" onclick={addTechSkill}>+ Add</button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {#each cvState.skills.tech_skills as skill (skill.id)}
                <div class="input-group input-group-divider grid-cols-[1fr_auto]">
                    <input type="text" bind:value={skill.degree} placeholder="e.g. Python, React" />
                    <button class="variant-filled-error w-10" onclick={() => removeTechSkill(skill.id)}>✕</button>
                </div>
            {/each}
        </div>
    </div>

    <hr class="opacity-50" />

    <!-- Soft Skills -->
    <div class="space-y-4">
        <div class="flex items-center justify-between">
            <h3 class="h3 font-bold">Soft Skills</h3>
            <button type="button" class="btn variant-filled-primary btn-sm" onclick={addSoftSkill}>+ Add</button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {#each cvState.skills.soft_skills as skill (skill.id)}
                <div class="input-group input-group-divider grid-cols-[1fr_auto]">
                    <input type="text" bind:value={skill.degree} placeholder="e.g. Leadership, Teamwork" />
                    <button class="variant-filled-error w-10" onclick={() => removeSoftSkill(skill.id)}>✕</button>
                </div>
            {/each}
        </div>
    </div>

    <hr class="opacity-50" />

    <!-- Language Skills -->
    <div class="space-y-4">
        <div class="flex items-center justify-between">
            <h3 class="h3 font-bold">Language Skills</h3>
            <button type="button" class="btn variant-filled-primary btn-sm" onclick={addLangSkill}>+ Add</button>
        </div>
        {#each cvState.skills.lang_skills as skill (skill.id)}
            <div class="card p-4 space-y-4 relative variant-ghost-surface">
                <button type="button" class="btn-icon btn-icon-sm variant-filled-error absolute top-2 right-2" onclick={() => removeLangSkill(skill.id)}>✕</button>
                <label class="label">
                    <span>Language</span>
                    <input class="input" type="text" bind:value={skill.lang} placeholder="English, Spanish" />
                </label>
                <div class="grid grid-cols-2 md:grid-cols-5 gap-2">
                    <label class="label"><span class="text-xs">Speaking</span><input class="input" type="text" bind:value={skill.speaking_lvl} placeholder="B2" /></label>
                    <label class="label"><span class="text-xs">Writing</span><input class="input" type="text" bind:value={skill.writing_lvl} placeholder="B2" /></label>
                    <label class="label"><span class="text-xs">Listening</span><input class="input" type="text" bind:value={skill.listening_lvl} placeholder="C1" /></label>
                    <label class="label"><span class="text-xs">Comprehension</span><input class="input" type="text" bind:value={skill.comprehension_level} placeholder="C1" /></label>
                    <label class="label"><span class="text-xs">Overall</span><input class="input" type="text" bind:value={skill.overall_lvl} placeholder="B2" /></label>
                </div>
            </div>
        {/each}
    </div>

    <hr class="opacity-50" />

    <!-- Driving Skills -->
    <div class="space-y-4">
        <div class="flex items-center justify-between">
            <h3 class="h3 font-bold">Driving Skills</h3>
            <button type="button" class="btn variant-filled-primary btn-sm" onclick={addDrivingSkill}>+ Add</button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {#each cvState.skills.driving_skills as skill (skill.id)}
                <div class="input-group input-group-divider grid-cols-[1fr_auto]">
                    <input type="text" bind:value={skill.driving_license} placeholder="e.g. Class B" />
                    <button class="variant-filled-error w-10" onclick={() => removeDrivingSkill(skill.id)}>✕</button>
                </div>
            {/each}
        </div>
    </div>
</div>
