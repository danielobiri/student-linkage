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

	onMount(() => {
		console.log('mounted');
		if (!$profile) {
			getUser();
		}
	});
	let form;
	if ($profile?.role == 'student') {
		form = createForm({
			email: {
				required: true,
				email: true,
				default: $profile?.user?.email
			},
			f_name: {
				required: true,
				default: $profile?.user?.f_name
			},
			l_name: {
				required: true,
				default: $profile?.user?.l_name
			},
			country: {
				required: true,
				default: $profile?.country
			},
			payment_plan: {
				required: false,
				default: 'free'
			},
			profile_status: {
				required: false
			},
			degree_seeking: {
				required: true,
				default: $profile?.degree_seeking
			}
		});
	} else {
		console.log('professor');
		form = createForm({
			email: {
				required: true,
				email: true,
				default: $profile?.user?.email
			},
			title: {
				required: true,
				default: $profile?.title
			},
			f_name: {
				required: true,
				default: $profile?.user?.f_name
			},
			l_name: {
				required: true,
				default: $profile?.user?.l_name
			},

			profile_status: {
				required: false
			},
			degree_seeking: {
				required: true,
				default: $profile?.interest_level
			}
		});
	}

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
		console.log('submit', form);
		form.validate();
		console.log('submit', form.errors);

		const isValid = form['isValid'];
		console.log(isValid, 'is Valid');
		if (!isValid) {
			return;
		}
		const values = form.values();
		console.log(values, 'values');
		const data = form.toFormData();
		if (files) {
			if (files.length > 0) {
				data.append('profile_pic', files[0]);
			}
		}

		postAuthUploadFile('profile/basic/', data)
			.then((res) => {
				if (res.code == 200) {
					console.log(res);
					profile.set(res?.data.profile);
					toastStore.trigger({
						message: 'Profile Updated'
					});
					if ($page.url.pathname == '/profile/complete') {
						if ($profile.role == 'student') {
							signup.set('university');
						} else {
							signup.set('research');
						}
					} else {
						console.log('not complete');
					}
				} else {
					console.log(res);
					toastStore.trigger({
						message: 'Something went wrong',
						background: 'bg-error-100'
					});
				}
			})
			.catch((err) => {
				console.log(err);
			});
	}
</script>

{#if form}
	<div class="card bg-transparent shadow-lg p-4 mb-4">
		<h3 class="h3">Basic</h3>

		<div class="flex justify-center flex-col items-center">
			{#if src}
				<Avatar {src} width="w-32" rounded="rounded-full" />
			{:else if $profile.image}
				<Avatar src={basemedia + $profile.image} width="w-32" rounded="rounded-full" />
			{:else}
				<Avatar initials="SL" width="w-32" rounded="rounded-full" />
			{/if}
			<div class="m-4">
				<FileButton
					name="files"
					on:change={onChangeHandler}
					accept="image/*"
					multiple={false}
					button="variant-soft-primary"
					bind:files>Upload</FileButton
				>
			</div>
		</div>

		<div class="grid grid-cols-6 gap-4">
			<label class="label col-span-6 sm:col-span-3">
				<span>Email</span>
				<input class="input" bind:value={form.email} disabled type="text" placeholder="Email" />
			</label>
			<label class="label col-span-6 sm:col-span-3">
				<span>First Name</span>
				<input class="input" type="text" bind:value={form.f_name} placeholder="John" />
				{#if form.errors.f_name}
					<p class="text-red-500 text-xs italic">{form.errors.f_name}</p>
				{/if}
			</label>
			<label class="label col-span-6 sm:col-span-3">
				<span>Last Name</span>
				<input class="input" bind:value={form.l_name} type="text" placeholder="Doe" />
				{#if form.errors.l_name}
					<p class="text-red-500 text-xs italic">{form.errors.l_name}</p>
				{/if}
			</label>
			{#if $profile.role == 'student'}
				<label class="label col-span-6 sm:col-span-3">
					<span>Country of Residence</span>
					<select bind:value={form.country} class="select">
						<option value="">Select Country</option>
						{#each countries as c}
							<option value={c.name}>{c.name}</option>
						{/each}
					</select>
					{#if form.errors.country}
						<p class="text-red-500 text-xs italic">{form.errors.country}</p>
					{/if}
				</label>
			{:else}
				<label class="label col-span-6 sm:col-span-3">
					<span>Title</span>
					<input class="input" bind:value={form.title} type="text" placeholder="Dr." />
					{#if form.errors.title}
						<p class="text-red-500 text-xs italic">{form.errors.title}</p>
					{/if}
				</label>
			{/if}

			<label class="label col-span-6 sm:col-span-3">
				<span>Profile Status</span>
				<select class="select" disabled>
					<option value="incomplete">Incomplete</option>
					<option value="complete">Complete</option>
				</select>
			</label>

			<!-- <label class="label col-span-6 sm:col-span-3">
				<span>Want to Supervise</span>
				<select class="select" disabled>
					<option value="incomplete">Incomplete</option>
					<option value="complete">Complete</option>
				</select>
			</label> -->

			<label class="label col-span-6 sm:col-span-3">
				{#if $profile.role == 'student'}
					<span>Level of Degree Seeking</span>
				{:else}
					<span>Level of Student Interested in to supervise</span>
				{/if}
				<select bind:value={form.degree_seeking} class="select">
					{#each degree_levels as level}
						<option value={level.value}>{level.label}</option>
					{/each}
				</select>
				{#if form.errors.degree_seeking}
					<p class="text-red-500 text-xs italic">{form.errors.degree_seeking}</p>
				{/if}
			</label>
		</div>
		<div class="flex justify-end my-2">
			<button on:click={handleSubmit} class="btn btn-base variant-filled-primary">Save</button>
		</div>
	</div>
{/if}
