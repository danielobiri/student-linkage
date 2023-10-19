<script>
	import { questions } from '$lib/stores';
	import { onMount } from 'svelte';
	import Qs from './Qs.svelte';
	import { postReq } from '$lib/net';
	export let topic;

	onMount(() => {
		postReq('community/get/', { topic: topic }).then((res) => {
			if (res?.code == 200) {
				questions.set(res?.data.questions);
			}
		});
	});

	$: {
		console.log($questions);
	}
</script>

<div class="shadow-md mt-6">
	{#each $questions as q}
		<Qs {topic} {q} />
	{/each}
</div>
