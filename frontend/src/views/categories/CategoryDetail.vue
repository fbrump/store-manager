<script setup lang="ts">
import ViewHeader from '../../components/ViewHeader.vue';

</script>

<template>
<main class="justify-items-center">
    <view-header title="Category" subtitle="Show details of the category"></view-header>
    <section>
        <form action="" method="post">
            <div>
                <label for="name">
                    Name
                </label>
                <input type="text" name="name" id="name" title="Category name" />
            </div>
            <div>
                <label for="active">Active</label>
                <input type="checkbox" name="active" id="active" />
            </div>
            <div>
                <label for="description">
                    Description
                </label>
                <textarea name="description" id="description" cols="30" rows="10"></textarea>
            </div>
            <button type="submit">
                Save
            </button>
        </form>
    </section>
</main>
</template>