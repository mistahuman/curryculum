<script lang="ts">
    import { cvState } from '$lib/state/cvState.svelte';
</script>

<div class="cv-preview-container bg-white text-black p-8 shadow-xl max-w-4xl mx-auto min-h-[1056px]">
    <!-- Header: Personal Info -->
    <header class="border-b-2 border-gray-300 pb-6 mb-6">
        <h1 class="text-4xl font-bold uppercase tracking-wider text-gray-900">
            {cvState.personal_info.name} {cvState.personal_info.surname}
        </h1>
        <div class="mt-4 flex flex-wrap gap-y-2 gap-x-6 text-sm text-gray-700">
            {#if cvState.personal_info.email}
                <div class="flex items-center gap-1">
                    <span class="font-semibold text-gray-900">Email:</span> {cvState.personal_info.email}
                </div>
            {/if}
            {#if cvState.personal_info.phone}
                <div class="flex items-center gap-1">
                    <span class="font-semibold text-gray-900">Phone:</span> {cvState.personal_info.phone}
                </div>
            {/if}
            {#if cvState.personal_info.address}
                <div class="flex items-center gap-1">
                    <span class="font-semibold text-gray-900">Address:</span> {cvState.personal_info.address}
                </div>
            {/if}
            {#if cvState.personal_info.github}
                <div class="flex items-center gap-1">
                    <span class="font-semibold text-gray-900">GitHub:</span> {cvState.personal_info.github}
                </div>
            {/if}
            {#if cvState.personal_info.linkedin}
                <div class="flex items-center gap-1">
                    <span class="font-semibold text-gray-900">LinkedIn:</span> {cvState.personal_info.linkedin}
                </div>
            {/if}
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Left Column: Experience & Education -->
        <div class="md:col-span-2 space-y-8">
            <!-- Experience -->
            {#if cvState.experience.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Experience</h2>
                    <div class="space-y-6">
                        {#each cvState.experience as exp}
                            <div>
                                <div class="flex justify-between items-baseline">
                                    <h3 class="text-lg font-bold text-gray-800">{exp.job_title}</h3>
                                    <span class="text-sm text-gray-500 font-medium whitespace-nowrap ml-4">
                                        {exp.start_date || 'Present'} - {exp.end_date || 'Present'}
                                    </span>
                                </div>
                                <div class="text-md font-semibold text-gray-600 mb-2">
                                    {exp.company} {#if exp.company_type} <span class="text-gray-400 font-normal">| {exp.company_type}</span>{/if}
                                </div>
                                <p class="text-sm text-gray-700 whitespace-pre-wrap">{exp.description}</p>
                            </div>
                        {/each}
                    </div>
                </section>
            {/if}

            <!-- Education -->
            {#if cvState.education.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Education</h2>
                    <div class="space-y-4">
                        {#each cvState.education as edu}
                            <div>
                                <div class="flex justify-between items-baseline">
                                    <h3 class="text-lg font-bold text-gray-800">{edu.degree}</h3>
                                    <span class="text-sm text-gray-500 font-medium">{edu.graduation_year}</span>
                                </div>
                                <div class="text-md text-gray-600">{edu.institution}</div>
                            </div>
                        {/each}
                    </div>
                </section>
            {/if}
        </div>

        <!-- Right Column: Skills -->
        <div class="space-y-8">
            <!-- Tech Skills -->
            {#if cvState.skills.tech_skills.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Tech Skills</h2>
                    <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
                        {#each cvState.skills.tech_skills as skill}
                            <li>{skill.degree}</li>
                        {/each}
                    </ul>
                </section>
            {/if}

            <!-- Soft Skills -->
            {#if cvState.skills.soft_skills.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Soft Skills</h2>
                    <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
                        {#each cvState.skills.soft_skills as skill}
                            <li>{skill.degree}</li>
                        {/each}
                    </ul>
                </section>
            {/if}

            <!-- Language Skills -->
            {#if cvState.skills.lang_skills.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Languages</h2>
                    <div class="space-y-3">
                        {#each cvState.skills.lang_skills as skill}
                            <div class="text-sm">
                                <span class="font-bold text-gray-800">{skill.lang}</span>
                                <div class="text-gray-600 text-xs mt-1 grid grid-cols-2 gap-1">
                                    {#if skill.overall_lvl}<div>Overall: {skill.overall_lvl}</div>{/if}
                                    {#if skill.speaking_lvl}<div>Speaking: {skill.speaking_lvl}</div>{/if}
                                    {#if skill.writing_lvl}<div>Writing: {skill.writing_lvl}</div>{/if}
                                    {#if skill.listening_lvl}<div>Listening: {skill.listening_lvl}</div>{/if}
                                </div>
                            </div>
                        {/each}
                    </div>
                </section>
            {/if}

            <!-- Driving Skills -->
            {#if cvState.skills.driving_skills.length > 0}
                <section>
                    <h2 class="text-xl font-bold uppercase border-b border-gray-200 pb-2 mb-4 text-gray-900">Driving</h2>
                    <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
                        {#each cvState.skills.driving_skills as skill}
                            <li>{skill.driving_license}</li>
                        {/each}
                    </ul>
                </section>
            {/if}
        </div>
    </div>
</div>
