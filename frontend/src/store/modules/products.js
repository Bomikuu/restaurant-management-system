import API from '@/utils/utils'

export default {
  state: {
    namespaced: true,
    products: [],
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
  actions: {
    fetchProductList({ commit }) {
      API.getAPI('products').then(response => {
        commit('setAllProducts', response.data)
      })
    },
    getProductDetail() {},
    async createProductDetail({ dispatch }, data) {
      await API.postAPI('products', data).then(response => {
        if (response) {
          dispatch('fetchProductList')
        }
      })
    },
    patchProductDetail() {}
  }
}
