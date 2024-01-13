<script lang="ts">
	import LightSwitch from '$lib/components/LightSwitch.svelte';
	import {Label} from '$lib/components/ui/label';
	import {Input} from '$lib/components/ui/input';
	import FileUpload from '$lib/components/FileUpload.svelte';
	import Header from '$lib/components/Header.svelte';
	import {Button} from '$lib/components/ui/button';

    export let params;
</script>

<div>
    <form class="flex w-full max-w-sm items-center space-x-2">
      <Input placeholder="Ask the Genie" />
      <Button>Enter</Button>
    </form>
</div>