<script>
    import LightSwitch from "$lib/components/LightSwitch.svelte";
    import { LampWallUp } from "lucide-svelte";
  
    function handleClick() {
      window.location.href = "";
    }
  </script>
  
  <div class="navbar sticky w-full p-4 flex justify-between">
    <button class="flex items-center" on:click={handleClick}>
      <LampWallUp class="text-blue-900 dark:text-yellow-400"/>
      <p class="font-bold text-blue-900 dark:text-yellow-400">Gaucho Genie</p>
    </button>
    <LightSwitch />
  </div>
  