<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@components/ViewHeader.vue';
import type { Product } from './interfaces';
import { useProductStore } from '@stores/products';


const store = useProductStore();

const products = ref<Array<Product>>(store.products);

</script>

<template>
<main class="flex flex-col">
    <view-header title="Products" subtitle="List of products"></view-header>
    <section>
        <a href="#/products/new" title="Go to form to insert a new one">
            Add New
        </a>
    </section>
    <section class="justify-center">
        <table v-if="products.length > 0" class="border-collapse border border-gray-400 m-5 drop-shadow-md">
            <thead class="bg-gray-200">
                <tr>
                    <th class="p-0.5 border-collapse border border-gray-400">
                        Code
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                       Name 
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                       Description 
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                       Price 
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                       Category 
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                       Actions 
                    </th>
                </tr>
            </thead>
            <tfoot class="bg-gray-200">
                <tr>
                    <td colspan="6" class="py-1 text-center">
                        Total items <strong class="font-semibold">{{ products.length }}</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody class="bg-gray-100">
                <tr v-for="item in products" class="hover:bg-gray-300 h-auto">
                    <td class="p-0.5 border-collapse border border-gray-400">
                        {{ item.code }}
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400">
                        {{ item.name }}
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400">
                        <p v-if="item.description">
                            {{ item.description }}
                        </p>
                        <p v-else class="italic">
                            -- Empty --
                        </p>
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400">
                       {{ item.price }} {{ item.priceCurrency }} 
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400">
                       {{ item.category }} 
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400">
                        <router-link :to="`products/${item.id}`" class="font-medium text-blue-600 dark:text-blue-500 hover:underline" title="Go to details">
                            Details
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-else> 
            <h3 class="text-center text-xl font-mono text-orange-900 line-through">
                There is no items :(
            </h3>
        </div>
    </section>
</main>
</template>