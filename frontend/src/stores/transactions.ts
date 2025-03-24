import { defineStore } from "pinia";
import { computed, ref } from "vue";
import type { Transaction } from "@views/transactions/interfaces";

export const useTransactionsStore = defineStore('transactions', () => {
    /// state
    const transactions = ref<Array<Transaction>>([{
            id: 'e12be4c6-bdcb-46ae-bf4b-f6e9e404b759',
            type: 'In',
            amount: 5,
            product: 'T-Shirt Nike',
            category: 'Clothing',
            active: true
        },
    ]);

    // getter
    const getAll = computed((): Array<Transaction> => transactions.value);

    // actions
    const getById = (id: string): Transaction | null => {
        var data: Array<Transaction> = transactions.value.filter(item => item.id == id);
        return data === undefined ? null : data[0];
    };

    // output
    return {
        transactions,
        getAll,
        getById
    }
});