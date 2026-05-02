<script lang="ts">
    import { cvState } from '$lib/state/cvState.svelte';
</script>

<div class="space-y-4">
    <h3 class="h3 font-bold">Personal Information</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <label class="label">
            <span>Name</span>
            <input class="input" type="text" bind:value={cvState.personal_info.name} placeholder="John" />
        </label>
        <label class="label">
            <span>Surname</span>
            <input class="input" type="text" bind:value={cvState.personal_info.surname} placeholder="Doe" />
        </label>
        <label class="label">
            <span>Email</span>
            <input class="input" type="email" bind:value={cvState.personal_info.email} placeholder="john@example.com" />
        </label>
        <label class="label">
            <span>Phone</span>
            <input class="input" type="tel" bind:value={cvState.personal_info.phone} placeholder="+1 234 567 890" />
        </label>
        <label class="label">
            <span>Address</span>
            <input class="input" type="text" bind:value={cvState.personal_info.address} placeholder="123 Main St, City, Country" />
        </label>
        <label class="label">
            <span>Birthday</span>
            <input class="input" type="date" bind:value={cvState.personal_info.birthday} />
        </label>
        <label class="label">
            <span>Gender</span>
            <select class="select" bind:value={cvState.personal_info.gender}>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
                <option value="Prefer not to say">Prefer not to say</option>
            </select>
        </label>
        <label class="label">
            <span>Nationality</span>
            <input class="input" type="text" bind:value={cvState.personal_info.nationality} placeholder="Italian" />
        </label>
        <label class="label">
            <span>Tax Code</span>
            <input class="input" type="text" bind:value={cvState.personal_info.tax_code} placeholder="..." />
        </label>
        <label class="label">
            <span>GitHub Profile URL</span>
            <input class="input" type="url" bind:value={cvState.personal_info.github} placeholder="https://github.com/..." />
        </label>
        <label class="label">
            <span>LinkedIn Profile URL</span>
            <input class="input" type="url" bind:value={cvState.personal_info.linkedin} placeholder="https://linkedin.com/in/..." />
        </label>
        <label class="label">
            <span>Picture URL</span>
            <input class="input" type="url" bind:value={cvState.personal_info.url_pic} placeholder="https://example.com/pic.jpg" />
        </label>
    </div>
</div>
