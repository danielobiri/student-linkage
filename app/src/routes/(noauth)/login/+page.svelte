<script lang="ts">
	import { goto } from '$app/navigation';
	import { createForm } from '$lib/formvalidator';
	import { getUser, postAuth, postReq } from '$lib/net';
	import { access, refresh, profile, signup } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import { error } from '@sveltejs/kit';
	import { fade } from 'svelte/transition';

	const form = createForm({
		email: {
			required: true,
			email: true
		},
		password: {
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
		if (!isValid) {
			loading = false;
			return;
		}

		const res = await postReq('login/', form);

		if (res.code == 200) {
			toastStore.trigger({
				message: 'Logged in successfully!'
			});
			signup.set('basic');
			access.set(res?.data.access);
			refresh.set(res?.data.refresh);
			await getUser();
			if ($profile.is_complete == false) {
				toastStore.trigger({
					message: 'Complete your profile first'
				});
				goto('/profile/complete');
			} else {
				goto('/home');
			}
			loading = false;
		} else {
			toastStore.trigger({
				message: res?.data.msg
			});
			loading = false;
		}
	}
</script>

<div class="flex min-h-full bg-white">
	<div
		class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24"
	>
		<div class="mx-auto w-full max-w-sm lg:w-96">
			<div>
				<a href="/">
					<img
						class="h-10 w-auto"
						src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
						alt="Your Company"
					/>
				</a>

				<h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in</h2>
			</div>

			<div class="mt-10">
				<div>
					<form on:submit|preventDefault={handleSubmit} class="space-y-6">
						<div>
							<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
								>Email</label
							>
							<div class="mt-2">
								<input
									id="email"
									name="email"
									type="email"
									bind:value={form.email}
									required
									class="input"
								/>
							</div>
							<div>
								{#each form.errors.email as err}
									<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
										{err}
									</p>
								{/each}
							</div>

							<div>
								<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
									>Password</label
								>
								<div class="mt-2">
									<input
										id="password"
										name="password"
										type="password"
										autocomplete="current-password"
										bind:value={form.password}
										required
										class="input"
									/>
								</div>
							</div>
							<div>
								{#each form.errors.password as err}
									<p transition:fade class=" text-sm text-red-600 m-0 p-0" id="email-error">
										{err}
									</p>
								{/each}
							</div>
							<div class="flex my-4 items-center justify-between">
								<div class="flex items-center">
									<input
										id="remember-me"
										name="remember-me"
										type="checkbox"
										class="h-4 w-4 rounded border-gray-300 text-primary-500 focus:ring-primary-500"
									/>
									<label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-700"
										>Remember me</label
									>
								</div>

								<div class="text-sm leading-6">
									<a href="#" class="font-semibold text-primary-500 hover:text-primary-500"
										>Forgot password?</a
									>
								</div>
							</div>

							<div>
								<button
									type="submit"
									disabled={loading}
									class="flex w-full justify-center rounded-md my-2 bg-primary-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500"
								>
									{loading ? 'Loading...' : 'Sign in'}
								</button>
							</div>
							<div class="relative">
								<div class="absolute inset-0 flex items-center" aria-hidden="true">
									<div class="w-full border-t border-gray-200" />
								</div>
								<div class="relative flex justify-center text-sm font-medium leading-6">
									<span class="bg-white px-6 text-gray-900">Or</span>
								</div>
							</div>
							<div>
								<a
									href="/signup"
									type="button"
									class="flex w-full justify-center text-primary-500 rounded-md border-2 border-primary-500 px-3 py-1.5 text-sm font-semibold leading-6 hover:text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500"
									>Sign up</a
								>
							</div>
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
