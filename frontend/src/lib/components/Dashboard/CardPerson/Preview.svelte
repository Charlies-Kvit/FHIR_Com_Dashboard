<script lang="ts">
  import type { Person } from "$lib/store/person.store";
  import { marked } from "marked";
  import { fade, slide } from "svelte/transition";

  let { person, summary_index, onmore, onsettings } = $props<{
    person: Person;
    summary_index: number;
    onmore: () => void;
    onsettings: () => void;
  }>();
</script>

<section class="flex flex-col overflow-hidden h-full">
  <div class="flex justify-between items-start basis-0 grow-1">
    <img
      src={person.avatar_url}
      class="w-[50px] h-[50px] rounded-full mb-4"
      alt=""
    />
    <button
      class="hover:rotate-90 transition-transform duration-700 h-[25px]"
      onclick={onsettings}
    >
      <span class="i-material-symbols-settings text-[25px]"></span>
    </button>
  </div>
  <div class="flex flex-col grow">
    <h1 class="font-bold mb-2">{person.name}</h1>
    {#await person.summary}
      <p out:slide={{ duration: 300 }}>Wait ...</p>
    {:then res}
      {@const summary = res[summary_index]}
      <div
        transition:slide|global={{ duration: 500, delay: 500 }}
        class="flex flex-col grow"
      >
        <div
          class="text-wrap break-all truncate prose basis-0 grow-[1] min-h-4 overflow-hidden"
        >
          {@html marked.parse(summary.text.slice(0, 250))}
        </div>
        <div class="flex justify-between mt-3">
          <a href={summary.url} class="link">Link</a>
          <button class="link" onclick={onmore}>Show more</button>
        </div>
      </div>
    {:catch}
      <p>
        No summary. Maybe you miss type email or summary can't be summarised
      </p>
    {/await}
  </div>
</section>
