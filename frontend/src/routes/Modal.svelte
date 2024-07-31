<script lang="ts">
    import type { Snippet } from "svelte";
    import {scale, fly, fade} from "svelte/transition"
  let { open = $bindable(false), children } = $props<{ open: boolean, children: Snippet }>();
    let isScrolled = $state(false)
    const onscroll = (el: Event)=> isScrolled = (el.target! as HTMLElement).scrollTop != 0 
    const close = () => {open = false; isScrolled = false}
    const onkeydown = (ev: KeyboardEvent)=>{ if (ev.key == "Escape") close() }
</script>
<svelte:window {onkeydown}></svelte:window>

{#if open}
<div
  class="fixed top-0 left-0 z-40 w-[100vw] h-[100vh] backdrop-brightness-50" 
    transition:fade|global
    onclick={close}
></div>
  <div
    class="fixed top-[50%] z-50 left-[50%] bg-base-100 max-h-[90vh] max-w-[min(80vw,800px)]  dark:bg-[#2A2A2A] card card-bordered border-[#3B3B3B] border-2 rounded-xl p-6 pr-7 -translate-x-[50%] -translate-y-[50%] "
      in:scale|global
    out:fly|global={{y:-50}}
  >
    <button class="fixed text-[20px] z-10 top-9 right-9" onclick={close}>
      <span class="i-material-symbols-close"></span>
    </button>
    <div class="overflow-y-scroll p-3 no-scrollbar transition-shadow duration-300 {isScrolled ? 'shadow-[inset_0_4px_8px_rgba(0,0,0,0.6)]' : ''}" {onscroll}>
    {@render children()}
    </div>
  </div>
{/if}
