import { getFormData } from '@/utils/utils'
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
        return prod.status === 1
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
      state.products = product.sort((a, b) => b.id - a.id)
    },
    setProductFilterMode(state, value) {
      state.productFilter = value
    }
  },
  actions: {
    fetchProductList({ commit, rootState }) {
      const token = rootState.currentUser.access

      API.getAPI('products/', token).then(response => {
        commit('setAllProducts', [])
        setTimeout(() => {
          commit('setAllProducts', response.data)
        }, 100)
        
      })
    },
    getProductDetail() {},
    async createProductDetail({ dispatch, rootState }, params) {
      const token = rootState.currentUser.access
      const formData = getFormData(params)

      return await API.postAPI('products/', formData, token).then(response => {
        console.log(response)
        if (response) {
          dispatch('fetchProductList')
        }
        return response
      })
    },
    patchProductDetail({ rootState, dispatch }, data) {
      const token = rootState.currentUser.access
      const formData = getFormData(data)

      const headers = { 'Content-Type': 'application/json' }
      if (token) {
        headers['authorization'] = `Bearer ${token}`
      }
      
      return axios
        .patch(`/api/products/${data.id}/`, formData, {
          headers: headers
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
