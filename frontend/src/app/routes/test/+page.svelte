<script>
  import { DatePicker } from "@svelte-plugins/datepicker";
  import { format } from "date-fns";

  let startDate = new Date();
  let dateFormat = "MM/dd/yy";
  let isOpen = false;

  const toggleDatePicker = () => (isOpen = !isOpen);

  const formatDate = (dateString) => {
    return (dateString && format(new Date(dateString), dateFormat)) || "";
  };

  let formattedStartDate = formatDate(startDate);

  const onChange = () => {
    startDate = new Date(formattedStartDate);
  };

  $: formattedStartDate = formatDate(startDate);
</script>

<div>
  <DatePicker bind:isOpen bind:startDate theme="dark">
    <input
      type="text"
      placeholder="Select date"
      bind:value={formattedStartDate}
      on:click={toggleDatePicker}
    />
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
    --datepicker-presets-button-background-active: #ff1683;
    --datepicker-presets-button-color: #fff;
    --datepicker-presets-button-color-active: #fff;
    --datepicker-presets-button-color-hover: #333;
    --datepicker-presets-button-color-focus: #333;
  }
</style>
