import { createMemoryHistory, createRouter } from 'vue-router'

import DashboardIndex from './views/dashboards/DashboardIndex.vue';
import CategoryList from './views/categories/CategoryList.vue'
import ProductList from './views/products/ProductList.vue'
import TransactionList from './views/transactions/TransactionList.vue'

const routes = [
  { path: '/', component: DashboardIndex },
  { path: '/categories', component: CategoryList },
  { path: '/products', component: ProductList },
  { path: '/transactions', component: TransactionList },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes: routes,
})

export default router;
