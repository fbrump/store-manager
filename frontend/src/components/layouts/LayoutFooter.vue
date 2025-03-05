<script setup lang="ts">

import { ref } from 'vue';

const currentYear = ref(new Date().getFullYear());

</script>

<template>
<footer class="h-80 bg-gray-700 text-center">
  <p class="m-auto py-2.5 font-medium tracking-wider text-base">
    <em class="italic">"An investment in knowledge pays the best interest."</em> — Benjamin Franklin
  </p>
  <div class="justify-center">
    <hr class="mx-8" />
  </div>
  <p class="my-15 font-semibold">
    © {{ currentYear }} Brum, Inc. All rights reserved.
  </p>
</footer>  
</template>

<style scoped>

</style>
