<script lang="ts">
  import { dashboards, type Dashboard } from "$lib/store.svelte";
  import EditForm from "$lib/components/EditForm.svelte";

  let { onadd } = $props<{ onadd: () => void }>();
  let dashboard: Dashboard = { name: "" };
  const add_dashboard = () => {
    dashboards.add(dashboard);
    onadd();
  };
</script>

<EditForm title="Add dashboard" oncomplete={add_dashboard}>
  <input
    class="input"
    type="text"
    bind:value={dashboard.name}
    placeholder="Dashboard title"
  />
</EditForm>
