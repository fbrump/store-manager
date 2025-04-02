<script setup lang="ts">
import LayoutFooter from './layouts/LayoutFooter.vue';
import LayoutNav from './layouts/LayoutNav.vue';

</script>

<template>
  <div class="flex flex-col h-screen justify-between bg-amber-50">
    <layout-nav v-once></layout-nav>
    <section>
      <router-view></router-view>
    </section>
    <layout-footer v-once class="sticky bottom-0 w-full mt-auto"></layout-footer>
  </div>
</template>

<style scoped>

</style>
