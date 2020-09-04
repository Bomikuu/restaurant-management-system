export default {
  state: {
    products: [
      {
        id: 0,
        name: "Buttered Chicken",
        price: "200.00",
        description: "I am a chicken",
        image: "1.jpeg",
      },
      {
        id: 1,
        name: "Roasted Chicken",
        price: "250.00",
        description: "I am a chicken",
        image: "2.jpg",
      },
      {
        id: 2,
        name: "Roasted Chicken BBQ",
        price: "300.00",
        description: "I am a chicken",
        image: "3.jpeg",
      },
      {
        id: 3,
        name: "Chicken Fries with Gulay",
        price: "350.00",
        description: "I am a chicken",
        image: "4.jpeg",
      },
      {
        id: 4,
        name: "Chicken Parmesan with Fries",
        price: "200.00",
        description: "I am a chicken",
        image: "5.jpg",
      },
    ],
  },
  getters: {
    getActiveProducts(state) {
      return state.products.filter((prod) => {
        return prod.status !== "Archieved";
      });
    },
  },
  mutations: {
    setProducts(state, product) {
      state.products.unshift(product);
    },
    setAllProducts(state, product) {
      state.products = product;
    },
  },
  actions: {},
};
