<script setup lang="ts">
</script>

<template>
<nav class="h-14 text-center bg-gray-700 text-white font-semibold">
    <ul class="flex flex-row justify-center content-center">
        <li class="mx-2">
            <router-link to="/" title="Go to dashboard">
                Dashboard
            </router-link>
        </li>
        <li class="mx-2">
            <router-link to="/transactions" title="Go to transactions">
             Transactions   
            </router-link>
        </li>
        <li class="mx-2">
            <router-link to="/products" title="Go to products">
                Products
            </router-link>
        </li>
        <li class="mx-2">
            <router-link to="/categories" title="Go to categories">
                Categories
            </router-link>
        </li>
        <li class="mx-2">
            <router-link to="/login" title="Go to login">
                Login
            </router-link>
        </li>
    </ul>
</nav>
</template>