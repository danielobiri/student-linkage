<script>
	export let topic;
	export let q;
</script>

<div class="card card-hover shadow-md m-2">
	<div class="card-header text-2xl">
		<span class="capitalize">
			{q.title}
		</span>
		<div class="text-sm text-gray-500">
			Made by
			{q.username}
			<span>
				{new Date(q.created_at).toLocaleDateString()}
			</span>
		</div>
	</div>
	<div class="p-4">
		{q.message}
	</div>
	<div class="card-footer flex justify-evenly">
		<a
			href="/community/q/{q.id}"
			class="flex flex-col justify-center items-center hover:text-primary-500"
		>
			<svg class="h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
				<path
					fill="currentColor"
					d="M6 14h12v-2H6v2Zm0-3h12V9H6v2Zm0-3h12V6H6v2ZM4 18q-.825 0-1.413-.588T2 16V4q0-.825.588-1.413T4 2h16q.825 0 1.413.588T22 4v18l-4-4H4Z"
				/>
			</svg>
			<small>Comment</small>
		</a>
		<button class="flex flex-col justify-center items-center hover:text-primary-500">
			<svg class="h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
				<path
					fill="currentColor"
					d="M23 10a2 2 0 0 0-2-2h-6.32l.96-4.57c.02-.1.03-.21.03-.32c0-.41-.17-.79-.44-1.06L14.17 1L7.59 7.58C7.22 7.95 7 8.45 7 9v10a2 2 0 0 0 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2M1 21h4V9H1v12Z"
				/>
			</svg>
			<small>Like</small>
		</button>
		<button class="flex flex-col justify-center items-center hover:text-primary-500">
			<svg class="h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
				<path fill="currentColor" d="M5 21V4h9l.4 2H20v10h-7l-.4-2H7v7H5Z" />
			</svg>
			<small>Flag</small>
		</button>
		<button class="flex flex-col justify-center items-center hover:text-primary-500">
			<svg class="h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
				<path
					fill="currentColor"
					d="M18 22q-1.25 0-2.125-.875T15 19q0-.175.025-.363t.075-.337l-7.05-4.1q-.425.375-.95.588T6 15q-1.25 0-2.125-.875T3 12q0-1.25.875-2.125T6 9q.575 0 1.1.213t.95.587l7.05-4.1q-.05-.15-.075-.337T15 5q0-1.25.875-2.125T18 2q1.25 0 2.125.875T21 5q0 1.25-.875 2.125T18 8q-.575 0-1.1-.212t-.95-.588L8.9 11.3q.05.15.075.338T9 12q0 .175-.025.363T8.9 12.7l7.05 4.1q.425-.375.95-.587T18 16q1.25 0 2.125.875T21 19q0 1.25-.875 2.125T18 22Z"
				/>
			</svg>
			<small>Share</small>
		</button>
	</div>
</div>
