<script>
	import Carousel from 'svelte-carousel';

	let carousel; // for calling methods of the carousel instance
	const handleNextClick = () => {
		carousel.goToNext();
	};

	const images = [
		'https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1544717305-2782549b5136?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1495995424756-6a5a3f9e7543?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1618355776464-8666794d2520?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80',
		'https://images.unsplash.com/photo-1567168539593-59673ababaae?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=528&q=80'
	];
</script>

<Carousel
	autoplayDuration={3000}
	autoplay={true}
	pauseOnFocus={true}
	arrows={false}
	bind:this={carousel}
>
	{#each images as image}
		<img
			src={image}
			alt=""
			class="aspect-[2/3] w-full rounded-xl bg-gray-900/5 object-cover shadow-lg"
		/>
	{/each}
</Carousel>
