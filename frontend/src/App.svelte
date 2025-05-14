<script>
  import "./app.css";
  import Map from "./lib/Map.svelte";
  import Navbar from "./lib/Navbar.svelte";

  import { fade } from "svelte/transition";

  // Splash screen that only loads the map when button is pressed
  let showMap = false;
  function handleEnterClick() {
    showMap = true;
  }
</script>

<svelte:head>
  <link rel="icon" type="image/svg+xml" href="/fish.svg" />
</svelte:head>

<main>
  {#if showMap}
    <div transition:fade={{ duration: 600 }}>
      <Navbar />

      <div class="map">
        <Map />
      </div>
    </div>
  {:else}
    <section class="home-screen" transition:fade={{ duration: 600 }}>
      <div>
        <h1 class="text-4xl font-bold text-[#FA8072]">Welcome to tuna 🐟</h1>

        <p class="text-lg mt-4 font-semibold text-gray-600">
          Current trends around the world, canned
        </p>

        <div class="flex justify-center mt-8">
          <button
            on:click={handleEnterClick}
            class="bg-[#4B9EA0] hover:bg-teal-500 text-white px-6 py-3 rounded-lg text-lg font-bold transition-all transform hover:scale-105"
          >
            Try tuna →
          </button>
        </div>
      </div>
    </section>
  {/if}
</main>

<!-- CSS for home screen -->
<style>
  .home-screen {
    background-color: #fff5f2;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
</style>
