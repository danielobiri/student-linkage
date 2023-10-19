<script>
	import { onMount } from 'svelte';
	import Feed from './Feed.svelte';
	import UserInput from './UserInput.svelte';
	import { answers, question } from './store';
	import { page } from '$app/stores';
	import { postReq } from '$lib/net';
	onMount(() => {
		postReq(`community/q/${$page.params.id}/`, {}).then((res) => {
			if (res?.code == 200) {
				answers.set(res?.data.answers);
				question.set(res.data.question);
			}
		});
	});

	$: {
		console.log($answers);
	}
</script>

<div class="card card-hover shadow-md m-2">
	<div class="card-header text-2xl">
		<span class="capitalize">
			{$question?.title}
		</span>
		<div class="text-sm text-gray-500">
			Made by
			{$question?.username}
			<span>
				{new Date($question?.created_at).toLocaleDateString()}
			</span>
		</div>
	</div>
	<div class="p-4">
		{$question?.message}
	</div>
</div>

<UserInput />

<Feed />
