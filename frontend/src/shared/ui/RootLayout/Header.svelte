<script lang="ts">
  import ThemeToggle from "@/shared/ui/ThemeToggle.svelte";
</script>

<header
  class="px-2 bg-base-300 grid grid-cols-subgrid items-center shadow-xl z-10 row-span-1 col-span-full"
>
  <nav class="navbar py-2 grid col-span-full grid-cols-subgrid">
    <ul class="list-none grid grid-cols-subgrid col-span-full">
      <li>
        <a class="btn btn-link" href="/"><img src="./logo.svg" alt="" /></a>
      </li>
      <li class="col-span-2 px-8"><ThemeToggle></ThemeToggle></li>
      <li class="col-span-2 flex gap-[12px] items-center">
        <div class="grow"></div>
        <!-- <a href="/about">Sign Up</a> -->
        <!-- <a href="/login">Login</a> -->
      </li>
    </ul>
  </nav>
</header>
