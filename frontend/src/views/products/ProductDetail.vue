<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
import { useProductStore } from '@stores/products';
import { ref } from 'vue';
import type { Product } from './interfaces';

const props = defineProps<{
    id:string,
}>();

const store = useProductStore();

const product = ref<Product | null>(store.getById(props.id));

</script>

<template>
<main class="justify-items-center">
    <view-header title="Product Details" subtitle="Show details of the product"/>
    <section>
        {{ props.id }}
        <br />
        {{ product }}
        <br />
        <form action="" method="post">
            <div>
                <label for="code">
                    SKU
                </label>
                <input type="text" name="code" id="code" :value="product?.code" title="Product code" />
            </div>
            <div>
                <label for="name">
                    Name
                </label>
                <input type="text" name="name" id="name" :value="product?.name" title="Product name" />
            </div>
            <div>
                <label for="price">
                   Price 
                </label>
                <input type="number" name="price" id="price" :value="product?.price" title="Product price" />
            </div>
            <div>
                <label for="currency">
                   Currency
                </label>
                <select name="currency" id="currency" :value="product?.code" title="Product price currency">
                    <option value="EUR">Euro</option>
                    <option value="USD">Dollar USA</option>
                </select>
            </div>
            <div>
                <label for="active">Active</label>
                <input type="checkbox" name="active" id="active" :checked="product?.active" />
            </div>
            <div>
                <label for="description">
                    Description
                </label>
                <textarea name="description" id="description" :value="product?.description" cols="30" rows="10">
                </textarea>
            </div>
            <button type="submit" title="Click to save">
                Save
            </button>
        </form>
    </section>
</main>
</template>