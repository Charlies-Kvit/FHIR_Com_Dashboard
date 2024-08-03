<script lang="ts">
  import { dashboards, type Dashboard } from "$lib/store/dashboard.store";
  import EditForm from "$lib/components/EditForm.svelte";

  let { dashboard, onremove } = $props<{
    dashboard: Dashboard;
    onremove?: () => void;
  }>();
  const update_dashboard = () => {
    dashboards.update(dashboard, new_dashboard);
  };
  const delete_dashboard = () => {
    dashboards.remove(dashboard);
    onremove();
  };
  let new_dashboard: Dashboard = { ...dashboard };
</script>

<EditForm
  title="Edit dashboard"
  oncomplete={update_dashboard}
  ondelete={delete_dashboard}
>
  <input
    class="input"
    type="text"
    bind:value={new_dashboard.name}
    placeholder="Dashboard name"
  />
</EditForm>
