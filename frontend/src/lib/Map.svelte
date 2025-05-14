<script>
  import { onMount } from "svelte";
  import * as topojson from "topojson-client";
  import { geoPath, geoMercator } from "d3-geo";
  import { draw } from "svelte/transition";
  import { zoom } from "d3-zoom";
  import { select } from "d3-selection";
  import LLMResponse from "$lib/LLMResponse.svelte";

  // Make a set to store the selected countries (id)
  let selectedCountryIds = new Set();

  let llmResponseInstance;

  const width = 900;
  const height = 600;

  const projection = geoMercator()
    .scale(140)
    .translate([width / 2, height / 1.85]);
  const path = geoPath().projection(projection);

  let countries = [];
  let svgRef;
  let gRef;

  let tooltipVisible = false;
  let tooltipContent = "";
  let tooltipX = 0;
  let tooltipY = 0;

  function handleMouseOver(event, feature) {
    tooltipVisible = true;
    tooltipContent = feature.properties.name; // Set content from feature properties

    // Use d3.pointer to get coordinates relative to the SVG
    tooltipX = event.pageX - 40; // Offset tooltip from cursor
    tooltipY = event.pageY - 40;
  }

  function handleMouseMove(event) {
    if (tooltipVisible) {
      tooltipX = event.pageX - 40; // Offset tooltip from cursor
      tooltipY = event.pageY - 40;
    }
  }

  function handleMouseOut() {
    tooltipVisible = false;
  }

  function handleCountryClick(feature) {
    // On country click add the selected country's id (feature.id) to the set, selectedCountryIds
    selectedCountryIds.add(feature.id);
    // Redeclare the selectedCountryIds set to itself in order to force the map color to refresh and change
    // This counts as assigning a new object, which is why it force refreshes
    selectedCountryIds = new Set(selectedCountryIds);

    if (
      llmResponseInstance &&
      typeof llmResponseInstance.openDialog === "function"
    ) {
      llmResponseInstance.openDialog(feature.id, feature.properties.name);
    } else {
      console.error(
        "LLMResponse instance or openDialog method not available in Map.svelte"
      );
    }
  }

  onMount(async () => {
    try {
      const worldmap = await fetch("/countries-110m.json").then((response) =>
        response.json()
      );
      if (worldmap && worldmap.objects && worldmap.objects.countries) {
        countries = topojson.feature(
          worldmap,
          worldmap.objects.countries
        ).features;
      } else {
        throw new Error(
          'Invalid TopoJSON data structure: "objects.countries" not found.'
        );
      }

      const zoomBehavior = zoom()
        .scaleExtent([1, 5]) // Min and max zoom levels
        .on("zoom", (event) => {
          if (gRef) {
            select(gRef).attr("transform", event.transform);
          }
        });

      if (svgRef) {
        select(svgRef).call(zoomBehavior);
      }
    } catch (error) {
      console.error("Error fetching world map data:", error);
    }
  });
</script>

<LLMResponse bind:this={llmResponseInstance} />

<svg
  bind:this={svgRef}
  viewBox="0 0 {width} {height}"
  on:mousemove={handleMouseMove}
  style="background-color: #6e6462;"
>
  <!-- animate and draw borders
   class:selected={selectedCountryIds.has(feature.id)} : When selected, check if selected country's id exists within the set
   and apply the .selected class to the associated countryID (actual css that changes the color).
   
   selected={} applies selected based on the condition (if exists in clicked set)
   so that the selected tag is applied which is then updated to match the tag.
   -->

  <g bind:this={gRef} fill="#FFF5F2" stroke="#2E2E2E">
    {#each countries as feature, i}
      <path
        d={path(feature)}
        on:click={() => handleCountryClick(feature)}
        on:mouseover={(event) => handleMouseOver(event, feature)}
        on:mouseout={handleMouseOut}
        class="country"
        class:selected={selectedCountryIds.has(feature.id)}
        in:draw={{ delay: i * 50, duration: 1000 }}
      />
    {/each}
  </g>
</svg>

{#if tooltipVisible}
  <div
    class="tooltip"
    style="position: absolute; left: {tooltipX}px; top: {tooltipY}px;"
  >
    {tooltipContent}
  </div>
{/if}

<style>
  .country:hover {
    fill: #4b9ea0;
  }

  svg:active {
    cursor: grabbing;
  }

  .tooltip {
    background-color: #2e2e2e; /* Darker background for better contrast */
    color: #fff5f2;
    padding: 6px 12px; /* Slightly more padding */
    border-radius: 5px; /* More rounded corners */
    font-size: 0.875rem; /* Standard small font size */
    pointer-events: none; /* Crucial: allows mouse events to pass through to map */
    white-space: nowrap; /* Keep tooltip content on one line */
    z-index: 1000; /* Ensure it's on top of other elements */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Optional: adds a subtle shadow */
    transition: opacity 0.1s ease-out; /* Optional: smooth fade for visibility */
  }

  /* Update selected country's fill color */
  .country.selected {
    fill: #f4a89d;
  }
</style>
