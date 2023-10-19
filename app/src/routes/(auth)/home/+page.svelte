<script>
	import { goto } from '$app/navigation';
	import Experience from '$lib/components/Experience.svelte';
	import Images from '$lib/components/Images.svelte';
	import NavDash from '$lib/components/NavDash.svelte';
	import Postings from '$lib/components/Postings.svelte';
	import { getUser } from '$lib/net';
	import { profile } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';

	// $: {
	// 	if (!$profile) {
	// 		getUser();
	// 	} else {
	// 		if ($profile?.is_complete) {
	// 			toastStore.trigger({
	// 				message: 'Welcome Home'
	// 			});
	// 		} else {
	// 			goto('/profile');
	// 			toastStore.trigger({
	// 				message: 'Complete your profile first'
	// 			});
	// 		}
	// 	}
	// }
</script>

{#if $profile?.is_complete}
	<div class="mx-auto max-w-7xl px-6 pb-32 lg:px-8">
		<div class="mx-auto max-w-2xl gap-x-14 lg:mx-0 lg:flex lg:max-w-none lg:items-center">
			<div class="w-full max-w-xl lg:shrink-0 xl:max-w-2xl">
				<h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
					Partner for your future of learning, research and educational connections
				</h1>
				<p class="relative mt-6 text-lg leading-8 text-gray-600 sm:max-w-md lg:max-w-none">
					Welcome to this user-friendly platform that helps students connect to professors and
					professors find qualified students for their research needs.
				</p>
				<div class="mt-10 flex items-center gap-x-6">
					{#if $profile.role == 'professor'}
						<div class="flex justify-end">
							<a href="/jobs/create" class="btn variant-filled-primary"> Create Posting </a>
						</div>
					{:else}
						<Postings />
					{/if}
				</div>
			</div>
			<div class=" flex justify-end gap-8 sm:-mt-44 sm:justify-start sm:pl-20 lg:mt-0 lg:pl-0">
				<div class="mx-auto w-96 flex-none hidden md:flex xl:order-none">
					<Images />
				</div>
			</div>
		</div>
		<div class="mx-auto max-w-2xl gap-x-14 lg:mx-0 lg:flex lg:max-w-none lg:items-center">
			<div class="w-full max-w-xl lg:shrink-0 xl:max-w-2xl">
				<Experience />
			</div>
			<div class=" flex justify-end gap-8 sm:-mt-44 sm:justify-start sm:pl-20 lg:mt-0 lg:pl-0">
				<div class="mx-auto w-96 flex-none hidden md:flex xl:order-none">New Fedd here</div>
			</div>
		</div>
	</div>
{:else}
	Complete your profile first
{/if}
