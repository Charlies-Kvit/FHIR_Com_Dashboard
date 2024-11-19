<script lang="ts">
  import { type Dashboard, selected_dashboard } from "@/entities/dashboard";

  let { dashboard, onedit, onaddperson } = $props<{
    dashboard: Dashboard;
    onedit: () => void;
    onaddperson: () => void;
  }>();
</script>

<button
  class={dashboard.id == $selected_dashboard?.id
    ? "font-bold dark:font-normal dark:text-white"
    : ""}
  onclick={() => selected_dashboard.select(dashboard)}
>
  {dashboard.name}
</button>
<div class="grow"></div>
<button class="h-min" onclick={onedit} aria-label="Edit">
  <span class="block i-material-symbols-settings text-xl text-[#5D5D5D]"></span>
</button>
<button
  class="h-min rounded-full bg-[#5D5D5D]"
  onclick={onaddperson}
  aria-label="Add person"
>
  <span class="block i-material-symbols-add text-xl text-[#D9D9D9]"></span>
</button>
