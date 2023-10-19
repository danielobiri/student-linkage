<script>
	import { basemedia, getUser } from '$lib/net';
	import { profile } from '$lib/stores';
	import { Avatar } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';

	$: console.log($profile, 'profile');
	onMount(async () => {
		await getUser();
	});
</script>

{#if $profile.role == 'professor'}
	<div class="max-w-6xl p-6 mx-auto card shadow-lg">
		<div class="flex justify-between my-8">
			<div>
				<h1 class="text-3xl">Profile</h1>
			</div>
			<a href="/profile/edit" class="btn variant-filled"> Edit Profile </a>
		</div>
		<div class="flex justify-center items-end bg-cover">
			<!-- style="background-image: url('/bg.jpeg'); height: 400px" -->

			<div>
				{#if $profile.image}
					<Avatar src={basemedia + $profile.image} width="w-44" rounded="rounded-full" />
				{:else}
					<Avatar width="w-32" rounded="rounded-full" />
				{/if}
			</div>
		</div>
		<div>
			<div class="text-xl font-semibold text-center justify-center capitalize">
				{$profile.user.f_name}
				{$profile.user.l_name}
			</div>
		</div>

		<div class="grid grid-cols-6 mt-4">
			<div class=" col-span-3 p-4 card">
				<div class="  text-lg font-semibold">Research Synopsis</div>
				<div>
					{$profile.research_background}
				</div>
			</div>
			<div class="card col-span-3 p-4">
				<div class="  text-lg font-semibold mb-2">Educational Background</div>
				{#each $profile.degrees as deg}
					<div
						class="mt-1 flex p-4 justify-between card shadow-sm my-4 gap-x-6 sm:mt-0 sm:flex-auto"
					>
						<div class="grid">
							<div class="text-base font-semibold uppercase">
								{deg.name}
							</div>
							<div class="text-sm">
								{deg.status}
							</div>
						</div>
						<div>
							<div class="text-base font-semibold uppercase">University</div>
							<div class="text-sm capitalize">
								{deg.university}
							</div>
						</div>
						<div>
							<div class="text-base font-semibold uppercase">GPA</div>
							<div class="text-sm">
								{deg.obtained_gpa} / {deg.total_gpa}
							</div>
						</div>
					</div>
				{/each}
				<div class="  text-lg font-semibold mb-2">Degree Seeking</div>
				<div class="text-gray-900 uppercase">{$profile.degree_seeking}</div>
			</div>
		</div>

		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Research Interests</div>
			{#each $profile.research_areas as area}
				<span class="chip variant-filled-primary m-2">{area.label}</span>
			{/each}
		</div>
		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Publications</div>
			{#each $profile.publications as pub, index}
				{index + 1}.
				<a target="_blank" class="btn underline capitalize" href={pub.url}>{pub.name}</a>
			{/each}
		</div>
		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Google Scholar Page</div>
			<a class="underline" href={$profile.google_scholar_page}>
				{$profile.google_scholar_page}
			</a>
		</div>
	</div>
{:else}
	<div class="max-w-6xl p-6 mx-auto card shadow-lg">
		<div class="flex justify-between my-8">
			<div>
				<h1 class="text-3xl">Profile</h1>
			</div>
			<a href="/profile/edit" class="btn variant-filled"> Edit Profile </a>
		</div>
		<div class="flex justify-center items-end bg-cover">
			<!-- style="background-image: url('/bg.jpeg'); height: 400px" -->

			<div>
				{#if $profile.image}
					<Avatar src={basemedia + $profile.image} width="w-44" rounded="rounded-full" />
				{:else}
					<Avatar width="w-32" rounded="rounded-full" />
				{/if}
			</div>
		</div>
		<div>
			<div class="text-xl font-semibold text-center justify-center capitalize">
				{$profile.user.f_name}
				{$profile.user.l_name}
			</div>
		</div>

		<div class="grid grid-cols-6 mt-4">
			<div class=" col-span-3 p-4 card">
				<div class="  text-lg font-semibold">Research Synopsis</div>
				<div>
					{$profile.research_background}
				</div>
			</div>
			<div class="card col-span-3 p-4">
				<div class="  text-lg font-semibold mb-2">Educational Background</div>
				{#each $profile.degrees as deg}
					<div
						class="mt-1 flex p-4 justify-between card shadow-sm my-4 gap-x-6 sm:mt-0 sm:flex-auto"
					>
						<div class="grid">
							<div class="text-base font-semibold uppercase">
								{deg.name}
							</div>
							<div class="text-sm">
								{deg.status}
							</div>
						</div>
						<div>
							<div class="text-base font-semibold uppercase">University</div>
							<div class="text-sm capitalize">
								{deg.university}
							</div>
						</div>
						<div>
							<div class="text-base font-semibold uppercase">GPA</div>
							<div class="text-sm">
								{deg.obtained_gpa} / {deg.total_gpa}
							</div>
						</div>
					</div>
				{/each}
				<div class="  text-lg font-semibold mb-2">Degree Seeking</div>
				<div class="text-gray-900 uppercase">{$profile.degree_seeking}</div>
			</div>
		</div>

		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Research Interests</div>
			{#each $profile.research_areas as area}
				<span class="chip variant-filled-primary m-2">{area.label}</span>
			{/each}
		</div>
		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Publications</div>
			{#each $profile.publications as pub, index}
				{index + 1}.
				<a target="_blank" class="btn underline capitalize" href={pub.url}>{pub.name}</a>
			{/each}
		</div>
		<div class="card p-4">
			<div class="  text-lg font-semibold mb-2">Google Scholar Page</div>
			<a class="underline" href={$profile.google_scholar_page}>
				{$profile.google_scholar_page}
			</a>
		</div>
	</div>
{/if}
