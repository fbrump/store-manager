<script setup lang="ts">
interface HeaderProps {
    title: string
    subtitle?: string
}

defineProps<HeaderProps>()

</script>

<template>
<header>
    <h1>
        {{ title }}
    </h1>
    <h2 v-if="subtitle">
        {{ subtitle }}
    </h2>
</header>
</template>