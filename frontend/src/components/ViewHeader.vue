<script setup lang="ts">
interface HeaderProps {
    title: string
    subtitle?: string
}

defineProps<HeaderProps>()

</script>

<template>
<header class="flex flex-col text-center">
    <h1 class="text-2xl">
        {{ title }}
    </h1>
    <h2 v-if="subtitle" class="text-lg">
        {{ subtitle }}
    </h2>
</header>
</template>