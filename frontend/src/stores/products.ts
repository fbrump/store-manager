import { defineStore } from "pinia";
import { computed, ref } from "vue";
import type { Product } from "@views/products/interfaces";


export const useProductStore = defineStore('product', () => {
    /// state
    const products = ref<Array<Product>>([
        {
            id: "b11cc280-ebe2-4f21-b85a-3f33569f9b9c",
            code: 'SKU001',
            name: 'Corne V3',
            price: 250.00,
            priceCurrency: 'EUR',
            category: 'Keyboards',
            active: true
        },
        {
            id: "b11cc280-ebe2-4f21-b85a-3f33569f9b8c",
            code: 'SKU003',
            name: 'Corne V4 Choc',
            description: 'The Corne keyboard is a split keyboard with 3x6/3x5 column staggered keys and 3 thumb keys.',
            price: 150.00,
            priceCurrency: 'EUR',
            category: 'Keyboards',
            active: true
        },
        {
            id: "b11cc280-ebe2-4f21-b85a-3f33569f9b7c",
            code: 'SKU002',
            name: 'Logitech M185 Wireless Mouse',
            description: 'Compact Mouse: With a comfortable and contoured shape, this Logitech ambidextrous wireless mouse feels great in either right or left hand and is far superior to a touchpad',
            price: 50.00,
            priceCurrency: 'EUR',
            category: 'Mouse',
            active: true
        },
    ]);

    // getter
    const getAll = computed((): Array<Product> => products.value);

    // actions
    const getById = (id: string): Product | null => {
        var data: Array<Product> = products.value.filter(item => item.id == id);
        return data === undefined ? null : data[0];
    };

    // output
    return {
        products,
        getAll,
        getById,
    }
});