<script>
  // optional: dropdown logic
</script>

<nav
  class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 py-4 bg-[#FA8072] shadow-sm"
>
  <!-- Logo can be made with just text and the color -->
  <div class="text-xl font-bold text-[#FFF5F2]">tuna</div>

  <!-- Menu -->
  <div class="hidden md:flex gap-6 text-sm text-[#2E2E2E]">
    <div class="relative group">
      <button>Something 1 ▾</button>
      <!-- dropdown could go here -->
    </div>
    <div class="relative group">
      <button>Something 2 ▾</button>
    </div>
    <div class="relative group">
      <button>Something 3 ▾</button>
    </div>
    <div class="relative group">
      <button>Something 4 ▾</button>
    </div>
  </div>

  <!-- CTA Button -->
  <a
    href="#"
    class="bg-[#4B9EA0] hover:bg-teal-500 text-white px-4 py-2 rounded-lg text-sm font-bold transition-all"
  >
    Try tuna →
  </a>
</nav>
