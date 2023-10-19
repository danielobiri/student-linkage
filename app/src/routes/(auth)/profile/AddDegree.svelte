<script>
	import { postAuth } from '$lib/net';
	import { mydegrees, profile, signup } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import DegreeForm from './DegreeForm.svelte';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	$: console.log($mydegrees);

	onMount(() => {
		if ($profile.degrees && $profile.degrees.length > 0) {
			const newDegrees = [];
			$profile.degrees.forEach((degree) => {
				const d = {
					id: newDegrees.length + 1,
					dbid: degree.id,
					name: degree.name,
					university: degree.university,
					status: degree.status,
					obtained_gpa: degree.obtained_gpa,
					total_gpa: degree.total_gpa,
					courses: degree.courses
				};
				newDegrees.push(d);
			});
			mydegrees.set(newDegrees);
		}
	});

	function handleSubmit() {
		postAuth('profile/degree/', $mydegrees)
			.then((res) => {
				if (res.code == 200) {
					console.log(res);
					profile.set(res?.data.profile);
					toastStore.trigger({
						message: 'Profile Updated'
					});
					if ($page.url.pathname == '/profile/complete') {
						signup.set('research');
					} else {
						console.log('not complete');
					}
				} else {
					console.log(res);
					toastStore.trigger({
						message: 'Something went wrong',
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
			mydegrees.add();
		}}
		class="btn variant-filled-primary"
	>
		Add Degree
	</button>
</div>

{#each $mydegrees as degree}
	<DegreeForm {degree} />
{/each}
<div class="text-end mt-4">
	{#if $page.url.pathname == '/profile/complete'}
		<button
			on:click={() => {
				signup.set('university');
			}}
			class="btn variant-filled-primary">Back</button
		>
	{/if}

	<button on:click={handleSubmit} class="btn variant-filled-primary">Save</button>
</div>
