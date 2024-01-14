<script>
    import LightSwitch from "$lib/components/LightSwitch.svelte";
    import { LampWallUp } from "lucide-svelte";
    import { goto } from '$app/navigation';
  
    function handleClick() {
     goto('/');
    }
  </script>
  
  <div class="navbar sticky w-full p-4 flex justify-between bg-background text-foreground">
    <button class="flex items-center" on:click={handleClick}>
      <LampWallUp class="text-blue-900 dark:text-yellow-400"/>
      <p class="font-bold text-blue-900 dark:text-yellow-400">Gaucho Genie</p>
    </button>
    <LightSwitch />
  </div>
  