<script lang="ts">
    import PersonalInfoForm from '$lib/components/cv-forms/PersonalInfoForm.svelte';
    import ExperienceForm from '$lib/components/cv-forms/ExperienceForm.svelte';
    import EducationForm from '$lib/components/cv-forms/EducationForm.svelte';
    import SkillsForm from '$lib/components/cv-forms/SkillsForm.svelte';
    import HTMLCVPreview from '$lib/components/preview/HTMLCVPreview.svelte';

    function printCV() {
        window.print();
    }
</script>

<div class="container mx-auto p-4 md:p-8 space-y-8 print:p-0 print:m-0 print:max-w-none print:w-full">
    <!-- Header Controls (Hidden during print) -->
    <div class="flex justify-between items-center bg-surface-100-800-token p-4 rounded-container-token shadow-sm print:hidden">
        <h1 class="h2 font-bold text-primary-500">CV Builder</h1>
        <button class="btn variant-filled-primary" onclick={printCV}>
            🖨️ Print CV
        </button>
    </div>

    <!-- Main Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 print:block">
        <!-- Left Column: Forms (Hidden during print) -->
        <div class="space-y-6 print:hidden">
            <h2 class="h3 mb-4">Edit Details</h2>

            <details class="card p-4 space-y-4 variant-glass" open>
                <summary class="h4 font-bold cursor-pointer hover:text-primary-500 transition-colors">Personal Info</summary>
                <div class="pt-4 border-t border-surface-500/20 mt-4">
                    <PersonalInfoForm />
                </div>
            </details>

            <details class="card p-4 space-y-4 variant-glass">
                <summary class="h4 font-bold cursor-pointer hover:text-primary-500 transition-colors">Experience</summary>
                <div class="pt-4 border-t border-surface-500/20 mt-4">
                    <ExperienceForm />
                </div>
            </details>

            <details class="card p-4 space-y-4 variant-glass">
                <summary class="h4 font-bold cursor-pointer hover:text-primary-500 transition-colors">Education</summary>
                <div class="pt-4 border-t border-surface-500/20 mt-4">
                    <EducationForm />
                </div>
            </details>

            <details class="card p-4 space-y-4 variant-glass">
                <summary class="h4 font-bold cursor-pointer hover:text-primary-500 transition-colors">Skills</summary>
                <div class="pt-4 border-t border-surface-500/20 mt-4">
                    <SkillsForm />
                </div>
            </details>
        </div>

        <!-- Right Column: Live Preview -->
        <div class="lg:sticky lg:top-8 self-start print:block print:w-full print:static">
            <h2 class="h3 mb-4 print:hidden">Live Preview</h2>
            <div class="border-4 border-surface-200-700-token rounded-container-token overflow-hidden shadow-2xl print:border-none print:shadow-none print:rounded-none bg-surface-backdrop-token">
                <HTMLCVPreview />
            </div>
        </div>
    </div>
</div>
