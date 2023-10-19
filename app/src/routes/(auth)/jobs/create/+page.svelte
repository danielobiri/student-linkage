<script>
	import { goto } from '$app/navigation';
	import { createForm } from '$lib/formvalidator';
	import { postAuth } from '$lib/net';
	import { toastStore } from '@skeletonlabs/skeleton';
	import { degree_levels } from '../../profile/options';
	const print = console.log;

	let form = createForm({
		title: {
			required: true
		},
		education_level: {
			required: true
		}
	});

	$: {
		form.validate();
	}

	async function onSubmit() {
		form.validate();
		const isValid = form['isValid'];
		print(isValid);
		if (!isValid) {
			return;
		}

		const formData = form.values();
		print(formData);

		const res = await postAuth('job/create/', formData);

		if (res?.code == 201) {
			toastStore.trigger({
				message: 'Job created successfully!'
			});
			// goto('/jobs/my');
		} else {
			toastStore.trigger({
				message: res?.data.msg
			});
		}
	}
</script>

<div class="isolate">
	<div
		class="absolute inset-x-0 -z-50 transform-gpu overflow-hidden blur-3xl sm:top-[-20rem]"
		aria-hidden="true"
	>
		<div
			class="relative left-1/2 -z-10 aspect-[1155/678] w-[36.125rem] max-w-none -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-40rem)] sm:w-[72.1875rem]"
			style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"
		/>
	</div>
	<div class="mx-auto max-w-2xl text-center">
		<h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Create Job Posting</h2>
	</div>
	<form action="#" method="POST" class="mx-auto z-[999999] mt-16 max-w-xl sm:mt-20">
		<div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
			<div class="sm:col-span-2">
				<label for="company" class="block text-sm font-semibold leading-6 text-gray-900"
					>Short Description</label
				>
				<div class="mt-2.5">
					<input bind:value={form.title} type="text" name="company" id="company" class="input" />
					<small>
						{#each form.errors.title as err}
							<p class="text-red-500 text-sm">{err}</p>
						{/each}
					</small>
				</div>
			</div>
			<div class="sm:col-span-2">
				<label for="email" class="block text-sm font-semibold leading-6 text-gray-900"
					>Education Level</label
				>
				<div class="mt-2.5">
					<select bind:value={form.education_level} class="select">
						{#each degree_levels as level}
							<option value={level.value}>{level.label}</option>
						{/each}
					</select>
					<small>
						{#each form.errors.education_level as err}
							<p class="text-red-500 text-sm">{err}</p>
						{/each}
					</small>
				</div>
			</div>
		</div>
		<div class="mt-10">
			<button
				on:click|preventDefault={onSubmit}
				type="submit"
				class="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
				>Post</button
			>
		</div>
	</form>
</div>
