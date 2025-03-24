<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
import { useCategoriesStore } from '@stores/categories';
import type { Category } from './interfaces';
import { ref } from 'vue';


const props = defineProps<{
    id:string,
}>();

const store = useCategoriesStore();

const category = ref<Category | null>(store.getById(props.id));
</script>

<template>
<main class="flex flex-col">
    <view-header title="Category" subtitle="Show details of the category"></view-header>
    <section v-if="category" class="justify-items-center">
        <form action="" method="post" class="w-full max-w-sm bg-white p-4">
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label for="name" class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                        Name
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input v-model="category.name" id="name" name="name" placeholder="Enter with category name" title="Category name" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500">
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                </div>
                <label for="active" class="md:w-2/3 block text-gray-500 font-bold">
                    <input type="checkbox" v-model="category.active" name="active" id="active" class="mr-2 leading-tight" /> 
                    <span class="text-sm">
                        Active 
                    </span>
                </label>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label for="description" class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                       Description 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <textarea v-model="category.description" id="description" name="description" placeholder="Enter with category description" cols="30" rows="10" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500"></textarea>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3"></div>
                <div class="md:w-2/3 gap-0.5 text-right">
                    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-1 rounded-full">
                        Save
                    </button>
                    <router-link to="/categories" class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 mx-1 rounded-full" title="Cancel and go back to list">
                        Cancel 
                    </router-link>
                    
                </div>
            </div>
        </form>
    </section>
</main>
</template>