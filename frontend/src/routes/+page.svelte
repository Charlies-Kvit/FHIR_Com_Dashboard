<script lang="ts">
  import Dashboard from "./Dashboard.svelte";
  import DatePicker from "$lib/components/DatePicker.svelte";
</script>

<div class="flex mb-6 gap-6 col-span-full">
  <DatePicker></DatePicker>
  <input type="range" class="w-[456px] max-w-[50%]" />
</div>
<Dashboard></Dashboard>
