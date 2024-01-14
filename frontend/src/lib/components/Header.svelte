<script>
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import { LampWallUp } from 'lucide-svelte';
	import { goto } from '$app/navigation';

	function handleClick() {
		goto('/');
	}
</script>

<div
	class="navbar sticky w-full p-4 flex justify-between text-foreground bg-blue-950 dark:bg-yellow-500"
>
	<button class="flex items-center" on:click={handleClick}>
		<LampWallUp class="dark:text-blue-900 text-yellow-400" />
		<p class="font-bold dark:text-blue-900 text-yellow-400">Gaucho Genie</p>
	</button>
	<LightSwitch />
</div>
