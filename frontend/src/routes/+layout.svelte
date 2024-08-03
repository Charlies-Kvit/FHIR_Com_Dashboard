<script>
  import "../styles.scss";
  import "animate.css";
  import Header from "./Header.svelte";
  import LeftPanel from "./LeftPanel.svelte";
</script>

<Header></Header>
<LeftPanel></LeftPanel>
<main
  class="row-span-15 col-span-4 mx-6 mt-8 grid grid-cols-subgrid auto-rows-min overflow-y-scroll"
>
  <slot />
</main>

<style lang="scss" global>
  :global(body) {
    @apply grid grid-rows-[repeat(16,1fr)] grid-cols-[0_repeat(4,1fr)] lg:grid-cols-[20%_repeat(4,1fr)] h-[100vh] transition-all;
  }
</style>
