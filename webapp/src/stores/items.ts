import { defineStore } from "pinia";
import type { Item } from "@/types";

export const useItemStore = defineStore({
  id: "itemstore",
  state: () => ({
    items: [] as Item[],
  }),
  getters: {
    count: (state) => state.items.length,
  },
  actions: {
    set(items: Item[]) {
      this.items = items;
    },
    get(id: string) {
      return this.items.find((o) => o.id == id);
    },
  },
});
