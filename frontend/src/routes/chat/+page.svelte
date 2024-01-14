<script>
    import Header from '$lib/components/Header.svelte';
    import { ArrowLeftFromLine } from 'lucide-svelte';
    import { Button } from '$lib/components/ui/button';
    import { writable, get } from 'svelte/store';

    let messages = [];
    let userInput = '';
    const responseOutput = writable('');
    const conversationHistory = writable('');

    const sendMessage = () => {
        if (userInput.trim() !== '') {
            messages = [...messages, { sender: 'user', text: userInput }];
            simulateBotResponse(userInput);
            userInput = '';
        }
    };

    async function simulateBotResponse(userInput){
        try {
            const response = await fetch(
                `http://127.0.0.1:5000/get_response?input=${encodeURIComponent(userInput)}&conversation_history=${encodeURIComponent(get(conversationHistory))}`
            );
            
            if (response.ok) {
                const data = await response.json();
                conversationHistory.set(data.conversation_history);
                responseOutput.set(data.output);
                
                // Update messages with bot response
                messages = [...messages, { sender: 'bot', text: get(responseOutput) }];
            } else {
                console.error('Failed to fetch response');
            }
        } catch (error) {
            console.error('Error fetching response:', error);
        }
    };
</script>
<main class="h-screen bg-white dark:bg-black">
	<div>
		<Header />
	</div>

	<div class="w-full mx-auto p-4 text-foreground">
		<div class="h-[680px] bg-gray-500 rounded-md bg-transparent">
			{#each messages as { sender, text } (text)}
				<div class="{sender === 'user' ? 'text-right' : 'text-left'} mb-2">
					<span
						class="text-message inline-block bg-blue-500 text-white p-2 rounded {sender === 'user' ? 'user-message': ''}">
						{text}
						</span
					>
				</div>
			{/each}
		</div>

		<div class="mt-2 flex items-center text-foreground bg-transparent px-5">
			<input
				bind:value={userInput}
				class="text-white-900  w-full p-2 border border-gray dark:border-white dark:text-white rounded bg-transparent mr-2 bg-transparent"
				placeholder="Ask the Genie..."
				on:keydown={(e) => e.key === 'Enter' && sendMessage()}
			/>
			<Button on:click={sendMessage}>
				<ArrowLeftFromLine />
			</Button>
		</div>
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

	.text-message {
		white-space : pre-line;
	}
</style>