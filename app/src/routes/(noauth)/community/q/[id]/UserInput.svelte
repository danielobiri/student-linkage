<script>
	import { page } from '$app/stores';
	import { createForm } from '$lib/formvalidator';
	import { postAuth } from '$lib/net';
	import { questions } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import { answers } from './store';

	export let topic;

	let form = createForm({
		message: {
			required: true
		}
	});
	$: {
		form.validate();
	}
	function onSubmit() {
		console.log(form);

		form.validate();
		const isValid = form['isValid'];
		console.log(isValid);

		if (!isValid) {
			toastStore.trigger({
				message: 'Please fill in all the fields'
			});
			return;
		} else {
			const formData = form.values();

			postAuth('community/q/' + $page.params.id + '/answer/', formData).then((res) => {
				if (res?.code == 201) {
					toastStore.trigger({
						message: 'Answer posted successfully!'
					});

					answers.set(res.data.answers);
					form.message = '';
					// questions.add(res?.data.question);
				} else {
					toastStore.trigger({
						message: res?.data.msg
					});
				}
			});
		}
	}
</script>

<div class="grid mt-6 grid-cols-6 gap-6 p-4 shadow-md">
	<div class="col-span-3">
		<label class="label">
			<span>Your Answer</span>
			<textarea bind:value={form.message} class="input" placeholder="Text message here" />
			<small>
				{#each form.errors.message as err}
					<p class="text-red-500 text-sm">{err}</p>
				{/each}
			</small>
		</label>
	</div>
	<div class="col-span-6">
		<button class="btn variant-filled" on:click={onSubmit}> Post </button>
	</div>
</div>
