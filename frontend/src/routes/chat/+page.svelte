<script>
	import Header from '$lib/components/Header.svelte';
	import { ArrowLeftFromLine } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	let messages = [];
	let userInput = '';

	const sendMessage = () => {
		if (userInput.trim() !== '') {
			messages = [...messages, { sender: 'user', text: userInput }];
			userInput = '';
		}
	};
</script>

<div>
	<Header />
</div>

<main class="bg-background dark:bg-background w-full mx-auto p-4 text-foreground">
	<div class="h-[680px] bg-gray-500 rounded-md bg-transparent">
		{#each messages as { sender, text } (text)}
			<div class="{sender === 'user' ? 'text-right' : 'text-left'} mb-2">
				<span
					class="inline-block bg-blue-500 text-white p-2 rounded {sender === 'user' ? 'user-message': ''}">{text}</span
				>
			</div>
		{/each}
	</div>

	<div class="mt-2 flex items-center text-foreground bg-background dark:bg-background px-5">
		<input
			bind:value={userInput}
			class="text-gray-900  w-full p-2 border rounded bg-transparent mr-2 bg-background dark:bg-background"
			placeholder="Ask the Genie"
			on:keydown={(e) => e.key === 'Enter' && sendMessage()}
		/>
		<Button on:click={sendMessage}>
			<ArrowLeftFromLine />
		</Button>
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
