<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(() => {
		goto('/community/general');
		// console.log("hello");
	});
</script>
