<script>
	import { postAuth } from '$lib/net';
	import { mydegrees, mypublications, profile, signup } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import DegreeForm from './DegreeForm.svelte';
	import PublicationForm from './PublicationForm.svelte';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { handleFinish } from './common';
	import { page } from '$app/stores';
	$: console.log($mypublications);

	onMount(() => {
		if ($profile.degrees && $profile.degrees.length > 0) {
			const newDegrees = [];
			$profile.publications.forEach((pub) => {
				const d = {
					id: newDegrees.length + 1,
					dbid: pub.id,
					name: pub.name,
					url: pub.url
				};
				newDegrees.push(d);
			});
			mypublications.set(newDegrees);
		}
	});

	function handleSubmit() {
		postAuth('profile/publication/', $mypublications)
			.then((res) => {
				if (res.code == 200) {
					console.log(res);
					profile.set(res?.data.profile);
					toastStore.trigger({
						message: 'Profile Updated'
					});
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

<div class="text-end">
	<button
		on:click={() => {
			mypublications.add();
		}}
		class="btn variant-filled-primary"
	>
		Add Publication
	</button>
</div>

{#each $mypublications as publication}
	<PublicationForm {publication} />
{/each}
<div class="flex justify-end my-4 space-x-4">
	<button on:click={handleSubmit} class="btn variant-filled-primary">Save</button>
	{#if $page.url.pathname == '/profile/complete'}
		<button
			on:click={() => {
				signup.set('research');
			}}
			class="btn variant-filled-primary">Back</button
		>
		<button on:click={handleFinish} class="btn variant-filled-primary">Finish</button>
	{/if}
</div>
