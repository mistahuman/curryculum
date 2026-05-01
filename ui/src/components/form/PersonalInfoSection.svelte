<script lang="ts">
  import { cvStore } from '$lib/stores/cv.svelte';
</script>

<form class="space-y-6">
  <!-- Name & Title -->
  <fieldset class="space-y-4">
    <legend class="text-xs font-bold uppercase tracking-widest opacity-50 mb-3">Identity</legend>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <label class="label">
        <span class="label-text">First Name</span>
        <input
          class="input"
          type="text"
          bind:value={cvStore.data.personal_info.name}
          placeholder="Marco"
        />
      </label>
      <label class="label">
        <span class="label-text">Last Name</span>
        <input
          class="input"
          type="text"
          bind:value={cvStore.data.personal_info.surname}
          placeholder="Rossi"
        />
      </label>
    </div>
    <label class="label">
      <span class="label-text">Professional Title</span>
      <input
        class="input"
        type="text"
        bind:value={cvStore.data.personal_info.job_title}
        placeholder="Software Engineer"
      />
    </label>
  </fieldset>

  <hr class="divider" />

  <!-- Contact -->
  <fieldset class="space-y-4">
    <legend class="text-xs font-bold uppercase tracking-widest opacity-50 mb-3">Contact</legend>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <label class="label">
        <span class="label-text">Email</span>
        <input
          class="input"
          type="email"
          bind:value={cvStore.data.personal_info.email}
          placeholder="marco@example.com"
        />
      </label>
      <label class="label">
        <span class="label-text">Phone</span>
        <input
          class="input"
          type="tel"
          bind:value={cvStore.data.personal_info.phone}
          placeholder="+39 333 1234567"
        />
      </label>
    </div>
    <label class="label">
      <span class="label-text">Address</span>
      <input
        class="input"
        type="text"
        bind:value={cvStore.data.personal_info.address}
        placeholder="Via Roma 1, Milan, Italy"
      />
    </label>
  </fieldset>

  <hr class="divider" />

  <!-- Personal details -->
  <fieldset class="space-y-4">
    <legend class="text-xs font-bold uppercase tracking-widest opacity-50 mb-3"
      >Personal Details</legend
    >
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <label class="label">
        <span class="label-text">Birthday</span>
        <input class="input" type="date" bind:value={cvStore.data.personal_info.birthday} />
      </label>
      <label class="label">
        <span class="label-text">Gender</span>
        <input
          class="input"
          type="text"
          bind:value={cvStore.data.personal_info.gender}
          placeholder="M / F / Other"
        />
      </label>
      <label class="label">
        <span class="label-text">Nationality</span>
        <input
          class="input"
          type="text"
          bind:value={cvStore.data.personal_info.nationality}
          placeholder="Italian"
        />
      </label>
    </div>
    <label class="label">
      <span class="label-text">Tax Code (Codice Fiscale)</span>
      <input
        class="input"
        type="text"
        bind:value={cvStore.data.personal_info.tax_code}
        placeholder="RSSMRC80A01F205X"
      />
    </label>
  </fieldset>

  <hr class="divider" />

  <!-- Social & Online -->
  <fieldset class="space-y-4">
    <legend class="text-xs font-bold uppercase tracking-widest opacity-50 mb-3"
      >Social & Online</legend
    >
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <label class="label">
        <span class="label-text">GitHub</span>
        <div class="input-group">
          <span class="input-group-prefix">github.com/</span>
          <input
            class="input"
            type="text"
            bind:value={cvStore.data.personal_info.github}
            placeholder="username"
          />
        </div>
      </label>
      <label class="label">
        <span class="label-text">LinkedIn</span>
        <div class="input-group">
          <span class="input-group-prefix">linkedin.com/in/</span>
          <input
            class="input"
            type="text"
            bind:value={cvStore.data.personal_info.linkedin}
            placeholder="username"
          />
        </div>
      </label>
    </div>
    <label class="label">
      <span class="label-text">Profile Picture Path (for PDF output)</span>
      <input
        class="input"
        type="text"
        bind:value={cvStore.data.personal_info.url_pic}
        placeholder="mycv/user.jpg"
      />
    </label>
  </fieldset>

  <hr class="divider" />

  <!-- Output settings -->
  <fieldset class="space-y-4">
    <legend class="text-xs font-bold uppercase tracking-widest opacity-50 mb-3">Output</legend>
    <label class="label">
      <span class="label-text">Filename Code</span>
      <div class="input-group">
        <span class="input-group-prefix">cv-</span>
        <input class="input" type="text" bind:value={cvStore.data.code} placeholder="mycv" />
        <span
          class="input-group-prefix"
          style="border-left:1px solid color-mix(in oklab, var(--color-surface-300) 50%, transparent); border-right:none;"
          >.json / .pdf</span
        >
      </div>
      <p class="text-xs opacity-50 mt-1">
        Used as the filename when exporting: <code class="font-mono bg-surface-200-800 px-1 rounded"
          >cv-mycv.json</code
        >
      </p>
    </label>
  </fieldset>
</form>

<style>
  @import './form-shared.css';
</style>
