<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Sun, Moon } from 'lucide-svelte';

	import { toggleMode } from 'mode-watcher';
</script>

<Button
	on:click={toggleMode}
	size="icon"
	class="bg-yellow-500 dark:bg-blue-950 hover:bg-yellow-400/90 dark:hover:bg-blue-950/90"
>
	<Sun
		class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
		color="rgb(23 37 84)"
	/>
	<Moon
		class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
		color="rgb(234 179 8)"
	/>
	<span class="sr-only">Toggle theme</span>
</Button>
