<script>
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import DarkGenie from '$lib/components/genie-dark.svelte';
	import LightGenie from '$lib/components/genie-light.svelte';
	import { goto } from '$app/navigation';
	import { setMode, mode } from 'mode-watcher';

	let isDarkMode = false;

	// Subscribe to mode changes
	function handleModeChange() {
		if ($mode === 'light') {
			setMode('dark');
		} else {
			setMode('light');
		}
	}

	function handleClick() {
		goto('/');
	}
</script>

<div
	class="navbar sticky w-full p-4 flex justify-between text-foreground bg-blue-950 dark:bg-yellow-500"
>
	<button class="flex items-center" on:click={handleClick}>
		{#if $mode === 'dark'}
			<DarkGenie class="mr-2" />
		{:else}
			<LightGenie class="mr-2" />
		{/if}
		<div class="ml-2">
			<p class="font-bold dark:text-blue-900 text-yellow-400">GAUCHO GENIE</p>
		</div>
	</button>
	<LightSwitch />
</div>
