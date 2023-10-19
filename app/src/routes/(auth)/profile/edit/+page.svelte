<script>
	import { Avatar } from '@skeletonlabs/skeleton';
	import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
	let tabSet = 0;
	import { FileButton } from '@skeletonlabs/skeleton';
	import AddDegree from '../AddDegree.svelte';
	import { degree_levels } from '../options';
	import Research from '../Research.svelte';
	import AddPublication from '../AddPublication.svelte';
	import BasicForm from '../BasicForm.svelte';
	import { onMount } from 'svelte';
	import { profile, signup } from '$lib/stores';
	import { getUser } from '$lib/net';
	import UniversityForm from '../UniversityForm.svelte';
	onMount(async () => {
		await getUser();
	});
</script>

<BasicForm />
<UniversityForm />
<div class="card bg-transparent shadow-lg p-4 mb-4">
	<h3 class="h3 my-4">Degree</h3>
	<AddDegree />
</div>
<Research />
<div class="card bg-transparent shadow-lg p-4 mb-4">
	<h3 class="h3 my-4">Publications</h3>
	<AddPublication />
</div>
