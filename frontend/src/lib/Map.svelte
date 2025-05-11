<script>
    import { onMount } from 'svelte';
    import * as topojson from 'topojson-client';
    import { geoPath, geoMercator } from 'd3-geo';
    import { draw } from 'svelte/transition';
    import { zoom } from 'd3-zoom';
    import { select } from 'd3-selection';

    const width = 900;
    const height = 600;

    const projection = geoMercator().scale(140).translate([width/2, height/1.4]);
    const path = geoPath().projection(projection);

    let countries = [];
    let selected;
    let svgRef;
    let gRef;

    let tooltipVisible = false;
    let tooltipContent = '';
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

    function handleFocus(event, feature) {
        tooltipVisible = true;
        tooltipContent = feature.properties.name;

        const targetPath = event.target;
        if (targetPath && typeof targetPath.getBBox === 'function' && svgRef) {
            const bbox = targetPath.getBBox(); // BBox relative to SVG
            const svgRect = svgRef.getBoundingClientRect(); // SVG position relative to viewport

            // Calculate absolute page position for the tooltip
            tooltipX = svgRect.left + window.scrollX + bbox.x + (bbox.width / 2) - 40;
            tooltipY = svgRect.top + window.scrollY + bbox.y + bbox.height - 40 + 5; // Position slightly below the element
        } else {
            // Fallback if we can't get precise coordinates
            tooltipX = event.pageX ? event.pageX - 40 : 50;
            tooltipY = event.pageY ? event.pageY - 40 : 50;
        }
    }


    onMount(async () => {
        try {
            const worldmap = await fetch('/countries-110m.json')
                .then(response => response.json());
            if (worldmap && worldmap.objects && worldmap.objects.countries) {
                countries = topojson.feature(worldmap, worldmap.objects.countries).features;
            } else {
                throw new Error('Invalid TopoJSON data structure: "objects.countries" not found.');
            }

            const zoomBehavior = zoom()
                .scaleExtent([1, 5]) // Min and max zoom levels
                .on('zoom', (event) => {
                    if (gRef) {
                        select(gRef).attr('transform', event.transform);
                    }
                });

            if (svgRef) {
                select(svgRef).call(zoomBehavior);
            }

        } catch (error) {
            console.error('Error fetching world map data:', error);
        }

    });
</script>


<svg bind:this={svgRef} viewBox="0 0 {width} {height}" on:mousemove={handleMouseMove}>
    <!-- animate and draw borders -->
    <g bind:this={gRef} fill="white" stroke="black">
        {#each countries as feature, i}
            <path d={path(feature)}
                  on:click={() => selected = feature}
                  on:mouseover={(event) => handleMouseOver(event, feature)}
                  on:mouseout={handleMouseOut}
                  on:focus={(event) => handleFocus(event, feature)}
                  on:blur={handleMouseOut}
                  class="country"
                  in:draw={{ delay: i * 50, duration: 1000 }} />
        {/each}
    </g>


</svg>

{#if tooltipVisible}
    <div class="tooltip" style="position: absolute; left: {tooltipX}px; top: {tooltipY}px;">
        {tooltipContent}
    </div>
{/if}


<style>
    .country:hover {
        fill: hsl(0 0% 50% / 20%);
    }

    svg:active {
        cursor: grabbing;
    }

    .tooltip {
        background-color: rgba(25, 25, 25, 0.85); /* Darker background for better contrast */
        color: white;
        padding: 6px 12px; /* Slightly more padding */
        border-radius: 5px; /* More rounded corners */
        font-size: 0.875rem; /* Standard small font size */
        pointer-events: none; /* Crucial: allows mouse events to pass through to map */
        white-space: nowrap; /* Keep tooltip content on one line */
        z-index: 1000; /* Ensure it's on top of other elements */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* Optional: adds a subtle shadow */
        transition: opacity 0.1s ease-out; /* Optional: smooth fade for visibility */
    }

</style>