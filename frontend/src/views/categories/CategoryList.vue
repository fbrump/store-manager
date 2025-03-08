<script setup lang="ts">
import { ref } from 'vue';
import ViewHeader from '../../components/ViewHeader.vue';
import type { Category } from './interfaces';


const categories = ref<Array<Category>>([
    { 
        id: "2856080a-e45d-4362-83e1-a727fbe22247",
        name: "Keyboards",
        active: true
    },
    { 
        id: "2856080a-e45d-4362-83e1-a727fbe22250",
        name: "Mouses",
        active: false
    },
    { 
        id: "2856080a-e45d-4362-83e1-a727fbe22260",
        name: "Chairs",
        active: true
    },
    { 
        id: "2856080a-e45d-4362-83e1-a727fbe22270",
        name: "Monitors",
        description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Suscipit, officiis. Aliquam labore autem odio et, ut fugit enim. Maiores maxime quae expedita dolorum minima facilis ratione enim adipisci amet tempore.",
        active: true
    },
    {
        id: "2856080a-e45d-4362-83e1-a727fbe22280",
        name: "Headset",
        active: false
    },
    { 
        id: "2856080a-e45d-4362-83e1-a727fbe22290",
        name: "Microphones",
        description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Suscipit, officiis. Aliquam labore autem odio et, ut fugit enim. Maiores maxime quae expedita dolorum minima facilis ratione enim adipisci amet tempore.",
        active: true
    },
])

</script>

<template>
<main> 
    <view-header title="Categories" subtitle="List of categories"></view-header>
    <section>
       
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
                        Total of items {{ categories.length }}.
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
                    <td>
                        <input type="checkbox" name="active" :checked="item.active" />
                    </td>
                    <td>
                        <router-link :to="`/categories/${item.id}`">
                            Details
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-else>
            <h3>
                There is no items
            </h3>
        </div>
    </section>
</main>
</template>