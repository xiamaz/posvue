<template>
  <div class="w-full flex flex-row">
    <ul class="bg-yellow-200 w-96 p-4 divide-y divide-black">
      <li
        class="p-4 h-12"
        v-bind:key="item.id"
        v-for="item of items"
        v-on:click="() => selectItem(item.id)"
        :class="{ 'list-item-active': item.id === selectedId }"
      >
        {{ item.name || "_______" }}
      </li>
      <li class="p-4" key="-1" v-on:click="addItem">+</li>
    </ul>
    <div class="bg-red-200 w-full p-4">
      <form action="" class="space-y-4">
        <div>
          <label for="name" class="w-32 inline-block">Name</label>
          <input
            name="name"
            type="text"
            :value="selectedItem && selectedItem.name"
            @input="
              event => setItem({ ...selectedItem as Item, ...{ name: (event.target as HTMLInputElement).value } })
            "
          />
        </div>
        <div>
          <label for="price" class="w-32 inline-block">Price</label>
          <input
            name="price"
            type="number"
            step="0.01"
            :value="selectedItem && selectedItem.price"
            @blur="
              event => setItem({ ...selectedItem as Item, ...{ price: Number((event.target as HTMLInputElement).value) } })
            "
          />
        </div>
      </form>

      <button
        class="border border-black p-4"
        @click="() => removeItem(selectedId)"
      >
        Remove Item
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { storeToRefs } from "pinia";
import { useItemStore } from "@/stores/items";
import type { Item } from "@/types";

const itemStore = useItemStore();
const { items } = storeToRefs(itemStore);

let selectedId = ref("");
let selectedItem = ref<Item | undefined>(undefined);

function selectItem(itemId: string) {
  selectedId.value = itemId;

  selectedItem.value = itemStore.get(itemId);
}

function addItem() {
  let items = itemStore.items;
  const maxId = Math.max(...items.map((i) => Number(i.id)));
  const item = { id: String(maxId + 1), name: "", price: 0 };
  items.push(item);
  itemStore.set(items);

  selectedId.value = item.id;
  selectedItem.value = item;
}

function removeItem(itemId: string) {
  let items = itemStore.items;
  items = items.filter((i) => !(i.id === itemId));
  itemStore.set(items);
}

function setItem(item: Item) {
  let items = itemStore.items;
  const index = items.findIndex((i) => i.id === item.id);
  items[index] = item;
  itemStore.set(items);

  selectedItem.value = item;
}
</script>

<style>
.list-item-active {
  @apply font-bold;
}
</style>
