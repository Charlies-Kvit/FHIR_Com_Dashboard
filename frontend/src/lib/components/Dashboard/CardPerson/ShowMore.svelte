<script lang="ts">
  import type { Summary } from "$lib/store/account.store";
  import { marked } from "marked";

  let { avatar_url, name, summary } = $props<{
    avatar_url: string;
    name: string;
    summary: Summary | undefined;
  }>();
</script>

{#if summary}
  <article class="min-w-[min(550px,60vw)]">
    <div class="flex items-center gap-4 mb-6">
      <img src={avatar_url} alt="" class="w-[75px] h-[75px] rounded-full" />
      <h1 class="m-0 text-2xl dark:text-white">{name}</h1>
    </div>
    <div class="prose">
      {@html marked.parse(summary.text)}
    </div>
  </article>
{/if}
