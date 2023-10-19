<script lang="ts">
	import { createForm } from '$lib/formvalidator';
	import { postAuth, postReq } from '$lib/net';

	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	let role = 'student';
	onMount(() => {});
	const form = createForm({
		email: {
			required: true,
			email: true
		},
		password: {
			required: true,
			min: 8
		},
		f_name: {
			required: true
		},
		l_name: {
			required: true
		},
		password2: {
			required: true,
			min: 8,
			equalTo: 'password'
		},
		role: {
			default: $page.url.searchParams.get('role') || 'student',
			required: true
		}
	});

	$: {
		form.validate();
	}

	let loading = false;
	async function handleSubmit() {
		loading = true;
		form.validate();

		const isValid = form['isValid'];
		console.log(isValid, 'is valid');
		if (!isValid) {
			loading = false;
			return;
		}

		const res = await postReq('signup/', form);
		if (res.code == 201) {
			loading = false;
			toastStore.trigger({
				message: res?.data.msg
			});
			goto('/login');
		} else {
			console.log(res, 'res');
			loading = false;
			toastStore.trigger({
				message: res?.data.msg
			});
		}
	}
</script>

<div class="flex min-h-full bg-white">
	<div
		class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24"
	>
		<div class="mx-auto w-full max-w-sm lg:w-96">
			<div>
				<a class="w-fit block" href="/">
					<img
						class="h-10 w-auto"
						src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
						alt="Your Company"
					/>
				</a>

				<h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign up</h2>
			</div>

			<div class="mt-10">
				<div>
					<form on:submit|preventDefault={handleSubmit} class="space-y-6">
						<div>
							<label for="email" class="block text-sm font-medium leading-6 text-gray-900"
								>Email {#if form.role == 'professor'}
									<span>(university email only)</span>
								{/if}</label
							>
							<div class="mt-2">
								<input
									id="email"
									name="email"
									type="text"
									bind:value={form.email}
									required
									class="input"
								/>
							</div>
						</div>
						{#each form.errors.email as err}
							<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
								{err}
							</p>
						{/each}
						<div>
							<label for="email" class="block text-sm font-medium leading-6 text-gray-900"
								>First Name</label
							>
							<div class="mt-2">
								<input
									id="email"
									name="email"
									type="text"
									bind:value={form.f_name}
									required
									class="input"
								/>
							</div>
						</div>
						{#each form.errors.f_name as err}
							<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
								{err}
							</p>
						{/each}

						<div>
							<label for="email" class="block text-sm font-medium leading-6 text-gray-900"
								>Last Name</label
							>
							<div class="mt-2">
								<input
									id="email"
									name="email"
									type="text"
									bind:value={form.l_name}
									required
									class="input"
								/>
							</div>
						</div>
						{#each form.errors.l_name as err}
							<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
								{err}
							</p>
						{/each}

						<div>
							<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
								>Password</label
							>
							<div class="mt-2">
								<input
									id="password"
									name="password"
									type="password"
									bind:value={form.password}
									required
									class="input"
								/>
							</div>
						</div>
						{#each form.errors.password as err}
							<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
								{err}
							</p>
						{/each}

						<div>
							<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
								>Retype Password</label
							>
							<div class="mt-2">
								<input
									id="password"
									name="password"
									type="password"
									bind:value={form.password2}
									required
									class="input"
								/>
							</div>
						</div>
						{#each form.errors.password2 as err}
							<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
								{err}
							</p>
						{/each}

						<div>
							<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
								>Role</label
							>
							<div class="mt-2">
								<select bind:value={form.role} class="input">
									<option value="student">I am Student</option>
									<option value="professor">I am Professor</option>
								</select>
							</div>
						</div>

						<div>
							<button
								type="submit"
								disabled={loading}
								class="flex w-full justify-center rounded-md bg-primary-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500"
							>
								{loading ? 'Signing Up' : 'Sign up'}
							</button>
						</div>

						<div>
							<a href="/login" class="text-sm text-primary-500 hover:text-primary-500"
								>Already have an account? Login</a
							>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
	<div class="relative hidden w-0 flex-1 lg:block">
		<img class="absolute inset-0 h-full center w-full object-cover" src="/login.webp" alt="" />
	</div>
</div>
