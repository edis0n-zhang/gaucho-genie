<script lang="ts">
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import FileUpload from '$lib/components/FileUpload.svelte';
	import Header from '$lib/components/Header.svelte';
	import { Button } from '$lib/components/ui/button';
	import { goto } from '$app/navigation';
</script>

<main class="h-screen bg-white dark:bg-black">
	<div>
		<Header />
	</div>
	
	<div
		class="flex flex-col gap-10 flex-1 items-center justify-center pb-10 md:pb-14 text-foreground"
	>
		<h1
			class="text-5xl sm:text-6xl md:text-7xl lg:text-8xl max-w-[1200px] mx-auto w-full text-center font-semibold mt-16"
		>
			Course Selection<br />
			Is <span class="line-through text-black-500"><span class="text-red-500">Hard</span></span>
			<span class="text-green-500">Easy</span>
		</h1>
		<p class="text-xl sm:text-2xl md:text-3xl text-center max-w-[1000px] mx-auto w-full">
			<span class="italic">Simplifying and Enhancing Your Course Selection Process with AI</span>
		</p>

		<button
			on:click={() => goto('/chat')}
			class="font-bold inline-flex items-center text-3xl px-8 py-6 dark:bg-yellow-500 text-gray rounded-md cursor-pointer dark:hover:bg-yellow-400 bg-blue-950 hover:bg-blue-950/90 text-white dark:text-black"
			>Let The Genie Know Your Wishes</button
		>

		<main class="container mx-auto p-4 text-foreground">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
				<div
					class="bg-blue-950 dark:bg-yellow-500 p-6 rounded-md shadow-lg dark:text-black text-white"
				>
					<h2 class="text-lg font-semibold mb-2 text-center">Estimate Course Difficulty</h2>
					<p class="text-sm italic text-center">
						Analyzes past student grades to estimate course diffiulty.
					</p>
				</div>
				<div
					class="bg-blue-950 dark:bg-yellow-500 p-6 rounded-md shadow-lg dark:text-black text-white"
				>
					<h2 class="text-lg font-semibold mb-2 text-center">Personalized Recommendations</h2>
					<p class="text-sm italic text-center">
						Tailored course recommendations are generated based on the analysis and specific user input.
					</p>
				</div>

				<div
					class="bg-blue-950 dark:bg-yellow-500 p-6 rounded-md shadow-lg dark:text-black text-white"
				>
					<h2 class="text-lg font-semibold mb-2 text-center">Instant Response</h2>
					<p class="text-sm italic text-center">
						No delays or waiting times whatsoever. 
						Our system ensures immediate replies, providing a seamless and efficient user experience.
					</p>
				</div>
			</div>
		</main>

		<p class="text-s text-center">
			*We are not affiliated with the University of California, Santa Barbara.<br />
			<span class="italic text-gray-500">This is a disclaimer statement.</span>
		</p>
	</div>
</main>

<style>
	:global(body) {
		--background-light: hsl(0 0% 100%); /* Light mode background color */
		--background-dark: hsl(226.2 57% 21%); /* Dark mode background color */
	}

	:global(body:not(.dark)) {
		background-color: var(--background-light);
	}

	:global(body.dark) {
		background-color: var(--background-dark);
	}

	/* Ensure the .bg-background class uses these variables */
	.bg-background {
		background-color: var(--background-light);
	}

	:global(.dark) .bg-background {
		background-color: var(--background-dark);
	}
</style>
