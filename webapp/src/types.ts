export interface Item {
  id: string;
  name: string;
  price: number;
  // scenarios for differential pricing
  // inhouse - 19%
  // takeway - 7%
  // beverage - inhouse 19%, takeway 7% + recycling fee
  // model with orderType (situation) and pricingType -> complexity of orderType x pricingType
}

export enum OrderType {
  dinein,
  takeout,
}
