<script lang="ts">
  import type { Person } from "$lib/store/person.store";
  import { marked } from "marked";

  let { person, summary_index } = $props<{
    person: Person;
    summary_index: number;
  }>();
</script>

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
    {@html marked.parse(person.summary[summary_index].text)}
  </div>
</article>
