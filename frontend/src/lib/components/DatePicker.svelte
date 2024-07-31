<script lang="ts">
  import { DatePicker } from "@svelte-plugins/datepicker";
  import { format } from "date-fns";
  import { theme } from "$lib/store.svelte";

  let {
    startDate = $bindable(new Date()),
    dateFormat = "dd.MM.yy",
    isOpen = $bindable(false),
  } = $props<{ startDate: Date; dateFormat: string; isOpen: boolean }>();

  const toggleDatePicker = () => (isOpen = !isOpen);

  const formatDate = (dateString: Date) => {
    return (dateString && format(new Date(dateString), dateFormat)) || "";
  };

  let formattedStartDate = $state(formatDate(startDate));

  $effect(() => {
    formattedStartDate = formatDate(startDate);
  });
</script>

<div>
  <DatePicker bind:isOpen bind:startDate theme={theme.value}>
    <button
      class="dark:bg-[#3D3D3D] px-3 py-2 rounded-xl"
      onclick={toggleDatePicker}
    >
      <span class="i-material-symbols-calendar-month mr-3"></span><span
        class="dark:text-[#9E9E9E]">{formattedStartDate}</span
      ><span class="ml-6 i-material-symbols-chevron-right rotate-90"></span>
    </button>
  </DatePicker>
</div>

<style>
  input[type="text"] {
    border: 1px solid #e8e9ea;
    border-radius: 4px;
    padding: 8px;
  }
  :global(.datepicker[data-picker-theme="dark"]) {
    --datepicker-container-background: oklch(var(--b3));
    --datepicker-container-border: 2px solid oklch(var(--n));
    --datepicker-calendar-today-border: 2px solid oklch(var(--a));
    --datepicker-calendar-header-text-color: oklch(var(--bc));
    --datepicker-calendar-dow-color: oklch(var(--bc));
    --datepicker-calendar-day-color: oklch(var(--bc));
    --datepicker-calendar-day-color-disabled: oklch(var(--er));
    --datepicker-calendar-range-selected-background: var(--bc);

    --datepicker-calendar-header-month-nav-background-hover: oklch(var(--a));
    --datepicker-calendar-header-month-nav-icon-next-filter: invert(100);
    --datepicker-calendar-header-month-nav-icon-prev-filter: invert(100);
    --datepicker-calendar-header-year-nav-icon-next-filter: invert(100);
    --datepicker-calendar-header-year-nav-icon-prev-filter: invert(100);

    --datepicker-calendar-split-border: 4px solid pink;

    --datepicker-presets-border: 1px solid pink;
    --datepicker-presets-button-background-active: oklch(var(--a));
    --datepicker-presets-button-color: #fff;
    --datepicker-presets-button-color-active: #fff;
    --datepicker-presets-button-color-hover: #333;
    --datepicker-presets-button-color-focus: #333;
  }
</style>
