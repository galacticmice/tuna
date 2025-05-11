<script>
  import "./app.css";
  import LLMResponse from "./lib/LLMResponse.svelte";
  import Map from "./lib/Map.svelte";
</script>

<main>

  <div class="map">
    <!-- Uncomment the line below to include the LLMResponse component -->
<!--    <LLMResponse />-->
    <Map />
    <LLMResponse />
  </div>

  <p>

  </p>
</main>
