<script lang="ts">
  import { Person, type Summary } from "$lib/store/person.store";
  import { fly, slide } from "svelte/transition";
  import BarChart from "../Diagram/BarChart.svelte";

  let { summaries, active_summary_index = $bindable() } = $props<{
    summaries: Summary[] | undefined;
    active_summary_index: number;
  }>();
</script>

<div class="flex w-[min(290px,35vw)] shrink-0 items-center justify-center">
  {#if summaries}
    <div
      class="w-[min(100%,290px)] aspect-square transition-all"
      transition:fly={{ x: -100, duration: 1000 }}
    >
      <BarChart data={summaries} bind:selected={active_summary_index}
      ></BarChart>
    </div>
  {:else}
    <div in:slide={{ axis: "x", duration: 500 }}>
      <p class="break-keep text-nowrap">No data</p>
    </div>
  {/if}
</div>
