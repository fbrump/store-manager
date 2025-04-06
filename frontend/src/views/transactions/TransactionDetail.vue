<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
import SelectIcon from '@components/SelectIcon.vue';
import { useTransactionsStore } from '@stores/transactions';
import { ref } from 'vue';
import type { Transaction } from './interfaces';


const props = defineProps<{
    id:string,
}>();

const store = useTransactionsStore();

const transaction = ref<Transaction | null>(store.getById(props.id));
</script>

<template>
<main class="flex flex-col">
    <view-header title="Transaction Details" subtitle="Show details of the transaction"/>
    <section class="justify-items-center">
        <form v-if="transaction" action="" method="post"> 
            <div>
                <div class="md:w-1/3">
                    <label for="code">
                        Code
                    </label>
                </div>
                <div class="md:w-2/3">
                    <code>
                    {{ transaction.id }}
                    </code>
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="type">
                        Type
                    </label>
                </div>
                <div class="md:w-2/3">
                    <div class="relative">
                        <select v-model="transaction.type" name="type" id="type" title="Transaction type"> 
                                <option value="In">In</option>
                                <option value="Out">Out</option>
                        </select>
                        <select-icon></select-icon>
                    </div>
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="amount"> 
                        Amount
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="number" v-model="transaction.amount" id="amount" name="amount" placeholder="Enter with amount" title="Amount">
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="product">
                        Product
                    </label>
                </div>
                <div class="md:w-2/3">
                    <div class="relative">
                        <select v-model="transaction.product" name="product" id="product" title="Product"> 
                                <option value="SKU001">T-Shirt Nike</option>
                                <option value="SKU002">Shorts Pullma</option>
                        </select>
                        <select-icon></select-icon>
                    </div>
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="category">
                        Category
                    </label>
                </div>
                <div class="md:w-2/3">
                    <em>
                    {{ transaction.category }}
                    </em>
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="user">
                        User
                    </label>
                </div>
                <div class="md:w-2/3">
                    <em>
                    {{ transaction.user }}
                    </em>
                </div>
            </div>
            <div>
                <div class="md:w-1/3"></div>
                <label class="md:w-2/3 block text-gray-500 font-bold">
                    <input  type="checkbox" name="active" id="active" v-model="transaction.active" /> 
                    <span class="text-sm">
                        Active
                    </span>
                </label>
            </div>
            <div>
                <div class="md:w-1/3"></div>
                <div class="md:w-2/3 gap-0.5 text-right">
                    <button type="submit">
                        Save
                    </button>
                    <router-link to="/transactions">
                        Cancel 
                    </router-link>
                </div>
            </div>
        </form>
    </section>
</main>
</template>