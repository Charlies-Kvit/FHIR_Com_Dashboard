<script lang="ts">
  import { dashboards, selected_dashboard } from "$lib/store.svelte";
  import Modal from "./Modal.svelte";
  import AddDashboard from "./AddDashboard.svelte";
  import AddPerson from "./AddPerson.svelte";
  import EditDashboard from "./EditDashboard.svelte";

  let show_add = $state(false);
  let show_edit_dashboard = $state(false);
  let dashboard_to_edit = null;
  let show_add_person = $state(false);
  let innerWidth = $state(0)
  let is_open = $state(undefined)
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
    <ul class="list-none flex flex-col gap-6">
      {#each dashboards.value as dashboard, i (dashboard.id)}
        <li class="flex items-center gap-2 border-b pb-6 border-[#313131]">
          <button
            class={dashboard == selected_dashboard.value
              ? "font-bold dark:font-normal dark:text-white"
              : ""}
            onclick={() => selected_dashboard.select(dashboard)}
            >{dashboard.name}</button
          >
        <div class="grow"></div>
          <button
            class="h-min"
            onclick={() => {
              dashboard_to_edit = dashboard;
              show_edit_dashboard = true;
            }}><span class="block i-material-symbols-settings text-xl text-[#5D5D5D]"></span></button
          >
          <button class="h-min rounded-full bg-[#5D5D5D]" onclick={()=>{
              dashboard_to_edit = dashboard;
              show_add_person = true;
          }}
            ><span class="block i-material-symbols-add text-xl text-[#D9D9D9] "></span></button
          >
        </li>
      {/each}
    </ul>
    <div class="grow"></div>
    <div>
      <button class="rounded-full bg-[#5D5D5D]" onclick={() => (show_add = true)}
        ><span class="block i-material-symbols-add text-[32px]"></span></button
      >
    </div>
  </nav>
</section>

<button class="fixed bottom-4 right-4 text-4xl md:hidden z-50" onclick={()=>is_open = !is_open}>
  <span class="i-material-symbols-menu "></span>
</button>

<Modal bind:open={show_add}>
  <AddDashboard onadd={() => (show_add = false)}></AddDashboard>
</Modal>

<Modal bind:open={show_edit_dashboard}>
  <EditDashboard dashboard={dashboard_to_edit!} onremove={()=>show_edit_dashboard = false}></EditDashboard>
</Modal>
<Modal bind:open={show_add_person}>
  <AddPerson dashboard={dashboard_to_edit!} onadd={()=>show_add_person = false}></AddPerson>
 </Modal>
