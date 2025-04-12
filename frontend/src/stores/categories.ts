import { defineStore } from "pinia";
import { computed, ref } from "vue";
import type { Category } from "../views/categories/interfaces";

export const useCategoriesStore = defineStore('categories', () => {
    /// state
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
    ]);

    // getter
    const getAll = computed((): Array<Category> => categories.value);

    // actions
    const getById = (id: string): Category | null => {
        var data: Array<Category> = categories.value.filter((item: Category) => item.id == id);
        return data === undefined ? null : data[0];
    };

    // output
    return {
        categories,
        getAll,
        getById
    }
});