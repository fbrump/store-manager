<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
import SelectIcon from '@components/SelectIcon.vue';
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
<main class="flex flex-col">
    <view-header title="Product Details" subtitle="Show details of the product"/>
    <section class="justify-items-center">
        <form v-if="product" action="" method="post">
            <div>
                <div class="md:w-1/3">
                    <label for="code">
                       SKU 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="text" v-model="product.code" id="code" name="code" placeholder="Enter with SKU" title="SKU Code" />
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="name">
                        Name 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="text" v-model="product.name" id="name" name="name" placeholder="Enter with name" title="Name" >
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="price">
                        Price
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="number" v-model="product.price" id="price" name="price" placeholder="Enter with price" title="Price" />
                    <div class="relative">
                        <select v-model="product.priceCurrency" name="currency" id="currency" title="Product price currency"> 
                            <option value="EUR">Euro</option>
                            <option value="USD">Dollar USA</option>
                        </select>
                        <select-icon></select-icon>
                    </div>
                </div>
            </div>
            <div>
                <div class="md:w-1/3"></div>
                <label class="md:w-2/3 block text-gray-500 font-bold">
                    <input  type="checkbox" name="active" id="active" v-model="product.active" />
                    <span class="text-sm">
                        Active
                    </span>
                </label>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="description">
                      Description 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <textarea v-model="product.description" id="description" name="description" placeholder="Enter with description" title="Description" cols="30" rows="10"></textarea>
                </div>
            </div>
            <div>
                <div class="md:w-1/3"></div>
                <div class="md:w-2/3 gap-0.5 text-right">
                    <button type="submit">
                        Save
                    </button>
                    <router-link to="/products" title="Cancel and go back to list">
                        Cancel 
                    </router-link>
                </div>
            </div>
        </form>
    </section>
</main>
</template>