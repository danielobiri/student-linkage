<script lang="ts">
	import { Avatar, toastStore } from '@skeletonlabs/skeleton';
	import { degree_levels } from './options';
	import { createForm } from '$lib/formvalidator';
	import { profile, signup } from '$lib/stores';
	import { countries } from '$lib/countries';
	import { FileButton } from '@skeletonlabs/skeleton';
	import { basemedia, getUser, postAuth, postAuthUploadFile } from '$lib/net';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	let files: FileList;

	$: console.log($profile);

	const form = createForm({
		name: {
			required: true,
			default: $profile?.university?.name
		},
		email: {
			required: false,
			email: true,
			default: $profile?.university?.email
		},
		is_verified: {
			required: false,
			default: $profile?.university?.is_verified ? true : false
		},
		verification_method: {
			required: true,
			default: $profile?.university?.verification_method
				? $profile?.university?.verification_method
				: 'email'
		}
	});
	let src = '';

	function onChangeHandler(e: Event): void {
		console.log(files);
		const file = files[0];
		const reader = new FileReader();
		reader.onload = (e) => {
			src = e.target.result as string;
		};
		reader.readAsDataURL(file);
	}

	$: {
		form.validate();
	}

	function handleSubmit() {
		const data = form.toFormData();

		if (form.verification_method == 'id') {
			if (!$profile?.university?.student_id) {
				if (!files) {
					toastStore.trigger({
						message: 'Please upload a file'
					});
					return;
				} else if (files.length == 0) {
					toastStore.trigger({
						message: 'Please upload a file'
					});
					return;
				} else {
					data.append('id', files[0]);
				}
			}
		}

		if (form.verification_method == 'email') {
			if (!form.email) {
				toastStore.trigger({
					message: 'Please enter an email'
				});
				return;
			}
		}

		// 	if()
		// }

		postAuthUploadFile('profile/university/', data)
			.then((res) => {
				if (res.code == 200) {
					console.log(res);
					profile.set(res?.data.profile);
					toastStore.trigger({
						message: 'Profile Updated'
					});
					if ($page.url.pathname == '/profile/complete') {
						signup.set('degree');
					} else {
						console.log('not complete');
					}
					files = null;
				} else {
					console.log(res);
					toastStore.trigger({
						message: res?.data.msg
					});
				}
			})
			.catch((err) => {
				console.log(err);
			});
	}
</script>

<div class="card bg-transparent shadow-lg p-4 mb-4">
	<h3 class="h3 my-4">University</h3>
	<div class="grid grid-cols-6 gap-4">
		<label class="label col-span-6 sm:col-span-3">
			<span>University Name</span>
			<input
				disabled={form.is_verified}
				bind:value={form.name}
				class="input"
				type="text"
				placeholder="Harvard"
			/>
			{#if form.errors.name}
				<p class="text-red-500 text-xs italic">{form.errors.name}</p>
			{/if}
		</label>

		<label class="label col-span-6 sm:col-span-3">
			<span>Verification Method</span>
			<select disabled={form.is_verified} bind:value={form.verification_method} class="select">
				<option value="email">Email</option>
				<option value="id">University ID</option>
			</select>
			{#if form.errors.verification_method}
				<p class="text-red-500 text-xs italic">{form.errors.verification_method}</p>
			{/if}
		</label>
		{#if form.verification_method == 'email'}
			<label class="label col-span-6 sm:col-span-3">
				<span>University Email</span>
				<input
					bind:value={form.email}
					disabled={form.is_verified}
					class="input"
					type="text"
					placeholder="user@harvard.edu"
				/>
				{#if form.errors.email}
					<p class="text-red-500 text-xs italic">{form.errors.email}</p>
				{/if}
			</label>

			<!-- <div class="col-span-6 sm:col-span-3">
				<button class="btn variant-soft-primary"> Verify Email </button>
			</div> -->
		{/if}
		{#if form.verification_method == 'id'}
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label class="label col-span-6 sm:col-span-3">
				<span>University ID</span>
				<FileButton name="files" bind:files button="variant-soft-primary"
					>Upload Student ID</FileButton
				>
				{#if $profile.university.student_id}
					<a
						class="btn btn-sm"
						href={basemedia + $profile.university?.student_id}
						target="_blank"
						download={true}
					>
						Download Student ID
					</a>
				{/if}

				{#if files}
					{#if files.length > 0}
						{files[0].name}
					{/if}
				{/if}
			</label>
		{/if}
		<label class="label col-span-6 sm:col-span-3">
			<span>Verification Status</span>
			<select class="select" disabled>
				{#if form.is_verified}
					<option selected={$profile.univeristy?.is_verified} value="complete">Verified</option>
				{:else}
					<option value="incomplete">Not Verified</option>
				{/if}
			</select>
		</label>

		<!-- svelte-ignore a11y-label-has-associated-control -->
	</div>
	<div class="flex justify-end my-2 space-x-4">
		{#if $page.url.pathname == '/profile/complete'}
			<button
				on:click={() => {
					signup.set('basic');
				}}
				class="btn variant-filled-primary">Back</button
			>
		{/if}

		<button
			on:click={handleSubmit}
			disabled={form.is_verified}
			class="btn btn-base variant-filled-primary">Save</button
		>
	</div>
</div>
