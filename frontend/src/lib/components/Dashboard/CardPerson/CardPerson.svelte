<script lang="ts">
  import Modal from "$lib/components/Modal.svelte";
  import PersonSettings from "$lib/components/Prompts/PersonSettings.svelte";
  import type { Person } from "$lib/store/person.store";
  import { fly, slide } from "svelte/transition";
  import BarChart from "../Diagram/BarChart.svelte";
  import Preview from "./Preview.svelte";
  import ShowMore from "./ShowMore.svelte";
  import Chart from "./Chart.svelte";

  let { person } = $props<{ person: Person }>();

  let active_summary_index = $state(0);
  let show_more = $state(false);
  let show_settings = $state(false);
</script>

<Modal bind:open={show_settings}>
  <PersonSettings {person}></PersonSettings>
</Modal>
<Modal bind:open={show_more}>
  <ShowMore summary_index={active_summary_index} {person}></ShowMore>
</Modal>
<div
  class="card bg-base-100 card-bordered border-base-300 flex flex-row p-6 h-[390px]"
>
  <div
    class="flex grow-[1.2] basis-0 items-center justify-center overflow-x-hidden"
  >
    <Chart {person} summary_index={active_summary_index}></Chart>
  </div>
  <div class="divider mx-6 divider-horizontal"></div>
  <div class="basis-0 grow-[1] h-full">
    <Preview
      {person}
      onmore={() => (show_more = true)}
      onsettings={() => (show_settings = true)}
      summary_index={active_summary_index}
    ></Preview>
  </div>
</div>
