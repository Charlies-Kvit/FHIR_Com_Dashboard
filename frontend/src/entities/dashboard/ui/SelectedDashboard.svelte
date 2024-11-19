<script lang="ts">
  import { selected_dashboard } from "..";
  import { fade, slide } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { Account, accounts, CardAccount } from "@/entities/account";

  let dashboard_accounts = $derived(
    $accounts.filter((p: Account) => p.group_id == $selected_dashboard?.id),
  );
</script>

{#key $selected_dashboard}
  <div class="overflow-y-scroll col-span-full" out:slide in:fade>
    <article class="flex flex-col justify-center items-center gap-6 pb-6">
      {#if $selected_dashboard}
        {#each dashboard_accounts as account (account.id)}
          <div
            animate:flip={{ duration: 1000 }}
            transition:slide
            class="w-full flex justify-center"
          >
            <CardAccount {account}></CardAccount>
          </div>
        {/each}
      {/if}
    </article>
  </div>
{/key}
