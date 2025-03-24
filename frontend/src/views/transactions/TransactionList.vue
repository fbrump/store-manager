<script setup lang="ts">
import { ref } from 'vue';
import ViewHeader from '@components/ViewHeader.vue';
import type { Transaction } from './interfaces';
import { useTransactionsStore  } from '@stores/transactions';


const store = useTransactionsStore();

const transactions = ref<Array<Transaction>>(store.getAll);

</script>

<template>
<main>
    <view-header title="Transactions" subtitle="List of transactions"></view-header>
    <section>
        <div>
        </div>
        <table v-if="transactions">
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
                        {{ item.id }}
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
                    <td>
                        {{ item.type }}
                    </td>
                    <td>
                        {{ item.amount }}
                    </td>
                    <td>
                        <router-link :to="`transactions/${ item.id }`">
                            Details
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-else> 
            <h3> 
                There is no items :(
            </h3>
        </div>
    </section>
</main>
</template>