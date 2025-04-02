<script setup lang="ts">
import { ref } from 'vue';
import ViewHeader from '@components/ViewHeader.vue';
import TableEmpty from '@components/TableEmpty.vue';
import type { Transaction } from './interfaces';
import { useTransactionsStore  } from '@stores/transactions';


const store = useTransactionsStore();

const transactions = ref<Array<Transaction>>(store.getAll);

</script>

<template>
<main class="flex flex-col gap-1.5">
    <view-header title="Transactions" subtitle="List of transactions"></view-header>
    <section class="flex flex-col">
        <div class="md:container gap-1 text-right">
            <router-link to="/transactions/new" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" title="Go to form to insert a new one">
                Add New
            </router-link>
        </div>
        <table v-if="transactions.length > 0">
            <thead>
                <tr>
                    <th>
                        Code 
                    </th>
                    <th>
                        Product
                    </th>
                    <th>
                        Category
                    </th>
                    <th>
                        User
                    </th>
                    <th>
                        Type
                    </th>
                    <th>
                        Amount
                    </th>
                    <th>
                        Actions 
                    </th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="7">
                        Total items <strong class="font-semibold">{{ transactions.length }}</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody>
                <tr v-for="item in transactions">
                    <td>
                        <code>
                        {{ item.id }}
                        </code>
                    </td>
                    <td>
                        {{ item.product }}
                    </td>
                    <td>
                        {{ item.category }}
                    </td>
                    <td>
                        {{ item.user }}
                    </td>
                    <td class="text-center">
                        {{ item.type }}
                    </td>
                    <td class="text-center">
                        {{ item.amount }}
                    </td>
                    <td class="text-center">
                        <router-link :to="`transactions/${ item.id }`">
                            Details
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <table-empty v-else></table-empty>
    </section>
</main>
</template>