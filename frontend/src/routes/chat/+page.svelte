<script>
	import Header from '$lib/components/Header.svelte';
  import { ArrowLeftFromLine } from 'lucide-svelte';
  let messages = [];
  let userInput = '';

  const sendMessage = () => {
    if (userInput.trim() !== '') {
      messages = [...messages, { sender: 'user', text: userInput }];
      userInput = '';
    }
  };
</script>

<style>
  .user-message {
    color: white; /* Change this to the color for user messages */
  }

  input {
    color: black; /* Set the color for the text typed by the user */
  }

  .chat-box {
    background-color: white; /* Change this to the desired background color */
    padding: 20px; /* Adjust padding as needed */
    height: 600px;
    overflow-y: auto;
    border-radius: 10px; /* Add border radius for rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a subtle box shadow */
  }
</style>

<div>
  <Header />
</div>

<main class="container mx-auto p-4">
  <div class="chat-box">
    {#each messages as { sender, text } (text)}
      <div class="{sender === 'user' ? 'text-right' : 'text-left'} mb-2">
        <span class="inline-block bg-blue-500 text-white p-2 rounded {sender === 'user' ? 'user-message' : ''}">{text}</span>
      </div>
    {/each} 
  </div>

  <div class="mt-4 flex items-center">
    <input
      bind:value={userInput}
      class="w-full p-2 border rounded"
      placeholder="Ask the Genie"
      on:keydown={(e) => e.key === 'Enter' && sendMessage()}
    />
    <button on:click={sendMessage} class="absolute right-14 bottom-30 cursor-pointer text-green-500">
      <ArrowLeftFromLine />
  </div>
</main>

<div>
  <p
    class="text-s text-center"	
  >
    We are not affiliated with the University of California, Santa Barbara.<br>
    <span class="italic text-gray-500">This is a disclaimer statement.</span></p>
</div>