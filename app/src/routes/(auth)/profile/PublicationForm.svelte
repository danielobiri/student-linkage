<script>
	import { postAuth } from '$lib/net';
	import { mydegrees, mypublications, profile } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import Trash from './Trash.svelte';
	export let publication;

	console.log(publication, 'publication');
</script>

<div class="flex justify-end">
	<button
		on:click={() => {
			mypublications.remove(publication);
		}}
		class="btn btn-icon"
	>
		<Trash />
	</button>
</div>

<div class="grid grid-cols-6 gap-4">
	<label class="label col-span-6 sm:col-span-3">
		<span>Publication Name</span>
		<input bind:value={publication.name} class="input" type="text" placeholder="Harvard" />
	</label>
	<label class="label col-span-6 sm:col-span-3">
		<span>URL</span>
		<input
			class="input"
			bind:value={publication.url}
			type="text"
			placeholder="https://domain.com"
		/>
	</label>

	<!-- svelte-ignore a11y-label-has-associated-control -->
</div>
