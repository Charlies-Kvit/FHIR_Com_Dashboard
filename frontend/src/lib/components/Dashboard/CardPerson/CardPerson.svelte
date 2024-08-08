<script lang="ts">
  import Modal from "$lib/components/Modal.svelte";
  import PersonSettings from "$lib/components/Prompts/PersonSettings.svelte";
  import type { Person, Summary } from "$lib/store/person.store";
  import Preview from "./Preview.svelte";
  import ShowMore from "./ShowMore.svelte";
  import Chart from "./Chart.svelte";

  let { person } = $props<{ person: Person }>();

  let active_summary_index = $state(0);
  let summaries: undefined | Summary[] = $state(undefined);
  let active_summary = $derived.by(() => {
    if (summaries == undefined) return undefined;
    return summaries[active_summary_index];
  });
  person.summary.then((v: Summary[] | undefined) => {
    summaries = v;
  });
  let show_more = $state(false);
  let show_settings = $state(false);
</script>

<Modal bind:open={show_settings}>
  <PersonSettings {person}></PersonSettings>
</Modal>
<Modal bind:open={show_more}>
  <ShowMore {...person} summary={active_summary}></ShowMore>
</Modal>
<div
  class="card bg-base-100 card-bordered border-base-300 flex flex-row p-6 h-[390px]"
>
  <div class="flex w-[min(290px,35vw)] shrink-0 items-center justify-center">
    <Chart {summaries} bind:active_summary_index></Chart>
  </div>
  <div class="divider mx-6 divider-horizontal"></div>
  <div class="">
    <Preview
      {...person}
      summary={active_summary}
      onmore={() => (show_more = true)}
      onsettings={() => (show_settings = true)}
      summary_index={active_summary_index}
    ></Preview>
  </div>
</div>
