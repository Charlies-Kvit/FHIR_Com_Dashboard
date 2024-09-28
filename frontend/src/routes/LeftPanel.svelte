<script lang="ts">
  import { dashboards, selected_dashboard, type Dashboard } from "$lib/store/dashboard.store";
  import Modal from "$lib/components/Modal.svelte";
  import AddDashboard from "$lib/components/Prompts/AddDashboard.svelte";
  import EditDashboard from "$lib/components/Prompts/EditDashboard.svelte";
    import LeftPanelEntry from "./LeftPanelEntry.svelte";
    import AddAccount from "$lib/components/Prompts/AddAccount.svelte";

  let show_add = $state(false);
  let show_edit_dashboard = $state(false);
  let dashboard_to_edit: Dashboard | null = $state(null);
  let show_add_person = $state(false);
  let innerWidth = $state(0)
  let is_open: undefined | boolean = $state(undefined)
  let classs = $derived.by(()=>{
    if(is_open === undefined) return ''
    else return "fixed inset-0 z-50 " + (is_open ? 'animate__slideInLeft' : 'animate__slideOutLeft')
  })
  $effect(()=>{
    if(innerWidth > 1024 /* tailwindcss lg responsive width */ && is_open !== undefined) is_open = undefined
  })
</script>

<svelte:window bind:innerWidth></svelte:window>

<section class="row-span-15 col-span-1 box-content overflow-hidden ">
  <nav class="bg-base-300 flex flex-col h-full px-6 py-9 transition-all animate__animated {classs} lg:static lg:!animate-none">
    {#key $selected_dashboard}
    <ul class="list-none flex flex-col gap-6">
      {#each $dashboards as dashboard (dashboard.id)}
        <li class="flex items-center gap-2 border-b pb-6 border-[#313131]">
            <LeftPanelEntry {dashboard} 
              onedit={ () => {
                  dashboard_to_edit = dashboard;
                  show_edit_dashboard = true;
                }
              }
              onaddperson={() => {
                    dashboard_to_edit = dashboard;
                    show_add_person = true;
                  }
              }
              ></LeftPanelEntry>
        </li>
      {/each}
    </ul>
    {/key}
    <div class="grow"></div>
    <div>
      <button class="rounded-full bg-[#5D5D5D]" onclick={() => (show_add = true)}
        ><span class="block i-material-symbols-add text-[32px] text-base-200 dark:text-base-content"></span></button
      >
    </div>
  </nav>
</section>

<button class="fixed bottom-4 right-4 text-4xl lg:hidden z-50" onclick={()=>is_open = !is_open}>
  <span class="i-material-symbols-menu "></span>
</button>

<Modal bind:open={show_add}>
  <AddDashboard onadd={() => (show_add = false)}></AddDashboard>
</Modal>

<Modal bind:open={show_edit_dashboard}>
  <EditDashboard dashboard={dashboard_to_edit!} onremove={()=>show_edit_dashboard = false}></EditDashboard>
</Modal>
<Modal bind:open={show_add_person}>
  <AddAccount dashboard={dashboard_to_edit!} onadd={()=>show_add_person = false}></AddAccount>
 </Modal>
