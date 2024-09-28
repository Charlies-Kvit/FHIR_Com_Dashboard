<script lang="ts">
  import { type Account, accounts } from "$lib/store/account.store";
  import { type Dashboard } from "$lib/store/dashboard.store";
  import EditForm from "$lib/components/EditForm.svelte";

  let { dashboard, onadd } = $props<{
    dashboard: Dashboard;
    onadd: () => void;
  }>();
  let account: Omit<Account, "id" | "summary"> = {
    avatar_url: "",
    name: "",
    email: "",
    group_id: dashboard.id,
    zulip_id: 0,
  };

  const add_person = () => {
    accounts.add(account);
    onadd();
  };
</script>

<EditForm title="Add person" oncomplete={add_person}>
  <input
    class="input"
    type="text"
    bind:value={account.avatar_url}
    placeholder="Upload image"
  />
  <input
    class="input"
    type="text"
    bind:value={account.name}
    placeholder="Name"
  />
  <input
    class="input"
    type="email"
    bind:value={account.email}
    placeholder="E-mail"
  />
  <input
    class="input"
    type="email"
    bind:value={account.zulip_id}
    placeholder="E-mail"
  />
</EditForm>
