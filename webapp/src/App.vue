<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import { useItemStore } from "./stores/items";

const items = useItemStore();
items.set([
  { id: "1", name: "Food", price: 3.5 },
  { id: "2", name: "Foodier", price: 4.5 },
  { id: "3", name: "Kabob", price: 6.5 },
  { id: "10", name: "Coke", price: 1.5 },
  { id: "11", name: "Coffee", price: 1.8 },
]);
</script>

<template>
  <nav class="text-center w-full mt-4 divide-slate-800 divide-solid divide-x">
    <router-link to="/">Bestellung</router-link>
    <router-link to="/history">Verlauf</router-link>
    <router-link to="/products">Produkte</router-link>
    <a href="">Ausloggen</a>
  </nav>
  <main class="m-4">
    <RouterView />
  </main>
</template>

<style>
a {
  @apply px-4 py-2;
}

.router-link-active {
  @apply font-bold bg-slate-200;
}
</style>
