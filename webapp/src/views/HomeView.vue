<script setup lang="ts">
import { useItemStore } from "@/stores/items";
import { useOrderStore } from "@/stores/orders";
import { OrderType } from "@/types";

const orders = useOrderStore();
const items = useItemStore();

const orderTypes = [
  {
    value: OrderType.dinein,
    label: "Dine In",
  },
  {
    value: OrderType.takeout,
    label: "Take Out",
  },
];
</script>

<template>
  <div class="flex flex-row">
    <div class="bg-yellow-200">
      <ul class="flex">
        <li
          v-for="item in items.items"
          v-bind:key="item.id"
          v-on:click="orders.add(item)"
          class="border border-black border-solid p-8 w-32 flex flex-col place-content-center"
        >
          <div class="text-lg">
            {{ item.name }}
          </div>
          <div>{{ item.price }} €</div>
        </li>
      </ul>
    </div>
    <div class="flex flex-col flex-grow ml-4">
      <div class="bg-red-200 p-4">
        <div>Total price: {{ orders.totalPrice }}</div>
        <div class="my-4">
          <button
            class="first:rounded-l-lg last:rounded-r-lg px-6 py-2 border-t border-b border-l last:border-r border-black font-medium text-xs leading-tight uppercase hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out"
            :class="{ isActive: otype.value == orders.orderType }"
            v-on:click="orders.$patch({ orderType: otype.value })"
            :value="otype.value"
            v-bind:key="otype.value"
            v-for="otype in orderTypes"
          >
            {{ otype.label }}
          </button>
        </div>
      </div>
      <div class="bg-blue-200">
        <ul class="flex">
          <li
            v-bind:key="index"
            v-for="(item, index) in orders.orders"
            v-on:click="orders.remove(index)"
            class="border border-black border-solid p-8 w-32 flex flex-col place-content-center"
          >
            <div class="text-lg">
              {{ item.name }}
            </div>
            <div>{{ item.price }} €</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style>
.isActive {
  @apply text-blue-700;
}
</style>
