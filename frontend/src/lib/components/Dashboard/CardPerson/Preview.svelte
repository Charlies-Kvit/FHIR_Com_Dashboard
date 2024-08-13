<script lang="ts">
  import type { Person, Summary } from "$lib/store/person.store";
  import { marked } from "marked";
  import { fade, fly, slide } from "svelte/transition";

  let { avatar_url, name, summary, onmore, onsettings } = $props<{
    avatar_url: string;
    name: string;
    summary: Summary | undefined;
    onmore: () => void;
    onsettings: () => void;
  }>();
</script>

<section class="flex grow flex-col overflow-hidden h-full">
  <div class="flex justify-between items-start basis-0 grow-1">
    <img src={avatar_url} class="w-[50px] h-[50px] rounded-full mb-4" alt="" />
    <button
      class="hover:rotate-90 transition-transform duration-700 h-[25px]"
      onclick={onsettings}
    >
      <span class="i-material-symbols-settings text-[25px]"></span>
    </button>
  </div>
  <div class="flex flex-col grow">
    <h1 class="font-bold mb-2">{name}</h1>
    <div class="text-wrap break-words truncate prose line-clamp-6 h-[12rem]">
      {#if summary}
        <div transition:fade class="flex flex-col grow">
          {@html marked.parse(summary.text)}
        </div>
        <div class="flex justify-between mt-3">
          <a href={summary.url} class="link">Link</a>
          <button class="link" onclick={onmore}>Show more</button>
        </div>
      {:else}
        <p transition:slide>
          No summary. Maybe you miss type email or summary can't be summarised
        </p>
      {/if}
    </div>
  </div>
</section>
