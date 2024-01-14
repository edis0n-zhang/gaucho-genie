<script lang="ts">
	import { writable } from 'svelte/store';

	const responseOutput = writable('');
	let userInput = 'What is the hardest machine learning class at UCSB';
	const conversationHistory = writable('');

	responseOutput.set('NOTHING YET');

	async function get_response() {
		responseOutput.set('Pressed')
		try {
			const response = await fetch(
				`http://127.0.0.1:5000/get_response?input=${encodeURIComponent(userInput)}&conversation_history=${encodeURIComponent($conversationHistory)}`
			);
			
			responseOutput.set('HUH')
			if (response.ok) {
				const data = await response.json();
				conversationHistory.set(data.conversation_history); // Update conversation history
				console.log(conversationHistory);
				responseOutput.set(data.output); // Update response output
				console.log(responseOutput);
			} else {
				console.error('Failed to fetch response');
			}
		} catch (error) {
			console.error('Error fetching response:', error);
		}
	}
</script>

<main>
	<button on:click={get_response}>Get Response</button>
	<div>
		{$responseOutput}
	</div>
	<div>
		{$conversationHistory}
	</div>
</main>
