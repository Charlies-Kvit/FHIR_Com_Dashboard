<script lang="ts">
    import { onMount, type Snippet } from "svelte";

  let { title, oncomplete, ondelete, children } = $props<{ title: string, oncomplete: ()=>void, ondelete?: ()=>void, children: Snippet }>();

  let container: HTMLElement;

  onMount(()=>{ container.querySelector('input, select, button')?.focus() })

  const onkeydown = (ev: KeyboardEvent) => {if(ev.key=="Enter") oncomplete()}
</script>
<svelte:window {onkeydown}></svelte:window>
<article class="edit-form">
  <h1 class="dark:text-white mb-9 text-2xl">{title}</h1>
  <div bind:this={container} class="flex flex-col gap-6 min-w-[400px]">
    {@render children()}
    <button class="btn dark:bg-[#5D5D5D]" onclick={oncomplete} 
      >Complete</button
    >
    {#if ondelete}
    <button class="link text-error self-end -mt-4" onclick={ondelete}
      >Delete</button
    >
    {/if}
  </div>
</article>
<style lang="scss">
:global(.edit-form) {
  .input,
  .select {
    @apply dark:bg-[#3D3D3D] p-3;
  }

}
</style>
