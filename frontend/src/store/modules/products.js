import API from '@/utils/utils'
import axios from 'axios'

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
    async createProductDetail({ state, dispatch, rootState }, data) {
      console.log(state, dispatch, data)
      console.log('ROOT', rootState)
      // return await API.postAPI('products/', data).then(response => {
      //   console.log(response)
      //   if (response) {
      //     dispatch('fetchProductList')
      //   }
      //   return response
      // })
      //   const config = {
      //     headers: { Authorization: `Bearer ${}`}
      //   }
      axios.post('/api/products/', data)
    },
    patchProductDetail() {}
  }
}
