<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@components/ViewHeader.vue';
import TableEmpty from '@components/TableEmpty.vue';
import type { Product } from './interfaces';
import { useProductStore } from '@stores/products';


const store = useProductStore();

const products = ref<Array<Product>>(store.getAll);

</script>

<template>
<main class="flex flex-col gap-1.5">
    <view-header title="Products" subtitle="List of products"></view-header>
    <section class="justify-items-center">
        <div class="md:container gap-1 text-right">
            <router-link to="/products/new" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" title="Go to form to insert a new one">
                Add New
            </router-link>
        </div>
        <table v-if="products.length > 0">
            <thead>
                <tr>
                    <th>
                        Code
                    </th>
                    <th>
                       Name 
                    </th>
                    <th>
                       Description 
                    </th>
                    <th class="w-24">
                       Price 
                    </th>
                    <th>
                       Category 
                    </th>
                    <th>
                       Actions 
                    </th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="6">
                        Total items <strong class="font-semibold">{{ products.length }}</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody>
                <tr v-for="item in products">
                    <td>
                        <code>
                        {{ item.code }}
                        </code>
                    </td>
                    <td>
                        {{ item.name }}
                    </td>
                    <td>
                        <p v-if="item.description">
                            {{ item.description }}
                        </p>
                        <p v-else class="italic">
                            -- Empty --
                        </p>
                    </td>
                    <td class="w-24 text-center">
                       {{ item.price }} {{ item.priceCurrency }} 
                    </td>
                    <td>
                       {{ item.category }} 
                    </td>
                    <td class="text-center">
                        <router-link :to="`products/${item.id}`" title="Go to details">
                            Details
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <table-empty v-else></table-empty>
    </section>
</main>
</template>