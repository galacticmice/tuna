<script>
  import "./app.css";
  import Map from "./lib/Map.svelte";
  import Navbar from "./lib/Navbar.svelte";

  import { fade } from "svelte/transition";

  // Splash screen that only loads the map when button is pressed
  let showMap = false;
  let animateTransition = false;

  // function to call the animation div
  function handleEnterClick() {
    animateTransition = true;

    setTimeout(() => {
      showMap = true;
    }, 1000);
  }
</script>

<svelte:head>
  <link rel="icon" type="image/svg+xml" href="/fish.svg" />
</svelte:head>

<main>
  <!-- Animation condition stuff -->
  {#if animateTransition}
    <div class="page-transition"></div>
  {/if}
  <!-- Actually showing the main page -->
  {#if animateTransition}
    <div transition:fade={{ delay: 150, duration: 600 }}>
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

<style>
  .home-screen {
    background-color: #fff5f2;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .page-transition {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background-color: #4b9ea0;
    border-radius: 50%;
    z-index: 50;
    transform: translate(-50%, -50%);
    animation: circleExpand 1.5s ease forwards;
  }

  @keyframes circleExpand {
    0% {
      width: 0;
      height: 0;
      opacity: 1;
    }
    50% {
      width: 300vw;
      height: 300vw;
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
</style>
