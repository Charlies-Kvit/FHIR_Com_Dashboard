<script lang="ts">
  import { EditForm } from "@/shared/ui";
  import { dashboards } from "@/entities/dashboard";
  import { type Account, accounts } from "..";

  let { account } = $props<{ account: Account }>();
  let edit_account: Omit<Account, "summary"> = $state(structuredClone(account));

  const update_person = () => {
    accounts.update(edit_account);
  };
  const delete_person = () => {
    accounts.remove(account);
  };
</script>

<EditForm
  title="Edit person"
  oncomplete={update_person}
  ondelete={delete_person}
>
  <select class="select" name="dashboard" bind:value={edit_account.group_id}>
    {#each $dashboards as dashboard}
      <option value={dashboard.id}>{dashboard.name}</option>
    {/each}
  </select>
  <input
    class="input"
    type="text"
    bind:value={edit_account.avatar_url}
    placeholder="Upload image"
  />
  <input
    class="input"
    type="text"
    bind:value={edit_account.name}
    placeholder="Name"
  />
  <input
    class="input"
    type="email"
    bind:value={edit_account.email}
    placeholder="E-mail"
  />
  <input
    class="input disable-arrows"
    type="number"
    bind:value={edit_account.zulip_id}
    placeholder="Zulip id"
  />
</EditForm>
