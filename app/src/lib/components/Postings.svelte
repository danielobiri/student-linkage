<script>
	import { goto } from '$app/navigation';
	import { postAuth } from '$lib/net';
	import { onMount } from 'svelte';

	let jobs = [];

	onMount(() => {
		postAuth('job/list/').then((res) => {
			console.log(res);
			jobs = res?.data?.jobs;
		});
	});
</script>

<!-- Path: src/lib/components/Postings.svelte -->

<div class="h-60 p-2 overflow-y-scroll bg-gray-100">
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	{#each jobs as j}
		<div class="card w-96 my-2 card-hover shadow-sm">
			<div class="card-header text-xl font-semibold flex space-x-4">
				<div class="overflow-clip">
					{j.title}
				</div>
			</div>
			<div class="p-4 flex justify-between">
				<div class="uppercase text-sm">
					{j.education_level}
				</div>
				<div>
					<a href="/jobs/{j.id}" class="btn variant-filled btn-sm">See Detail</a>
				</div>
			</div>
		</div>
	{/each}
</div>
