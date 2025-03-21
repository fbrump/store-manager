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
<main class="flex flex-col">
    <view-header title="Product Details" subtitle="Show details of the product"/>
    <section class="justify-items-center">
        {{ product }}
        <br />
        <form action="" method="post" class="w-full max-w-sm bg-white p-4">
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label for="code" class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                       SKU 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input v-model="product.code" id="code" name="code" placeholder="Enter with SKU" title="SKU Code" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500" />
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label for="name" class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                        Name 
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input v-model="product.name" id="name" name="name" placeholder="Enter with name" title="Name" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500">
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label for="price" class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
                        Price
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input v-model="product.price" id="price" name="price" placeholder="Enter with price" title="Price" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded max-w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500">
                    <div class="relative">
                        <select v-model="product.priceCurrency" name="currency" id="currency" title="Product price currency" class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"> 
                                <option value="EUR">Euro</option>
                                <option value="USD">Dollar USA</option>
                        </select>
                        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3"></div>
                <label class="md:w-2/3 block text-gray-500 font-bold">
                <input  type="checkbox" name="active" id="active" v-model="product.active" class="mr-2 leading-tight" />
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
                    <textarea v-model="product.description" id="description" name="description" placeholder="Enter with description" title="Description" cols="30" rows="10" class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500"></textarea>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3"></div>
                <div class="md:w-2/3 gap-0.5 text-right">
                    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-1 rounded-full">
                        Save
                    </button>
                    <router-link to="/products" class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 mx-1 rounded-full" title="Cancel and go back to list">
                        Cancel 
                    </router-link>
                    
                </div>
            </div>
        </form>
    </section>
</main>
</template>