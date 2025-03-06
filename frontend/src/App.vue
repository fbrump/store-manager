<script setup lang="ts">
import LayoutFooter from './layouts/LayoutFooter.vue';
import LayoutNav from './layouts/LayoutNav.vue';

</script>

<template>
  <layout-nav></layout-nav>
  <section class="h-dvh bg-amber-50">
    <router-view></router-view>
  </section>
  <layout-footer v-once></layout-footer>
</template>

<style scoped>

</style>
