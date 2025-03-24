<script setup lang="ts">
import ViewHeader from '@components/ViewHeader.vue';

</script>

<template>
<main>
    <view-header title="Transactions" subtitle="List of transactions"></view-header>
    <section>
        <div>
        </div>
        <table>
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
                        Total items <strong class="font-semibold">0</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody>
                <tr>
                    <td>
                        3748290
                    </td>
                    <td>
                        T-Shart
                    </td>
                    <td>
                        Clouth
                    </td>
                    <td>
                        Employee 1
                    </td>
                    <td>
                        In
                    </td>
                    <td>
                        5
                    </td>
                    <td>
                        <a href="#details">
                            Details
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
        <div> 
            <h3> 
                There is no items :(
            </h3>
        </div>
    </section>
</main>
</template>