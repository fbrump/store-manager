<script setup lang="ts">
import ViewHeader from '../../components/ViewHeader.vue';

</script>

<template>
<main>
    <view-header title="Products" subtitle="List of products"></view-header>
    <section>
        <a href="#/products/new" title="Go to form to insert a new one">
            Add New
        </a>
    </section>
    <section>
        <table>
            <thead>
                <tr>
                    <th>
                        Code
                    </th>
                    <th>
                       Name 
                    </th>
                    <th>
                       Description 
                    </th>
                    <th>
                       Price 
                    </th>
                    <th>
                       Category 
                    </th>
                    <th>
                       Actions 
                    </th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="6">
                        Total items <strong>[Number]</strong>.
                    </td>
                </tr>
            </tfoot>
            <tbody>
                <tr>
                    <td>
                        123
                    </td>
                    <td>
                        Corne V3
                    </td>
                    <td>
                        Split keyboard bluetooth with blue switchers and LP keykaps
                    </td>
                    <td>
                        250.00 Euro
                    </td>
                    <td>
                        Kayboards
                    </td>
                    <td>
                        <a href="#products/123" title="Go to details">
                            Details
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    </section>
</main>
</template>