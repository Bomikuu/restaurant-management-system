export default {
  state: {
    namespaced: true,
    products: [
      {
        id: 0,
        name: 'Buttered Chicken',
        price: '200.00',
        description: 'I am a chicken',
        image: '1.jpeg',
        status: 'Available'
      },
      {
        id: 1,
        name: 'Roasted Chicken',
        price: '250.00',
        description: 'I am a chicken',
        image: '2.jpg',
        status: 'Available'
      },
      {
        id: 2,
        name: 'Roasted Chicken BBQ',
        price: '300.00',
        description: 'I am a chicken',
        image: '3.jpeg',
        status: 'Available'
      },
      {
        id: 3,
        name: 'Chicken Fries with Gulay',
        price: '350.00',
        description: 'I am a chicken',
        image: '4.jpeg',
        status: 'Available'
      },
      {
        id: 4,
        name: 'Chicken Parmesan with Fries',
        price: '200.00',
        description: 'I am a chicken',
        image: '5.jpg',
        status: 'Available'
      }
    ],
    productFilter: ''
  },
  getters: {
    getActiveProducts(state) {
      return state.products.filter(prod => {
        return prod.status !== 'Archived'
      })
    },
    getFilteredProducts(state) {
      return state.products.filter(prod => {
        return prod.status === state.productFilter
      })
    }
  },
  mutations: {
    setProducts(state, product) {
      state.products.unshift(product)
    },
    setAllProducts(state, product) {
      state.products = product
    },
    setProductFilterMode(state, value) {
      state.productFilter = value
    }
  },
  actions: {}
}
