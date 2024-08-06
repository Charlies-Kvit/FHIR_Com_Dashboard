<script lang="ts">
  import { Person } from "$lib/store/person.store";
  import { fly, slide } from "svelte/transition";
  import BarChart from "../Diagram/BarChart.svelte";

  let { person, summary_index } = $props<{
    person: Person;
    summary_index: number;
  }>();
  let show_content = $state(false);
</script>

{#await person.summary}
  <div
    out:fly={{ y: -10, duration: 300 }}
    class="text-center w-full p-1"
    onoutroend={() => (show_content = true)}
  >
    <p>Wait ...</p>
  </div>
{:then res}
  {#if show_content}
    <div
      class="w-[min(100%,290px)] aspect-square transition-all"
      transition:fly={{ x: -100, duration: 1000 }}
    >
      <BarChart data={res} bind:selected={summary_index}></BarChart>
    </div>
  {/if}
{:catch _}
  {#if show_content}
    <div in:slide={{ axis: "x", duration: 500 }}>
      <p class="break-keep text-nowrap">No data</p>
    </div>
  {/if}
{/await}
