<script lang="ts">
  import * as d3 from "d3";
  import type { Summary } from "@/entities/account";
  import BarItem from "./BarItem.svelte";

  let { data, selected = $bindable(undefined) } = $props<{
    data: Summary[];
    selected: undefined | number;
  }>();

  let width = 300;
  let height = 300;
  let margin = 5;

  const xScale = d3
    .scaleLinear()
    .range([margin, width - margin - 50])
    .domain([0, Math.max(...data.map((v: Summary) => v.account_post_count))]);

  const yScale = d3
    .scaleBand()
    .range([margin, height - margin])
    .domain(data.map((v: Summary) => v.id))
    .padding(0.2);

  const color = d3
    .scaleOrdinal()
    .range(["#5388D8", "#F4BE37", "#FF9F40", "#543EDC", "#FF4B40"]);
  const bar_item_size = 20;
  let sum_count_posts = data
    .map((v: Summary) => v.account_post_count)
    .reduce((previous: number, current: number) => previous + current, 0);
</script>

<svg viewBox="0 0 {width} {height}" class="overflow-hidden">
  <line
    x1="0"
    y1="5"
    x2="0"
    y2={height - 5}
    stroke-width="10"
    class="stroke-gray-300 dark:stroke-neutral"
    stroke-linecap="round"
  ></line>
  <g>
    {#each data as d, i}
      {@const y =
        (yScale(d.id) as number) + (yScale.bandwidth() - bar_item_size) / 2}
      {@const width = xScale(d.account_post_count) - margin}
      <BarItem
        x={margin}
        {y}
        {width}
        height={bar_item_size}
        r={bar_item_size / 2}
        color={color(String(i)) as string}
        percent={(d.account_post_count / sum_count_posts) * 100}
        title={d.title}
        is_active={i == selected}
        onclick={() => (selected = i)}
      ></BarItem>
    {/each}
  </g>
</svg>
