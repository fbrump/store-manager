<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';
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
<main>
    <view-header title="Transaction Details" subtitle="Show details of the transaction"/>
    <section>
        <form v-if="transaction" action="" method="post">
            <div>
                <div>
                    <label for="code">
                        Code
                    </label>
                </div>
                <div>
                    <code>
                    {{ transaction.id }}
                    </code>
                </div>
            </div>
            <div>
                <div>
                    <label for="type">
                        Type
                    </label>
                </div>
                <div>
                    <div>
                    <select v-model="transaction.type" name="type" id="type" title="Transaction type"> 
                                <option value="In">In</option>
                                <option value="Out">Out</option>
                        </select>
                        <div>
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <div>
                    <label for="amount">
                        Amount
                    </label>
                </div>
                <div>
                    <input v-model="transaction.amount" id="amount" name="amount" placeholder="Enter with amount" title="Amount">
                </div>
            </div>
            <div>
                <div>
                    <label for="product">
                        Product
                    </label>
                </div>
                <div>
                    <div>
                    <select v-model="transaction.product" name="product" id="product" title="Product"> 
                                <option value="SKU001">T-Shirt Nike</option>
                                <option value="SKU002">Shorts Pullma</option>
                        </select>
                        <div>
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <div>
                    <label for="category">
                        Category
                    </label>
                </div>
                <div>
                    <em>
                    {{ transaction.category }}
                    </em>
                </div>
            </div>
            <div>
                <div>
                    <label for="user">
                        User
                    </label>
                </div>
                <div>
                    <em>
                    {{ transaction.user }}
                    </em>
                </div>
            </div>
            <div>
                <div></div>
                <label>
                <input  type="checkbox" name="active" id="active" v-model="transaction.active" /> 
                <span class="text-sm">
                    Active
                </span>
                </label>
            </div>
            <div>
                <div></div>
                <div>
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