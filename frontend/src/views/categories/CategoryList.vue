<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@components/ViewHeader.vue';
import TableEmpty from '@components/TableEmpty.vue';
import type { Category } from './interfaces';
import { useCategoriesStore } from '@stores/categories';


const store = useCategoriesStore();

const categories = ref<Array<Category>>(store.getAll);

</script>

<template>
<main class="flex flex-col">
    <view-header title="Categories" subtitle="List of categories"></view-header>
    <section class="justify-items-center">
        <table v-if="categories.length > 0">
            <thead>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        Description
                    </th>
                    <th>
                        Active
                    </th>
                    <th>
                        Actions
                    </th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="4">
                        Total of items <strong class="font-semibold">{{ categories.length }}</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody>
                <tr v-for="item in categories" :key="item.id">
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
                    <td class="text-center">
                        <input type="checkbox" name="active" :checked="item.active" />
                    </td>
                    <td class="text-center">
                        <router-link :to="`/categories/${item.id}`" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">
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