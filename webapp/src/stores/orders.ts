import { defineStore } from "pinia";
import { OrderType, type Item } from "@/types";

const TAX_RATE = 0.07;

// function getNetPrice(price: number, taxRate: number) {
//   return price / (taxRate + 1);
// }

function getTaxPrice(price: number, taxRate: number) {
  return (price / (taxRate + 1)) * taxRate;
}

export const useOrderStore = defineStore({
  id: "orderstore",
  state: () => ({
    orders: [] as Item[],
    orderType: OrderType.dinein,
  }),
  getters: {
    count: (state) => state.orders.length,
    totalPrice(state): number {
      let price = 0;
      for (const o of state.orders) {
        price += o.price;
      }
      return price;
    },
    taxPrice(): number {
      return getTaxPrice(this.totalPrice, TAX_RATE);
    },
  },
  actions: {
    empty() {
      this.orders = [];
    },
    add(item: Item) {
      this.orders.push(item);
    },
    remove(index: number) {
      this.orders.splice(index, 1);
    },
  },
});
