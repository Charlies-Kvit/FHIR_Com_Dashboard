<script lang="ts">
  import { onMount, type Snippet } from "svelte";
  import Modal from "./Modal.svelte";
  import DeleteConfirmation from "./DeleteConfirmation.svelte";

  let { title, oncomplete, ondelete, children } = $props<{
    title: string;
    oncomplete: () => void;
    ondelete?: () => void;
    children: Snippet;
  }>();

  let delete_prompt = $state(false);
  let container: HTMLElement;

  onMount(() => {
    (
      container.querySelector("input, select, button") as HTMLInputElement
    ).focus();
  });

  const onkeydown = (ev: KeyboardEvent) => {
    if (ev.key == "Enter") oncomplete();
  };
</script>

<svelte:window {onkeydown} />
<article class="edit-form">
  <h1 class="dark:text-white mb-9 text-2xl">{title}</h1>
  <div bind:this={container} class="flex flex-col gap-6 min-w-[400px]">
    {@render children()}
    <button class="btn dark:bg-[#5D5D5D]" onclick={oncomplete}>Complete</button>
    {#if ondelete}
      <button
        class="link text-error self-end -mt-4"
        onclick={() => (delete_prompt = true)}>Delete</button
      >
    {/if}
  </div>
</article>
{#if ondelete}
  <Modal bind:open={delete_prompt} custom_close={true}>
    <DeleteConfirmation {ondelete} oncancel={() => (delete_prompt = false)}
    ></DeleteConfirmation>
  </Modal>
{/if}

<style lang="scss">
  :global(.edit-form) {
    :global(.input),
    :global(.select) {
      @apply dark:bg-[#3D3D3D] p-3;
    }
  }
</style>
