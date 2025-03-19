import { createWebHashHistory, createRouter } from 'vue-router'

import DashboardIndex from './views/dashboards/DashboardIndex.vue';
import CategoryList from './views/categories/CategoryList.vue'
import CategoryDetail from './views/categories/CategoryDetail.vue'
import ProductList from './views/products/ProductList.vue'
import TransactionList from './views/transactions/TransactionList.vue'
import ProductDetail from './views/products/ProductDetail.vue';

const routes = [
  { path: '/', component: DashboardIndex },
  { path: '/categories', component: CategoryList },
  { path: '/categories/:id', component: CategoryDetail, props: true },
  { path: '/products', component: ProductList },
  { path: '/products/:id', component: ProductDetail, props: true },
  { path: '/transactions', component: TransactionList },
]

const router = createRouter({
  history: createWebHashHistory(), 
  routes: routes,
})

export default router;
