<script lang="ts">
  import { marked } from "marked";
  import Modal from "$lib/components/Modal.svelte";
  import PersonSettings from "$lib/components/Prompts/PersonSettings.svelte";
  import type { Person, Summary } from "$lib/store/person.store";
  import BarChart from "./Diagram/BarChart.svelte";

  let { person } = $props<{ person: Person }>();

  $effect(() => {
    console.log(person.summary);
  });

  let active_summary = $state(0);
  let summary = $derived(person.summary[active_summary]);
  let show_more = $state(false);
  let show_settings = $state(false);
</script>

<Modal bind:open={show_settings}>
  <PersonSettings {person}></PersonSettings>
</Modal>
<Modal bind:open={show_more}>
  <article>
    <div class="flex items-center gap-4 mb-6">
      <img
        src={person.avatar_url}
        alt=""
        class="w-[75px] h-[75px] rounded-full"
      />
      <h1 class="m-0 text-2xl dark:text-white">{person.name}</h1>
    </div>
    <div class="prose">
      {@html marked.parse(summary.text)}
    </div>
  </article>
</Modal>
<div class="card bg-base-100 card-bordered border-base-300 flex flex-row p-6">
  <div
    class="flex grow-[1.6] basis-0 items-center justify-center gap-4 overflow-x-hidden overflow-y-scroll"
  >
    <BarChart data={person.summary} bind:selected={active_summary}></BarChart>
  </div>
  <div class="divider mx-6 divider-horizontal"></div>
  <div class="basis-0 grow-[1]">
    <div class="flex justify-between items-start">
      <img
        src={person.avatar_url}
        class="w-[50px] h-[50px] rounded-full mb-4"
        alt=""
      />
      <button
        class="hover:rotate-90 transition-transform duration-700 h-[25px]"
        onclick={() => (show_settings = true)}
      >
        <span class="i-material-symbols-settings text-[25px]"></span>
      </button>
    </div>
    <h1 class="font-bold mb-2">{person.name}</h1>
    <p class="text-wrap break-all max-h-[10vw] truncate prose">
      {@html marked.parse(summary.text)}
    </p>
    <div class="flex justify-between mt-3">
      <a href={summary.url} class="link">Link</a>
      <button class="link" onclick={() => (show_more = true)}>Show more</button>
    </div>
  </div>
</div>
