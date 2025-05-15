<script>
  import { selectedLanguage, selectedCategory} from "$lib/stores.js";
</script>

<nav
  class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 py-4 bg-[#FA8072] shadow-sm"
>
  <!-- Logo can be made with just text and the color -->
  <div class="text-xl font-bold text-[#FFF5F2]">tuna 🐟</div>

  <!-- Dropdown menu -->
  <div class="relative">
    <div class="flex gap-2 items-center">
      <select
        bind:value={$selectedLanguage}
        class="bg-[#FFF5F2] text-[#4B9EA0] border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#4B9EA0]"
      >
        <option value="en" selected>🇺🇸 English</option>
        <option value="es">🇪🇸 Spanish</option>
        <option value="fr">🇫🇷 French</option>
        <option value="de">🇩🇪 German</option>
        <option value="zh">🇨🇳 Chinese</option>
        <option value="kr">🇰🇷 Korean</option>
      </select>
      <select
        bind:value={$selectedCategory}
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
  </div>

  <!-- transition adds that nice hover effect for changing the color on hover -->
  <a
    href="#"
    class="bg-[#4B9EA0] hover:bg-teal-500 text-white px-4 py-2 rounded-lg text-sm font-bold transition-all"
  >
    Try tuna →
  </a>
</nav>
