// place files you want to import through the `$lib` alias in this folder.

import * as d3 from "d3";
export function generate_pie(data) {
  const width = 500;
  const height = Math.min(width, 500);
  const radius = Math.min(width, height) / 2;

  const arc = d3
    .arc()
    .innerRadius(radius * 0.57)
    .outerRadius(radius - 1);

  const pie = d3
    .pie()
    .padAngle(20 / radius)
    .sort(null)
    .value((d) => d);

  const color = d3
    .scaleOrdinal()
    .domain(data.map((d) => d))
    .range(
      d3
        .quantize((t) => d3.interpolateSpectral(t * 0.8 + 0.1), data.length)
        .reverse(),
    );

  const svg = d3
    .create("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [-width / 2, -height / 2, width, height])
    .attr("style", "max-width: 100%; height: auto;");

  svg
    .append("g")
    .selectAll()
    .data(pie(data))
    .join("path")
    .attr("fill", (d) => color(d.data))
    .attr("d", arc);

  return svg.node();
}
