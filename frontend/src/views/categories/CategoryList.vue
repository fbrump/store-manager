<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@components/ViewHeader.vue';
import type { Category } from './interfaces';
import { useCategoriesStore } from '@stores/categories';


const store = useCategoriesStore();

const categories = ref<Array<Category>>(store.getAll);

</script>

<template>
<main class="flex flex-col">
    <view-header title="Categories" subtitle="List of categories"></view-header>
    <section class="justify-items-center">
        <table v-if="categories.length > 0" class="border-collapse border border-gray-400 m-5 drop-shadow-md">
            <thead class="bg-gray-200">
                <tr>
                    <th class="p-0.5 border-collapse border border-gray-400">
                        Name
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                        Description
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                        Active
                    </th>
                    <th class="p-0.5 border-collapse border border-gray-400">
                        Actions
                    </th>
                </tr>
            </thead>
            <tfoot class="bg-gray-200">
                <tr>
                    <td colspan="4" class="py-1 text-center">
                        Total of items <strong class="font-semibold">{{ categories.length }}</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody class="bg-gray-100">
                <tr v-for="item in categories" :key="item.id" class="hover:bg-gray-300 h-auto">
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
                    <td class="p-0.5 border-collapse border border-gray-400 text-center">
                        <input type="checkbox" name="active" :checked="item.active" />
                    </td>
                    <td class="p-0.5 border-collapse border border-gray-400 text-center">
                        <router-link :to="`/categories/${item.id}`" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">
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