<script>
  // Initialize selectedCategory to "0" (Default Category)
  let selectedCategory = "0";

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
      body: JSON.stringify({ categoryID: selectedCategory }),
    });

    // Wait for the server to respond and save its nessage to result
    const result = await response.json();
    // The log sends a message to the console on the browser so we can see what went through
    console.log("Server response:", result);
  }
  // Call sendCategory on page load
  sendCategory();
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
      <option value="0" selected>📁 Default Category</option>
      <option value="1">🚗 Autos and Vehicles</option>
      <option value="2">💄 Beauty and Fashion</option>
      <option value="3">👔 Business and Finance</option>
      <option value="20">⛅ Climate</option>
      <option value="4">🍿 Entertainment</option>
      <option value="5">🍽️ Food and Drink</option>
      <option value="6">🎮 Games</option>
      <option value="7">💉 Health</option>
      <option value="8">🪷 Hobbies and Leisure</option>
      <option value="9">🏫 Jobs and Education</option>
      <option value="10">🧑‍⚖️ Law and Government</option>
      <option value="11">👾 Other</option>
      <option value="13">🐕 Pets and Animals</option>
      <option value="14">💀 Politics</option>
      <option value="15">⚛️ Science</option>
      <option value="16">🛍️ Shopping</option>
      <option value="17">⚽ Sports</option>
      <option value="18">💻 Technology</option>
      <option value="19">✈️ Travel and Transportation</option>
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
