<script lang="ts">
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-gold-nouveau.css';
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/skeleton.css';
	import { AppShell, toastStore } from '@skeletonlabs/skeleton';
	// Most of your app wide CSS should be put in this file
	import '../../app.postcss';
	import { Toast } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import NavDash from '$lib/components/NavDash.svelte';
	import { profile } from '$lib/stores';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';

	import { storePopup } from '@skeletonlabs/skeleton';
	import Footer from '$lib/components/Footer.svelte';
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });

	onMount(() => {});

	// $: {
	// 	console.log($user, 'user');
	// 	if ($user) {
	// 		if ($user.is_complete == false) {
	// 			console.log('user is not complete');
	// 			toastStore.trigger({
	// 				message: 'Please complete your profile to continue'
	// 			});
	// 			goto('/profile');
	// 		}
	// 	}
	// }
</script>

<Toast />
<!-- <slot /> -->
<AppShell>
	<svelte:fragment slot="header">
		<NavDash />
	</svelte:fragment>
	<!-- (sidebarLeft) -->
	<!-- (sidebarRight) -->
	<!-- Router Slot -->
	<div class="mx-auto mt-24 max-w-7xl p-8">
		<slot />
	</div>
	<!-- ---- / ---- -->
	<!-- (pageFooter) -->
	<!-- (footer) -->
	<Footer />
</AppShell>

<style>
	:global(.themed) {
		--border: 1px solid #744aa1;
		--border-focused: 1px solid #744aa1;
		--border-hover: 1px solid #744aa1;
		--chevron-background: #744aa1;
		--clear-select-color: #744aa1;
		--item-hover-color: #744aa1;
		--item-hover-bg: #f2eef7;
		--input-color: #744aa1;
		--item-is-active-bg: #744aa1;
		--list-background: #faf8fc;
		--multi-item-bg: #faf8fc;
		--multi-item-clear-icon-color: #744aa1;
		--multi-item-color: #744aa1;
		--value-container-padding: 0.5rem 0.75;

		--border-radius: 4px;
		--placeholder-color: #744aa1;
		--background: #e5dcef;
	}
</style>
