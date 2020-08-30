import { API, getFormData } from '@/utils/utils'
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
    fetchProductList({ commit, rootState }) {
      const token = rootState.currentUser.access
      console.log(token)
      API.getAPI('products').then(response => {
        commit('setAllProducts', response.data)
      })
      // axios
      //   .get(`/api/products/`, {
      //     headers: {
      //       Authorization: `Bearer ${token}`
      //     }
      //   })
      //   .then(response => {
      //     console.log('RESPONSE', response)
      //     commit('setAllProducts', response.data)
      //     return response
      //   })
      //   .finally(() => {})
      //   .catch(error => {
      //     console.log(error)
      //   })
    },
    getProductDetail() {},
    async createProductDetail({ dispatch, rootState }, params) {
      console.log('ROOT', rootState)
      // return await API.postAPI('products/', data).then(response => {
      //   console.log(response)
      //   if (response) {
      //     dispatch('fetchProductList')
      //   }
      //   return response
      // })

      const token = rootState.currentUser.access
      const formData = getFormData(params)

      console.log(formData)

      axios
        .post(`/api/products/`, formData, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          console.log('RESPONSE', response)
          dispatch('fetchProductList')
          return response
        })
        .finally(() => {})
        .catch(error => {
          console.log(error)
        })
    },
    patchProductDetail({ rootState, dispatch }, data) {
      const token = rootState.currentUser.access
      const formData = getFormData(data)

      return axios
        .post(`/api/products/${data.id}`, formData, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          return response
        })
        .finally(() => {
          dispatch('fetchProductList')
        })
        .catch(error => {
          console.log(error)
          return error
        })
    }
  }
}
