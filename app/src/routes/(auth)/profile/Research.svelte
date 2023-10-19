<script>
	import Select from 'svelte-select';
	import AddPublication from './AddPublication.svelte';
	import { FileButton, toastStore } from '@skeletonlabs/skeleton';
	import { basemedia, postAuth, postAuthUploadFile } from '$lib/net';
	import { profile, signup } from '$lib/stores';
	import { createForm } from '$lib/formvalidator';
	import { page } from '$app/stores';
	import { handleFinish } from './common';

	let filterText = '';

	let value = null;

	let items = [];

	function handleFilter(e) {
		if (value?.find((i) => i.label === filterText)) return;
		if (e.detail.length === 0 && filterText.length > 0) {
			const prev = items.filter((i) => !i.created);
			if (items.length < 7) {
				items = [...prev, { value: filterText, label: filterText, created: true }];
			}
		}
	}

	function handleChange(e) {
		items = items.map((i) => {
			delete i.created;
			return i;
		});
	}
	let files;

	const form = createForm({
		google_scholar: {
			required: true,
			default: $profile.google_scholar_page
		},
		interests: {
			required: true,
			default: $profile.research_areas
		},
		research_background: {
			required: true,
			maxWords: 50,
			default: $profile.research_background
		}
	});

	$: {
		console.log(form);
		form.validate();
	}

	function handleSubmit() {
		form.validate();

		if (!form.isValid) {
			return;
		}
		const f = form.toFormData();
		if ($profile.role == 'student') {
			if (!$profile.resume) {
				if (!files) {
					toastStore.trigger({
						message: 'Please upload a resume',
						background: 'bg-error-100'
					});
					return;
				} else {
					if (files.length < 1) {
						toastStore.trigger({
							message: 'Please upload a resume',
							background: 'bg-error-100'
						});
						return;
					} else {
						f.append('resume', files[0]);
					}
				}
			}
		}

		postAuthUploadFile('profile/research/', f)
			.then((res) => {
				if (res.code == 200) {
					console.log(res);
					profile.set(res?.data.profile);
					files = null;
					toastStore.trigger({
						message: 'Profile Updated'
					});
					if ($page.url.pathname == '/profile/complete') {
						if ($profile.role == 'student') {
							signup.set('publication');
						}
					} else {
						console.log('not complete');
					}
				} else {
					console.log(res);
					toastStore.trigger({
						message: res?.data.msg,
						background: 'bg-error-100'
					});
				}
			})
			.catch((err) => {
				console.log(err);
			});
	}
</script>

<div class="card bg-transparent shadow-lg p-4 mb-4">
	<h3 class="h3 my-4">Research</h3>
	<div class="grid grid-cols-6 gap-4">
		<label class="label col-span-6 sm:col-span-3">
			<span>Google Scholar Page / Website</span>
			<input
				class="input"
				type="text"
				bind:value={form.google_scholar}
				placeholder="https://scholar.google.com/citations?hl=en&user=aU_oO1QAAAAJ
			"
			/>
			{#if form.errors.google_scholar}
				<p class="text-red-500 text-xs italic">{form.errors.google_scholar}</p>
			{/if}
		</label>

		<!-- svelte-ignore a11y-label-has-associated-control -->
		{#if $profile.role == 'student'}
			<label class="label col-span-6 sm:col-span-3">
				<span>Resume</span>
				<FileButton name="files" accept="application/pdf" bind:files button="variant-soft-primary"
					>Upload Resume</FileButton
				>
				{#if $profile.resume}
					<a
						class="btn btn-sm variant-form-material"
						href={basemedia + $profile.resume}
						target="_blank"
						download={true}
					>
						Download Resume
					</a>
				{/if}

				{#if files}
					{#if files.length > 0}
						{files[0].name}
					{/if}
				{/if}
			</label>
		{/if}
		<!-- svelte-ignore a11y-label-has-associated-control -->
		<label class="label col-span-6 sm:col-span-3">
			<span>Interests</span>
			<div class="themed">
				<Select
					on:change={handleChange}
					multiple
					on:filter={handleFilter}
					bind:filterText
					bind:value={form.interests}
					{items}
				>
					<div slot="item" let:item>
						{item.created ? 'Add new: ' : ''}
						{item.label}
					</div>
				</Select>
				{#if form.errors.interests}
					<p class="text-red-500 text-xs italic">{form.errors.interests}</p>
				{/if}
			</div>
			<div class="text-sm">Min 3, Max 7</div>
		</label>

		<label class="label col-span-6 sm:col-span-6">
			<span>Research Background (max 50 words) </span>
			<textarea
				class="textarea"
				bind:value={form.research_background}
				rows="4"
				placeholder="Your research synopsis here"
			/>
			<div class="text-sm">
				{form.research_backgroundData.wordCount < 51
					? 50 - form.research_backgroundData.wordCount + ' words left'
					: 'Max word limit reached'}
			</div>
			{#if form.errors.research_background}
				<p class="text-red-500 text-xs italic">{form.errors.research_background}</p>
			{/if}
			<div />
		</label>

		<!-- svelte-ignore a11y-label-has-associated-control -->

		<!-- svelte-ignore a11y-label-has-associated-control -->
	</div>

	<div class="text-end mt-4">
		{#if $page.url.pathname == '/profile/complete'}
			{#if $profile.role == 'professor'}
				<button on:click={handleFinish} class="btn variant-filled-primary">Finish</button>
			{/if}
			<button
				on:click={() => {
					signup.set('degree');
				}}
				class="btn variant-filled-primary">Back</button
			>
		{/if}
		<button on:click={handleSubmit} class="btn variant-filled-primary">Save</button>
	</div>
</div>
