<script>
	import { postAuth } from '$lib/net';
	import { mydegrees, profile } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import Trash from './Trash.svelte';
	export let degree;

	import Select from 'svelte-select';

	let filterText = '';

	let value = null;

	let items = [];

	function handleFilter(e) {
		if (value?.find((i) => i.label === filterText)) return;
		if (e.detail.length === 0 && filterText.length > 0) {
			const prev = items.filter((i) => !i.created);
			if (items.length < 7) {
				items = [...prev, { value: filterText, label: filterText, created: true }];
			}
		}
	}

	function handleChange(e) {
		items = items.map((i) => {
			delete i.created;
			return i;
		});
	}
</script>

<div class="flex justify-end">
	<button
		on:click={() => {
			mydegrees.remove(degree);
		}}
		class="btn btn-icon"
	>
		<Trash />
	</button>
</div>

<div class="grid grid-cols-6 gap-4">
	<label class="label col-span-6 sm:col-span-3">
		<span>Degree Name</span>
		<input class="input" bind:value={degree.name} type="text" placeholder="Harvard" />
	</label>

	<label class="label col-span-6 sm:col-span-3">
		<span>University Name</span>
		<input bind:value={degree.university} class="input" type="text" placeholder="Harvard" />
	</label>
	<label class="label col-span-6 sm:col-span-3">
		<span>Status</span>
		<select bind:value={degree.status} class="select">
			<option value="in_progress">In progress</option>
			<option value="completed">Completed</option>
		</select>
	</label>

	<label class="label col-span-6 sm:col-span-3">
		<span>Obtained GPA</span>
		<input bind:value={degree.obtained_gpa} class="input" type="text" placeholder="3.5" />
	</label>
	<label class="label col-span-6 sm:col-span-3">
		<span>Total GPA</span>
		<input class="input" bind:value={degree.total_gpa} type="text" placeholder="4.0" />
	</label>

	<!-- svelte-ignore a11y-label-has-associated-control -->
	<label class="label col-span-6 sm:col-span-3">
		<span>Courses (recomended)</span>
		<div class="themed">
			<Select
				on:change={handleChange}
				multiple
				on:filter={handleFilter}
				placeholder="Start Typing"
				bind:filterText
				bind:value={degree.courses}
				{items}
			>
				<div slot="item" let:item>
					{item.created ? 'Add new: ' : ''}
					{item.label}
				</div>
			</Select>
			<div class="text-sm">Min 5 or Max 7 is allowed</div>
		</div>
	</label>
</div>

<style>
	:global(.themed) {
		--border: 1px solid #744aa1;
		--border-focused: 1px solid #744aa1;
		--border-hover: 1px solid #744aa1;
		--chevron-background: #744aa1;
		--clear-select-color: #744aa1;
		--item-hover-color: #744aa1;
		--item-hover-bg: #f2eef7;
		--input-color: #744aa1;
		--item-is-active-bg: #744aa1;
		--list-background: #faf8fc;
		--multi-item-bg: #faf8fc;
		--multi-item-clear-icon-color: #744aa1;
		--multi-item-color: #744aa1;
		--value-container-padding: 0.5rem 0.75;

		--border-radius: 4px;
		--placeholder-color: #744aa1;
		--background: #e5dcef;
	}
</style>
