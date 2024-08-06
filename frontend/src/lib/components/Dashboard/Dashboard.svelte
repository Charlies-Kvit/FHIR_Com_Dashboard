<script>
  import CardPerson from "./CardPerson/CardPerson.svelte";
  import { selected_dashboard } from "$lib/store/dashboard.store";
  import { fade, slide } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { persons } from "$lib/store/person.store";

  let dashboard_persons = $derived(
    $persons.filter((p) => p.group_id == $selected_dashboard?.id),
  );
</script>

{#key $selected_dashboard}
  <div class="overflow-y-scroll col-span-full" out:slide in:fade>
    <article
      class="grid justify-center items-center grid-cols-1 xl:grid-cols-2 gap-6"
    >
      {#if $selected_dashboard}
        {#each dashboard_persons as person (person.id)}
          <div animate:flip={{ duration: 1000 }} transition:slide>
            <CardPerson {person}></CardPerson>
          </div>
        {/each}
      {/if}
    </article>
  </div>
{/key}
