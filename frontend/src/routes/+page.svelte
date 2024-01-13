<script lang="ts">
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import { goto } from '$app/navigation';
  </script>
  
  <LightSwitch />
  
  <div class="flex flex-col items-center justify-center h-screen">
	<div class="mb-8">
	  <button on:click={() => goto('/chatbot')} class="bg-blue-500 text-white px-4 py-2 rounded">
		Get Started
	  </button>
	</div>
  </div>
  