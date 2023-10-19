<script>
	import Carousel from 'svelte-carousel';

	let carousel; // for calling methods of the carousel instance
	const handleNextClick = () => {
		carousel.goToNext();
	};

	const images = [
		'https://images.unsplash.com/photo-1544717305-2782549b5136?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1618355776464-8666794d2520?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1567168539593-59673ababaae?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80'
	];
</script>

<Carousel
	autoplayDuration={3000}
	autoplay={true}
	pauseOnFocus={true}
	arrows={false}
	particlesToShow={3}
	bind:this={carousel}
>
		<a href="#" class=" max-w-sm p-6 m-4 bg-white border flex flex-col justify-between border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Blogs</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400">Some description</p>
		</a>
		<a href="#" class=" max-w-sm p-6 m-4 bg-white border flex flex-col justify-between border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Community</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400">Some description</p>
		</a>
		<a href="#" class=" max-w-sm p-6 m-4 bg-white border flex flex-col justify-between border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Events</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400">Some description</p>
		</a>
		
</Carousel>
