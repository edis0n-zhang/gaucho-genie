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

<main class="container mx-auto p-4 text-foreground">
	<div class="h-[650px] bg-gray-500 rounded-md bg-transparent">
		{#each messages as { sender, text } (text)}
			<div class="{sender === 'user' ? 'text-right' : 'text-left'} mb-2">
				<span
					class="inline-block dark:bg-blue-500 text-white p-2 rounded {sender === 'user'
						? 'user-message'
						: ''}">{text}</span
				>
			</div>
		{/each}
	</div>

	<div class="mt-4 flex items-center text-foreground">
		<input
			bind:value={userInput}
			class="w-full p-2 border rounded bg-transparent mr-2"
			placeholder="Ask the Genie"
			on:keydown={(e) => e.key === 'Enter' && sendMessage()}
		/>
		<Button on:click={sendMessage}>
			<ArrowLeftFromLine />
		</Button>
	</div>
</main>
