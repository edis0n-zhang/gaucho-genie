
<script lang="ts">
	import {Label} from '$lib/components/ui/label';
	import {Input} from '$lib/components/ui/input';
</script>
  <Label
class="inline-flex items-center text-3xl px-4 py-2 bg-white-100 dark:bg-white-900 text-gray rounded-md cursor-pointer hover:bg-yellow-400 dark:hover:bg-yellow-900"
for="file-input">Click to Upload Your Transcript</Label
>
<Input
	id="file-input"
	type="file"
	accept="application/pdf"
	class="hidden"
/>