<script>
	import Faq from '$lib/components/Faq.svelte';
import Hero from '$lib/components/Hero.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Header from '$lib/components/Nav.svelte';
	import Pricing from '$lib/components/Pricing.svelte';
	import Service from '$lib/components/Service.svelte';
</script>

<div class="bg-white">
	<!-- Header -->
	<Nav />

	<main class="isolate">
		<!-- Hero section -->
		<div class="relative isolate -z-10">
			<svg
				class="absolute inset-x-0 top-0 -z-10 h-[64rem] w-full stroke-gray-200 [mask-image:radial-gradient(32rem_32rem_at_center,white,transparent)]"
				aria-hidden="true"
			>
				<defs>
					<pattern
						id="1f932ae7-37de-4c0a-a8b0-a6e3b4d44b84"
						width="200"
						height="200"
						x="50%"
						y="-1"
						patternUnits="userSpaceOnUse"
					>
						<path d="M.5 200V.5H200" fill="none" />
					</pattern>
				</defs>
				<svg x="50%" y="-1" class="overflow-visible fill-gray-50">
					<path
						d="M-200 0h201v201h-201Z M600 0h201v201h-201Z M-400 600h201v201h-201Z M200 800h201v201h-201Z"
						stroke-width="0"
					/>
				</svg>
				<rect
					width="100%"
					height="100%"
					stroke-width="0"
					fill="url(#1f932ae7-37de-4c0a-a8b0-a6e3b4d44b84)"
				/>
			</svg>
			<div
				class="absolute left-1/2 right-0 top-0 -z-10 -ml-24 transform-gpu overflow-hidden blur-3xl lg:ml-24 xl:ml-48"
				aria-hidden="true"
			>
				<div
					class="aspect-[801/1036] w-[50.0625rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30"
					style="clip-path: polygon(63.1% 29.5%, 100% 17.1%, 76.6% 3%, 48.4% 0%, 44.6% 4.7%, 54.5% 25.3%, 59.8% 49%, 55.2% 57.8%, 44.4% 57.2%, 27.8% 47.9%, 35.1% 81.5%, 0% 97.7%, 39.2% 100%, 35.2% 81.4%, 97.2% 52.8%, 63.1% 29.5%)"
				/>
			</div>
			<div class="overflow-hidden">
				<div class="mx-auto max-w-5xl px-6 pb-32 pt-36 sm:pt-60 lg:px-8 lg:pt-32">
					<h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">About Us</h1>
					<p class="relative mt-6 text-lg leading-8 text-gray-600 sm:max-w-md lg:max-w-none">
						Welcome to this user-friendly platform that helps students connect to professors and
						professors find qualified students for their research needs.
						This platform is designed to ease the process of connecting professors and students and
						Postdocs together to facilitate intellectual and academic relationships. Please take
						your time to enjoy the experience. Thank you
					</p>
				</div>
			</div>
		</div>

		<!-- service section -->

		<!-- Testimonial section -->

		<!-- FAQs -->
		
		  <Faq/>

		<!-- CTA section -->
		<div class="relative -z-10 mt-32 px-6 lg:px-8">
			<div
				class="absolute inset-x-0 top-1/2 -z-10 flex -translate-y-1/2 transform-gpu justify-center overflow-hidden blur-3xl sm:bottom-0 sm:right-[calc(50%-6rem)] sm:top-auto sm:translate-y-0 sm:transform-gpu sm:justify-end"
				aria-hidden="true"
			>
				<div
					class="aspect-[1108/632] w-[69.25rem] flex-none bg-gradient-to-r from-[#ff80b5] to-[#9089fc] opacity-25"
					style="clip-path: polygon(73.6% 48.6%, 91.7% 88.5%, 100% 53.9%, 97.4% 18.1%, 92.5% 15.4%, 75.7% 36.3%, 55.3% 52.8%, 46.5% 50.9%, 45% 37.4%, 50.3% 13.1%, 21.3% 36.2%, 0.1% 0.1%, 5.4% 49.1%, 21.4% 36.4%, 58.9% 100%, 73.6% 48.6%)"
				/>
			</div>
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
					Boost your productivity.<br />Start using our app today.
				</h2>
				<p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-gray-600">
					Incididunt sint fugiat pariatur cupidatat consectetur sit cillum anim id veniam aliqua
					proident excepteur commodo do ea.
				</p>
				<div class="mt-10 flex items-center justify-center gap-x-6">
					<a
						href="#"
						class="rounded-md bg-primary-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500"
						>Get started</a
					>
					<a href="#" class="text-sm font-semibold leading-6 text-gray-900"
						>Learn more <span aria-hidden="true">→</span></a
					>
				</div>
			</div>
			<div
				class="absolute left-1/2 right-0 top-full -z-10 hidden -translate-y-1/2 transform-gpu overflow-hidden blur-3xl sm:block"
				aria-hidden="true"
			>
				<div
					class="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30"
					style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"
				/>
			</div>
		</div>
	</main>

	<!-- Footer -->
	<div class="mx-auto mt-32 max-w-7xl px-6 lg:px-8">
		<footer
			aria-labelledby="footer-heading"
			class="relative border-t border-gray-900/10 py-24 sm:mt-56 sm:py-32"
		>
			<h2 id="footer-heading" class="sr-only">Footer</h2>
			<div class="xl:grid xl:grid-cols-3 xl:gap-8">
				<img
					class="h-7"
					src="https://tailwindui.com/img/logos/mark.svg?color=primary&shade=600"
					alt="Company name"
				/>
				<div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
					<div class="md:grid md:grid-cols-2 md:gap-8">
						<div>
							<h3 class="text-sm font-semibold leading-6 text-gray-900">Solutions</h3>
							<ul role="list" class="mt-6 space-y-4">
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Hosting</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>Data Services</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>Uptime Monitoring</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>Enterprise Services</a
									>
								</li>
							</ul>
						</div>
						<div class="mt-10 md:mt-0">
							<h3 class="text-sm font-semibold leading-6 text-gray-900">Support</h3>
							<ul role="list" class="mt-6 space-y-4">
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Pricing</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>Documentation</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Guides</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>API Reference</a
									>
								</li>
							</ul>
						</div>
					</div>
					<div class="md:grid md:grid-cols-2 md:gap-8">
						<div>
							<h3 class="text-sm font-semibold leading-6 text-gray-900">Company</h3>
							<ul role="list" class="mt-6 space-y-4">
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">About</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Blog</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Jobs</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Press</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900"
										>Partners</a
									>
								</li>
							</ul>
						</div>
						<div class="mt-10 md:mt-0">
							<h3 class="text-sm font-semibold leading-6 text-gray-900">Legal</h3>
							<ul role="list" class="mt-6 space-y-4">
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Claim</a>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Privacy</a
									>
								</li>
								<li>
									<a href="#" class="text-sm leading-6 text-gray-600 hover:text-gray-900">Terms</a>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</footer>
	</div>
</div>
