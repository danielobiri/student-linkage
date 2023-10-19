<script>
	// import { questions } from '$lib/stores';
	import { onMount } from 'svelte';
	import Qs from './Qs.svelte';
	import { postReq } from '$lib/net';
	import { page } from '$app/stores';
	import { answers, question } from './store';
	export let topic;

	let questions;
</script>

<div class="shadow-md mt-6">
	{#each $answers as q}
		<Qs {q} />
	{/each}
</div>
