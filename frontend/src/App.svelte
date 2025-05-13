<script>
  import './app.css';
  import Map from './lib/Map.svelte';
  import Navbar from './lib/Navbar.svelte';
</script>

<svelte:head>
  <link rel="icon" type="image/svg+xml" href="/fish.svg" />
</svelte:head>

<main>
  <Navbar />
  <div class="map">
    <Map />
  </div>

  <p></p>
</main>
