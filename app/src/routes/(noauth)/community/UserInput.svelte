<script>
	import { createForm } from '$lib/formvalidator';
	import { postAuth } from '$lib/net';
	import { questions } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';

	export let topic;

	let form = createForm({
		title: {
			required: true
		},
		username: {
			required: true
		},
		message: {
			required: true
		},
		topic: {
			default: topic
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
			postAuth('community/create/', formData).then((res) => {
				if (res?.code == 201) {
					toastStore.trigger({
						message: 'Question posted successfully!'
					});

					questions.add(res?.data.question);
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
	<div class="col-span-6">
		<div class="text-xl">Post your question here</div>
	</div>

	<div class="col-span-3">
		<label class="label">
			<span>Title</span>
			<input bind:value={form.title} class="input" type="text" placeholder="Title of the post" />
			<small>
				{#each form.errors.title as err}
					<p class="text-red-500 text-sm">{err}</p>
				{/each}
			</small>
		</label>
	</div>
	<div class="col-span-3">
		<label class="label">
			<span>Username</span>
			<input bind:value={form.username} class="input" type="text" placeholder="Username" />
			<small>
				{#each form.errors.username as err}
					<p class="text-red-500 text-sm">{err}</p>
				{/each}
			</small>
		</label>
	</div>

	<div class="col-span-3">
		<label class="label">
			<span>Message</span>
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
