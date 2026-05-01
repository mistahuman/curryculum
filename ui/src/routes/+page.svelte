<script lang="ts">
  import { Tabs, Dialog, Portal } from '@skeletonlabs/skeleton-svelte';
  import { cvStore } from '$lib/stores/cv.svelte';
  import PersonalInfoSection from '@components/form/PersonalInfoSection.svelte';
  import ExperienceSection from '@components/form/ExperienceSection.svelte';
  import EducationSection from '@components/form/EducationSection.svelte';
  import SkillsSection from '@components/form/SkillsSection.svelte';
  import CertificationsSection from '@components/form/CertificationsSection.svelte';
  import PublicationsSection from '@components/form/PublicationsSection.svelte';
  import LetterSection from '@components/form/LetterSection.svelte';
  import OptionsSection from '@components/form/OptionsSection.svelte';
  import { Download, Upload, Eye, RotateCcw, X } from 'lucide-svelte';
  import { base } from '$app/paths';

  let activeId = $state('personal');

  const counts = $derived({
    experience: cvStore.data.experience.length,
    education: cvStore.data.education.length,
    skills:
      cvStore.data.skills.tech_skills.length +
      cvStore.data.skills.soft_skills.length +
      cvStore.data.skills.lang_skills.length +
      cvStore.data.skills.driving_skills.length,
    certs: cvStore.data.certifications.length,
    pubs: cvStore.data.publications.length,
    letter: cvStore.data.letter.is_active ? 1 : 0,
  });

  let fileInput: HTMLInputElement;

  async function onFileChange(e: Event) {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;
    try {
      await cvStore.importJSON(file);
    } catch (err) {
      alert('Invalid JSON file: ' + (err as Error).message);
    }
    fileInput.value = '';
  }

  $effect(() => {
    JSON.stringify(cvStore.data);
    cvStore.save();
  });
</script>

<input
  bind:this={fileInput}
  type="file"
  accept=".json,application/json"
  class="sr-only"
  onchange={onFileChange}
/>

<!--
  Tabs fills the flex-1 main — flex-col so app-bar, tab-bar and content stack vertically.
  min-h-0 is critical: without it, a flex child won't shrink below its content height,
  making overflow-y-auto on the content panel ineffective.
-->
<Tabs
  value={activeId}
  onValueChange={(d) => (activeId = d.value)}
  class="cv-tabs flex flex-col flex-1 min-h-0"
