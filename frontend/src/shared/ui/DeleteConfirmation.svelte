<script lang="ts">
  const { ondelete, oncancel } = $props<{
    ondelete: () => void;
    oncancel: () => void;
  }>();
</script>

<section class="p-3">
  <h1 class="text-2xl dark:text-white text-center font-medium mb-9">
    Are you sure you<br />want to delete?
  </h1>
  <div class="flex gap-3">
    <button class="btn px-20 text-error" onclick={ondelete}>Delete</button>
    <button class="btn px-20" onclick={oncancel}>Cancel</button>
  </div>
</section>
