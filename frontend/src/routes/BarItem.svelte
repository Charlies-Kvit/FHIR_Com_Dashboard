<script lang="ts">
  import { sineIn, sineInOut, sineOut } from "svelte/easing";
  import { tweened, type Tweened } from "svelte/motion";

  let { x, y, width, height, r, color, percent, title, is_active, onclick } =
    $props<{
      x: number;
      y: number;
      width: number;
      height: number;
      r: number;
      color: string;
      percent: number;
      title: string;
      is_active: boolean;
      onclick: () => void;
    }>();
  const options = { easing: sineOut, duration: 1000 };
  let animated_width = tweened(r, options);
  let animated_percent = tweened(0, options);
  $effect(() => {
    animated_width.set(width);
    animated_percent.set(percent);
  });
  const boundary = 10;
  const offset = 20;
</script>

<path
  fill={color}
  d="M{x},{y}
    h{$animated_width - r / 2}
    q{r},0 {r},{r}
    v{height - 2 * r}
    q0,{r} {-r},{r}
    h{-($animated_width - r / 2)}
    z
    "
/>
<text x={x + 12} y={y + 36} class="fill-current">{title}</text>
<text
  x={Math.max($animated_width + 20, boundary)}
  y={y + height / 2}
  class="text-[{height}] font-extrabold font-mono dark:fill-white"
  dominant-baseline="middle">{Math.round($animated_percent)}%</text
>
<rect
  role="button"
  tabindex="0"
  {onclick}
  {x}
  y={y - offset / 2}
  width={300 - x}
  height={height + offset * 1.5}
  class="fill-transparent opacity-5 hover:fill-accent hover:opacity-25 transition-all {is_active
    ? 'fill-accent opacity-15'
    : ''}"
></rect>
