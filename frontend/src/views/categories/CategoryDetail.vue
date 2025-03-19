<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@components/ViewHeader.vue';
import { useCategoriesStore } from '@stores/categorie';
import type { Category } from './interfaces';

const props = defineProps<{
    id:string,
}>();

const store = useCategoriesStore();

const category = ref<Category | null>(store.getById(props.id));

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
                <input type="text" name="name" id="name" title="Category name" :value="category?.name" />
            </div>
            <div>
                <label for="active">Active</label>
                <input type="checkbox" name="active" id="active" :checked="category?.active" />
            </div>
            <div>
                <label for="description">
                    Description
                </label>
                <textarea name="description" id="description" cols="30" rows="10" :value="category?.description" >
                </textarea>
            </div>
            <button type="submit">
                Save
            </button>
        </form>
    </section>
</main>
</template>