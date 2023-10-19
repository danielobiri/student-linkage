<script>
	let isOpen = false;
</script>

<div class="pt-6">
	<dt>
		<!-- Expand/collapse question button -->
		<button
			on:click={() => (isOpen = !isOpen)}
			type="button"
			class="flex w-full items-start justify-between text-left text-gray-900"
			aria-controls="faq-0"
			aria-expanded="false"
		>
			<span class="text-base font-semibold leading-7">How can i apply?</span>
			<span class="ml-6 flex h-7 items-center">
				<!--
    Icon when question is collapsed.

    Item expanded: "hidden", Item collapsed: ""
  -->
				{#if isOpen}
					<svg
						class=" h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						aria-hidden="true"
					>
						<path stroke-linecap="round" stroke-linejoin="round" d="M18 12H6" />
					</svg>
				{:else}
					<svg
						class="h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						aria-hidden="true"
					>
						<path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6" />
					</svg>
				{/if}
				<!--
    Icon when question is expanded.

    Item expanded: "", Item collapsed: "hidden"
  -->
			</span>
		</button>
	</dt>
	{#if isOpen}
		<dd class="mt-2 pr-12" id="faq-0">
			<p class="text-base leading-7 text-gray-600">
				I don&#039;t know, but the flag is a big plus. Lorem ipsum dolor sit amet consectetur
				adipisicing elit. Quas cupiditate laboriosam fugiat.
			</p>
		</dd>
	{/if}
</div>
