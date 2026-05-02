<script lang="ts">
	import { cvStore } from '$lib/stores/cv.svelte';
</script>

<div class="space-y-4">
	<!-- Toggle -->
	<div class="card border border-surface-200-800 preset-filled-surface-100-900 p-4">
		<label class="flex cursor-pointer items-center gap-3">
			<input type="checkbox" class="checkbox" bind:checked={cvStore.data.letter.is_active} />
			<span class="font-medium">Include cover letter in CV output</span>
		</label>
		{#if !cvStore.data.letter.is_active}
			<p class="mt-2 ml-7 text-sm opacity-50">Enable to append a cover letter to the PDF output.</p>
		{/if}
	</div>

	{#if cvStore.data.letter.is_active}
		<!-- Recipient -->
		<div class="card border border-surface-200-800 preset-filled-surface-100-900 p-5">
			<fieldset class="space-y-4">
				<legend class="mb-3 text-xs font-bold tracking-widest uppercase opacity-50"
					>Recipient</legend
				>
				<div class="grid grid-cols-1 gap-4 md:grid-cols-3">
					<label class="label" for="letter-company">
						<span class="label-text">Company Name</span>
						<input
							id="letter-company"
							class="input"
							type="text"
							bind:value={cvStore.data.letter.company.name}
							placeholder="ACME Corp"
						/>
					</label>
					<label class="label" for="letter-address">
						<span class="label-text">Address</span>
						<input
							id="letter-address"
							class="input"
							type="text"
							bind:value={cvStore.data.letter.company.address}
							placeholder="Via Roma 1"
						/>
					</label>
					<label class="label" for="letter-city">
						<span class="label-text">City</span>
						<input
							id="letter-city"
							class="input"
							type="text"
							bind:value={cvStore.data.letter.company.city}
							placeholder="Milan, Italy"
						/>
					</label>
				</div>
			</fieldset>
		</div>

		<!-- Body -->
		<div class="card border border-surface-200-800 preset-filled-surface-100-900 p-5">
			<fieldset>
				<legend class="mb-3 text-xs font-bold tracking-widest uppercase opacity-50"
					>Letter Content</legend
				>
				<label class="label" for="letter-content">
					<span class="sr-only label-text">Letter body</span>
					<textarea
						id="letter-content"
						class="textarea rounded-container"
						rows="12"
						bind:value={cvStore.data.letter.content}
						placeholder="Dear Hiring Manager,&#10;&#10;I am writing to express my interest in..."
					></textarea>
				</label>
			</fieldset>
		</div>
	{/if}
</div>
