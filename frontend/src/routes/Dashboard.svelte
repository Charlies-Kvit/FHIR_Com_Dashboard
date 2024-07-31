<script>
  import CardPerson from "./CardPerson.svelte";
  import { selected_dashboard, persons } from "$lib/store.svelte";
  import { blur, fade, slide } from "svelte/transition";
  import { flip } from "svelte/animate";
</script>

{#key selected_dashboard.value}
  <div class="overflow-y-scroll col-span-full" out:slide>
    <article
      class="grid auto-rows-[minmax(min-content,200px)] grid-cols-1 lg:grid-cols-2 gap-6"
    >
      {#if selected_dashboard.value?.id}
        {#each persons.for_dashboard(selected_dashboard.value.id) as person, i (person.id)}
          <div animate:flip={{ duration: 1000 }} transition:slide>
            <CardPerson {person}></CardPerson>
          </div>
        {/each}
      {/if}
    </article>
  </div>
{/key}
