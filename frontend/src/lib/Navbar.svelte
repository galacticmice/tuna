<script>
  // Initialize the empty category variable
  let selectedCategory = "";

  // Function is defined. Srt to async, so that it can await a response from backend with code
  async function sendCategory() {
    // If the function is empty then return, so the rest of the function does not send an empty message
    if (!selectedCategory) return;

    // Calls the backend at /set-category to send a POST request (lets data be sent to the backend)
    const response = await fetch("http://localhost:8080/set-category", {
      method: "POST",
      // The header lets the backend know this will be a JSON message
      headers: {
        "Content-Type": "application/json",
      },

      // Send the selected category as a JSON object
      // selectedCategory is within the <select> tag which receives the value (what was selected)
      // Important to note we store the selectedCategory value in the "category" tag of the JSON object (will be parsed on app.py)
      body: JSON.stringify({ category: selectedCategory }),
    });

    // Wait for the server to respond and save its nessage to result
    const result = await response.json();
    // The log sends a message to the console on the browser so we can see what went through
    console.log("Server response:", result);
  }
</script>

<nav
  class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 py-4 bg-[#FA8072] shadow-sm"
>
  <!-- Logo can be made with just text and the color -->
  <div class="text-xl font-bold text-[#FFF5F2]">tuna 🐟</div>

  <!-- Dropdown menu -->
  <div class="relative">
    <select
      bind:value={selectedCategory}
      on:change={sendCategory}
      class="bg-[#FFF5F2] text-[#4B9EA0] border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#4B9EA0]"
    >
      <option disabled selected>Select an option</option>
      <option>🚗 Autos and Vehicles</option>
      <option>💄 Beauty and Fashion</option>
      <option>👔 Business and Finance</option>
      <option>⛅ Climate</option>
      <option>🍿 Entertainment</option>
      <option>🍽️ Food and Drink</option>
      <option>🎮 Games</option>
      <option>💉 Health</option>
      <option>🪷 Hobbies and Leisure</option>
      <option>🏫 Jobs and Education</option>
      <option>🧑‍⚖️ Law and Government</option>
      <option>👾 Other</option>
      <option>🐕 Pets and Animals</option>
      <option>💀 Politics</option>
      <option>⚛️ Science</option>
      <option>🛍️ Shopping</option>
      <option>⚽ Sports</option>
      <option>💻 Technology</option>
      <option>✈️ Travel and Transportation</option>
    </select>
  </div>

  <!-- transition adds that nice hover effect for changing the color on hover -->
  <a
    href="#"
    class="bg-[#4B9EA0] hover:bg-teal-500 text-white px-4 py-2 rounded-lg text-sm font-bold transition-all"
  >
    Try tuna →
  </a>
</nav>
