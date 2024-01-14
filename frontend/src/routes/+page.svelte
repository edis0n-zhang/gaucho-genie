<script lang="ts">
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import {Label} from '$lib/components/ui/label';
	import {Input} from '$lib/components/ui/input';
	import FileUpload from '$lib/components/FileUpload.svelte';
	import Header from '$lib/components/Header.svelte';
	import {Button} from '$lib/components/ui/button';
	import { goto } from '$app/navigation';

  </script>

	<Header/>

    <div
        class="flex flex-col gap-10 flex-1 items-center justify-center pb-10 md:pb-14 bg-background text-foreground"
    >
        <h1
            class="text-5xl sm:text-6xl md:text-7xl lg:text-8xl max-w-[1200px] mx-auto w-full text-center font-semibold"
        >
            Course Selection<br />
            Is <span class="line-through text-black-500"><span class="text-red-500">Hard</span></span>
            <span class="text-green-500">Easy</span>
        </h1>
        <p
			class="text-xl sm:text-2xl md:text-3xl text-center max-w-[1000px] mx-auto w-full"
		>	
			<span class="italic">Simplifying and Enhancing Your Course Selection Process with AI</span>
        </p>

		<h2
			class="text-xl sm:text-xl md:text-xl lg:text-4xl max-w-[1200px] mx-auto w-full text-center font-semibold"
		>
			How It Works<br />
		</h2>
		<p
			class="text-xl sm:text-xl md:text-xl text-center max-w-[1000px] mx-auto w-full"
		>
			<span class="italic">
			Our system utilizes advanced algorithms to analyze your transcript. 
			Course Recommendations are tailored from our extensive school database, ensuring personalized course suggestions for an optimized learning journey.</span>
		</p>	
		<FileUpload />

		<p
		class="text-s text-center"	
	>
		We are not affiliated with the University of California, Santa Barbara.<br>
		<span class="italic text-gray-500">This is a disclaimer statement.</span></p>

		<button on:click={() => goto('/chat')}>Talk to the Genie</button>

    </div>
  

<style>
</style>
