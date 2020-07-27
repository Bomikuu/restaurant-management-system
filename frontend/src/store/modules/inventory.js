export default {
  state: {
    namespaced: true,
    inventoryList: [
      {
        product: "Chicken Parmesan",
        quantity: 20,
        date: "2020-17-02",
      },
      {
        product: "Chicken Parmesan with Fries",
        quantity: 20,
        date: "2020-17-02",
      },
      {
        product: "Roasted Chicken BBQ",
        quantity: 20,
        date: "2020-17-02",
      },
    ],
  },
  mutations: {
    setInventoryItem(state, invent) {
      state.inventoryList.push(invent);
    },
  },
  actions: {},
};
