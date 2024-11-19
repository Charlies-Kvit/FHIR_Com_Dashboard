<script lang="ts">
  import { theme } from "@/shared/store";
</script>

<label class="swap swap-rotate">
  <input type="checkbox" checked={$theme == "light"} onclick={theme.toggle} />
  <span class="swap-off h-10 w-10 i-material-symbols-light-mode"></span>
  <span class="swap-on h-10 w-10 i-material-symbols-dark-mode"></span>
</label>
