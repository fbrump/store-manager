<script setup lang="ts">
import { ref } from 'vue';
import { useTransactionsStore  } from '@stores/transactions';
import type { Transaction } from '@/views/transactions/interfaces';


const store = useTransactionsStore();

const transactions = ref<Array<Transaction>>(store.getAll);
const numberOfTransactions = ref<number>(transactions.value.length);

</script>

<template>
<main>
    <header>
        <h1>
            Dashboard Charts
        </h1>
    </header>
    <section>
        <h2>
            There are <strong>{{ numberOfTransactions }}</strong>.
        </h2>
    </section>
    <section>
        Top 5 Transactions.
        <div>
            <ol>
                <li>
                    1 Produt Name - In   
                </li>
                <li>
                    2 Produt Name - In   
                </li>
                <li>
                    3 Produt Name - In   
                </li>
                <li>
                    4 Produt Name - In   
                </li>
                <li>
                    5 Produt Name - In   
                </li>
            </ol>
        </div>
    </section>
    <section>
        Products with less amount on stock.
        <ul>
            <li>
                Product Name - <strong>number</strong>
            </li>
            <li>
                Product Name - <strong>number</strong>
            </li>
            <li>
                Product Name - <strong>number</strong>
            </li>
            <li>
                Product Name - <strong>number</strong>
            </li>
        </ul>
    </section>
    <section>
        Products by Category.
        <ul>
            <li>
                <strong>x</strong> Products by <em>Category Name</em>
            </li>
            <li>
                <strong>x</strong> Products by <em>Category Name</em>
            </li>
            <li>
                <strong>x</strong> Products by <em>Category Name</em>
            </li>
        </ul>
    </section>
</main>
</template>