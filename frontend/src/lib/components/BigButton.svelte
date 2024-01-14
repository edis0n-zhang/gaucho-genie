<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { goto } from '$app/navigation';
</script>
<button 
	on:click={() => goto('/chat')}
	class="rounded-md font-matter text-md flex items-center justify-center 
	px-8 py-4 font-semibold uppercase leading-none [&amp;_svg]:ml-[8px] [&amp;_svg]:mt-[1px] 
	shadow-fill hover:shadow-input-grow border-primary-700 active:shadow-input-shrink border-2 
	transition-all duration-100	0 ease-in-out will-change-transform hover:translate-y-[-2px] active:translate-y-[2px] 
	active:duration-100 md:h-[90px] dark:text-black text-white group mx-auto h-full w-full bg-blue-950 dark:bg-yellow-500 md:w-auto md:min-w-[220px] lg:min-w-[295px]"
	>Have Your Wishes Granted by The Gaucho Genie<div class="ml-2 scale-150"><svg class="stroke-white dark:stroke-black stroke-2" fill="none" width="10" height="10" viewBox="0 0 10 10" aria-hidden="true">
	<path class="opacity-0 transition group-hover:opacity-100" d="M0 5h7"></path><path class="transition group-hover:translate-x-[3px]" d="M1 1l4 4-4 4"></path></svg></div></button>