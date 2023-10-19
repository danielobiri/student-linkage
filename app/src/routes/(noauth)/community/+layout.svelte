<script>
	import Experience from '$lib/components/Experience.svelte';
	import Faq from '$lib/components/Faq.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Header from '$lib/components/Nav.svelte';
	import NavCom from '$lib/components/NavCom.svelte';
	import Pricing from '$lib/components/Pricing.svelte';
	import Service from '$lib/components/Service.svelte';
	import Testimonials from '$lib/components/Testimonials.svelte';
</script>

<div class="bg-white">
	<!-- Header -->
	<NavCom />

	<main class="isolate mt-24 max-w-7xl mx-auto p-4">
		<!-- Hero section -->
		<div class="text-4xl font-bold">Welcome to Student Linkage Community</div>

		<div class="text-xl font-semibold mt-4">Topics</div>

		<div class="my-4 flex space-x-2">
			<a href="/community/general">
				<span class="chip variant-filled">
					<span> #General</span>
				</span>
			</a>
			<a href="/community/visa">
				<span class="chip variant-soft hover:variant-filled">
					<span> #VisaInformation</span>
				</span>
			</a>
			<a href="/community/finance">
				<span class="chip variant-soft hover:variant-filled">
					<span> #Scholarships and Finances </span>
				</span>
			</a>
			<a href="/community/housing">
				<span class="chip variant-soft hover:variant-filled">
					<span> #Housing and Accommodation</span>
				</span>
			</a>
		</div>

		<slot />
	</main>

	<!-- Footer -->
	<Footer />
</div>