>
  <!-- ── App bar ──────────────────────────────────────────── -->
  <div
    class="flex items-center gap-2 px-4 h-12 border-b border-surface-200-800 shrink-0 bg-surface-50-950"
  >
    <span class="text-sm font-semibold mr-auto truncate">
      {#if cvStore.data.personal_info.name || cvStore.data.personal_info.surname}
        {cvStore.data.personal_info.name} {cvStore.data.personal_info.surname}
      {:else}
        <span class="opacity-40">Unnamed CV</span>
      {/if}
    </span>

    {#if cvStore.data.code}
      <span class="badge preset-tonal text-xs hidden sm:inline-flex">{cvStore.data.code}</span>
    {/if}

    <button
      class="btn-icon hover:preset-tonal"
      onclick={() => fileInput.click()}
      title="Import JSON"
    >
      <Upload size={16} />
    </button>
    <button
      class="btn-icon hover:preset-tonal"
      onclick={() => cvStore.exportJSON()}
      title="Export JSON"
    >
      <Download size={16} />
    </button>
    <a class="btn preset-filled-primary-500 btn-sm gap-1.5" href="{base}/preview">
      <Eye size={15} /> Preview
    </a>

    <Dialog>
      <Dialog.Trigger class="btn-icon hover:preset-tonal-error" title="Reset all data">
        <RotateCcw size={15} />
      </Dialog.Trigger>
      <Portal>
        <Dialog.Backdrop class="fixed inset-0 z-50 bg-surface-950/60 backdrop-blur-sm" />
        <Dialog.Positioner class="fixed inset-0 z-50 flex justify-center items-center p-4">
          <Dialog.Content
            class="card bg-surface-100-900 border border-surface-200-800 w-full max-w-sm shadow-xl divide-y divide-surface-200-800 overflow-hidden p-0"
          >
            <header class="flex justify-between items-center px-4 py-3">
              <Dialog.Title class="font-bold">Reset CV Data</Dialog.Title>
              <Dialog.CloseTrigger class="btn-icon hover:preset-tonal"
                ><X size={16} /></Dialog.CloseTrigger
              >
            </header>
            <article class="px-4 py-4">
              <Dialog.Description class="text-sm opacity-60">
                This will permanently clear all CV data from your browser. This action cannot be
                undone.
              </Dialog.Description>
            </article>
            <footer class="flex justify-end gap-2 px-4 py-3">
              <Dialog.CloseTrigger class="btn preset-tonal">Cancel</Dialog.CloseTrigger>
              <Dialog.CloseTrigger
                class="btn preset-filled-error-500"
                onclick={() => cvStore.reset()}
              >
                Reset
              </Dialog.CloseTrigger>
            </footer>
          </Dialog.Content>
        </Dialog.Positioner>
      </Portal>
    </Dialog>
  </div>

  <!-- ── Tab bar ──────────────────────────────────────────── -->
  <!--
    overflow-x: auto lives on the WRAPPER, not on Tabs.List.
    Tabs.List must be non-overflowing so Tabs.Indicator (position: absolute)
    is positioned relative to the list and not clipped.
  -->
  <div class="tab-scroll-wrapper shrink-0 bg-surface-50-950">
    <Tabs.List class="tab-list">
      <Tabs.Trigger value="personal">Personal</Tabs.Trigger>
      <Tabs.Trigger value="experience">
        Experience{#if counts.experience > 0}&nbsp;<span class="count-badge"
            >{counts.experience}</span
          >{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="education">
        Education{#if counts.education > 0}&nbsp;<span class="count-badge">{counts.education}</span
          >{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="skills">
        Skills{#if counts.skills > 0}&nbsp;<span class="count-badge">{counts.skills}</span>{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="certs">
        Certifications{#if counts.certs > 0}&nbsp;<span class="count-badge">{counts.certs}</span
          >{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="pubs">
        Publications{#if counts.pubs > 0}&nbsp;<span class="count-badge">{counts.pubs}</span>{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="letter">
        Cover Letter{#if counts.letter > 0}&nbsp;<span class="count-badge count-badge-success"
            >✓</span
          >{/if}
      </Tabs.Trigger>
      <Tabs.Trigger value="options">Options</Tabs.Trigger>
      <Tabs.Indicator />
    </Tabs.List>
  </div>

  <!-- ── Content panels ───────────────────────────────────── -->
  <!--
    Single scrollable container for all panels.
    flex-1 + min-h-0 ensure it fills remaining space without overflowing the viewport.
  -->
  <div class="flex-1 overflow-y-auto min-h-0">
    <Tabs.Content value="personal" class="tab-content"><PersonalInfoSection /></Tabs.Content>
    <Tabs.Content value="experience" class="tab-content"><ExperienceSection /></Tabs.Content>
    <Tabs.Content value="education" class="tab-content"><EducationSection /></Tabs.Content>
    <Tabs.Content value="skills" class="tab-content"><SkillsSection /></Tabs.Content>
    <Tabs.Content value="certs" class="tab-content"><CertificationsSection /></Tabs.Content>
    <Tabs.Content value="pubs" class="tab-content"><PublicationsSection /></Tabs.Content>
    <Tabs.Content value="letter" class="tab-content"><LetterSection /></Tabs.Content>
    <Tabs.Content value="options" class="tab-content"><OptionsSection /></Tabs.Content>
  </div>
</Tabs>

<style>
  /* ── Tab scroll wrapper ──────────────────────────────────── */
  .tab-scroll-wrapper {
    overflow-x: auto;
    scrollbar-width: none;
  }
  .tab-scroll-wrapper::-webkit-scrollbar {
    display: none;
  }

  /* ── Tabs.List overrides ─────────────────────────────────── */
  /* Skeleton adds margin-bottom: spacing(4) for standalone use — remove it
     since our flex layout handles spacing. Keep min-width so scroll works. */
  :global(.cv-tabs [data-part='list']) {
    min-width: max-content;
    margin-bottom: 0;
    padding-inline: 8px;
  }

  /* Highlight the selected trigger — Skeleton only uses the indicator by
     default, so we add a text-color + weight cue for better readability. */
  :global(.cv-tabs [data-part='trigger'][data-selected]) {
    color: var(--color-primary-500);
    font-weight: 600;
  }

  /* ── Content panel ───────────────────────────────────────── */
  :global(.tab-content) {
    padding: 24px 16px;
    max-width: 760px;
    width: 100%;
    margin: 0 auto;
    box-sizing: border-box;
  }

  /* ── Count badges ────────────────────────────────────────── */
  :global(.count-badge) {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.65rem;
    font-weight: 600;
    line-height: 1;
    padding: 2px 5px;
    border-radius: 9999px;
    background-color: var(--color-primary-500);
    color: var(--color-primary-contrast-500);
  }
  :global(.count-badge-success) {
    background-color: var(--color-success-500);
    color: var(--color-success-contrast-500);
  }
</style>
