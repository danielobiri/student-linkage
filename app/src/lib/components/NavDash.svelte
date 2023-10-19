<script lang="ts">
	import { goto } from '$app/navigation';
	import { menu } from '$lib/menu';
	import { basemedia } from '$lib/net';
	import { access, profile, refresh } from '$lib/stores';
	import { Avatar, popup, toastStore, type PopupSettings } from '@skeletonlabs/skeleton';

	let is_mobile_menu_closed = true;

	const popupClick: PopupSettings = {
		event: 'click',
		target: 'popupClick',
		placement: 'top'
	};
	const logout = async () => {
		access.set(null);
		refresh.set(null);
		profile.set(null);
		toastStore.trigger({
			message: 'Logged out successfully'
		});
		goto('/login');
	};
</script>

<header class="absolute inset-x-0 top-0 z-50 shadow-sm bg-white">
	<nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
		<div class="flex lg:flex-1 space-x-10">
			<a href="#" class="-m-1.5 p-1.5">
				<span class="sr-only">Your Company</span>
				<img
					class="h-8 w-auto"
					src="https://tailwindui.com/img/logos/mark.svg?color=primary&shade=600"
					alt=""
				/>
			</a>
			<div>
				<div class="mt-2 flex rounded-md shadow-sm">
					<div class="relative flex flex-grow items-stretch focus-within:z-10">
						<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
							<svg
								class="h-5 w-5 text-gray-400"
								viewBox="0 0 20 20"
								fill="currentColor"
								aria-hidden="true"
							>
								<path
									d="M7 8a3 3 0 100-6 3 3 0 000 6zM14.5 9a2.5 2.5 0 100-5 2.5 2.5 0 000 5zM1.615 16.428a1.224 1.224 0 01-.569-1.175 6.002 6.002 0 0111.908 0c.058.467-.172.92-.57 1.174A9.953 9.953 0 017 18a9.953 9.953 0 01-5.385-1.572zM14.5 16h-.106c.07-.297.088-.611.048-.933a7.47 7.47 0 00-1.588-3.755 4.502 4.502 0 015.874 2.636.818.818 0 01-.36.98A7.465 7.465 0 0114.5 16z"
								/>
							</svg>
						</div>
						<input
							type="email"
							name="email"
							id="email"
							class="block w-full rounded-none rounded-l-md border-0 py-1.5 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
							placeholder="Search..."
						/>
					</div>
					<button
						type="button"
						class="relative -ml-px inline-flex items-center gap-x-1.5 rounded-r-md px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
					>
						<!--  -->

						<svg
							class="-ml-0.5 h-5 w-5 text-gray-400"
							viewBox="0 0 24 24"
							xmlns="http://www.w3.org/2000/svg"
						>
							<path
								fill="currentColor"
								d="m19.6 21l-6.3-6.3q-.75.6-1.725.95T9.5 16q-2.725 0-4.612-1.888T3 9.5q0-2.725 1.888-4.612T9.5 3q2.725 0 4.612 1.888T16 9.5q0 1.1-.35 2.075T14.7 13.3l6.3 6.3l-1.4 1.4ZM9.5 14q1.875 0 3.188-1.313T14 9.5q0-1.875-1.313-3.188T9.5 5Q7.625 5 6.312 6.313T5 9.5q0 1.875 1.313 3.188T9.5 14Z"
							/>
						</svg>
						Search
					</button>
				</div>
			</div>
		</div>
		<div class="flex lg:hidden">
			<button
				type="button"
				on:click={() => (is_mobile_menu_closed = !is_mobile_menu_closed)}
				class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
			>
				<span class="sr-only">Open main menu</span>
				<svg
					class="h-6 w-6"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					aria-hidden="true"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
					/>
				</svg>
			</button>
		</div>
		<div class="hidden lg:flex lg:gap-x-12">
			{#if $profile?.is_complete}
				{#each menu.dashboard as item}
					<a href={item.url} class="text-sm font-semibold leading-6 text-gray-900">{item.name}</a>
				{/each}
			{:else}
				<a href="/profile" class="text-sm font-semibold leading-6 text-gray-900">Profile</a>
			{/if}
		</div>
		<div class="hidden lg:flex lg:flex-1 lg:justify-end">
			<button class="btn" use:popup={popupClick}>
				{#if $profile?.image}
					<Avatar src={basemedia + $profile.image} width="w-12" rounded="rounded-full" />
				{:else}
					<Avatar width="w-12" rounded="rounded-full" />
				{/if}
			</button>

			<div class="card p-4" data-popup="popupClick">
				<nav class="list-nav">
					<!-- (optionally you can provide a label here) -->
					<ul>
						<li>
							<a href="/profile/my">
								<span class="flex-auto">Profile</span>
							</a>
						</li>
						<li>
							<button on:click={logout}>
								<span class="flex-auto">Logout</span>
							</button>
						</li>
						<!-- ... -->
					</ul>
				</nav>
			</div>
		</div>
	</nav>
	<!-- Mobile menu, show/hide based on menu open state. -->
	<div class="lg:hidden" class:hidden={is_mobile_menu_closed} role="dialog" aria-modal="true">
		<!-- Background backdrop, show/hide based on slide-over state. -->
		<div class="fixed inset-0 z-50" />
		<div
			class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10"
		>
			<div class="flex items-center justify-between">
				<a href="#" class="-m-1.5 p-1.5">
					<span class="sr-only">Your Company</span>
					<img
						class="h-8 w-auto"
						src="https://tailwindui.com/img/logos/mark.svg?color=primary&shade=600"
						alt=""
					/>
				</a>
				<button
					on:click={() => (is_mobile_menu_closed = !is_mobile_menu_closed)}
					type="button"
					class="-m-2.5 rounded-md p-2.5 text-gray-700"
				>
					<span class="sr-only">Close menu</span>
					<svg
						class="h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						aria-hidden="true"
					>
						<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</button>
			</div>
			<div class="mt-6 flow-root">
				<div class="-my-6 divide-y divide-gray-500/10">
					<div class="space-y-2 py-6">
						{#each menu.dashboard as item}
							<a
								href={item.url}
								class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
								>{item.name}</a
							>
						{/each}
					</div>
					<div class="py-6">
						<a
							href="/login"
							class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
							>Log out</a
						>
					</div>
				</div>
			</div>
		</div>
	</div>
</header>
