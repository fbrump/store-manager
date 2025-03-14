<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
import { useCategoriesStore } from '../../stores/categorie';
import { ref } from 'vue';
import type { Category } from './interfaces';

const props = defineProps<{
    id:string,
}>();

const store = useCategoriesStore();

let category = ref<Category | null>(store.getById(props.id));

</script>

<template>
<main class="justify-items-center">
    <view-header title="Category" subtitle="Show details of the category"></view-header>
    <section v-if="category">
        {{ category }}
        <form action="" method="post">
            <div>
                <label for="name">
                    Name
                </label>
                <input type="text" name="name" id="name" title="Category name" :module="category.name" :value="category?.name" @input="e => category?.name" />
            </div>
            <div>
                <label for="active">Active</label>
                <input type="checkbox" name="active" id="active" :model="category?.active" :checked="category.active" />
            </div>
            <div>
                <label for="description">
                    Description
                </label>
                <textarea name="description" id="description" cols="30" rows="10" :model="category?.description">
                </textarea>
            </div>
            <button type="submit">
                Save
            </button>
        </form>
    </section>
</main>
</template>