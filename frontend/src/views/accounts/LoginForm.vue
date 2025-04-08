<script setup lang="ts">

</script>

<template>
<main class="flex flex-col">
    <view-header title="Product Details" subtitle="Show details of the product"/>
    <section class="justify-items-center">
        <form action="" method="post">
            <div>
                <div class="md:w-1/3">
                    <label for="login">
                       Login
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="email" id="login" name="login" placeholder="Enter with the login" title="Enter with the login" autofocus />
                </div>
            </div>
            <div>
                <div class="md:w-1/3">
                    <label for="password">
                        Password
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input type="email" id="password" name="password" placeholder="Enter with the password" title="Enter with the password" />
                </div>
            </div>
            <div>
                <button type="submit" title="Login">
                    Login
                </button>
            </div>
        </form> 
    </section>
</main>
</template>