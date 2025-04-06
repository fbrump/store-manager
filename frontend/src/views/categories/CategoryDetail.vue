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
        <form action="" method="post">
            <div>
                <div class="md:w-1/3">
                    <label for="name">
                        Name
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="text" v-model="category.name" id="name" name="name" placeholder="Enter with category name" title="Category name" />
                </div>
            </div>
            
            <div> 
                <div class="md:w-1/3">
                    <label for="description">
                       Description 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <textarea v-model="category.description" id="description" name="description" placeholder="Enter with category description" cols="30" rows="10"></textarea>
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                </div>
                <label for="active" class="md:w-2/3">
                    <input type="checkbox" v-model="category.active" name="active" id="active" class="mr-2 leading-tight" /> 
                    <span class="text-sm">
                        Active 
                    </span>
                </label>
            </div>
            <div>
                <div class="md:w-1/3"></div>
                <div class="md:w-2/3 gap-0.5 text-right">
                    <button type="submit">
                        Save
                    </button>
                    <router-link to="/categories" title="Cancel and go back to list">
                        Cancel 
                    </router-link>
                </div>
            </div>
        </form>
    </section>
</main>
</template>