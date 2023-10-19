<script>
	import { services } from '$lib/menu';
	import ExperienceCarousel from './ExperienceCarousel.svelte';
</script>

<div class="mx-auto mt-16 max-w-7xl px-6 sm:mt-16 lg:px-8">
	<div class="mx-auto max-w-2xl lg:text-center">
		<p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Services</p>
	</div>
	<div id="services" class="mx-auto max-w-2xl">
		<dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10">
			<ExperienceCarousel />
		</dl>
	</div>
</div>
