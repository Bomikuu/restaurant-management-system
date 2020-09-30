import { getFormData } from '@/utils/utils'
import API from '@/utils/utils'
import axios from 'axios'

export default {
  state: {
    namespaced: true,
    inventoryList: [
      {
        id: 99,
        product: 'Chicken Parmesan',
        quantity: 20,
        date: '2020-17-02'
      },
      {
        id: 100,
        product: 'Chicken Parmesan with Fries',
        quantity: 20,
        date: '2020-17-02'
      },
      {
        id: 98,
        product: 'Roasted Chicken BBQ',
        quantity: 20,
        date: '2020-17-02'
      }
    ]
  },
  getters: {
    getActiveInventoryItem(state) {
      return state.inventoryList.filter(invent => {
        return invent.status !== 2
      })
    },
    getFilteredInventoryItem(state) {
      return state.inventoryList.filter(invent => {
        return invent.status === state.productFilter
      })
    }
  },
  mutations: {
    setInventoryItem(state, invent) {
      state.inventoryList.push(invent)
    },
    setAllInventory(state, invent) {
      state.inventoryList = invent.sort((a, b) => b.id - a.id)
    }
  },
  actions: {
    fetchInventoryList({ commit, rootState }) {
      const token = rootState.currentUser.access

      API.getAPI('inventory/', token).then(response => {
        commit('setAllInventory', response.data)
      })
    },
    getInventoryDetail() {},
    async createInventoryDetail({ dispatch, rootState }, params) {
      const token = rootState.currentUser.access
      const formData = getFormData(params)

      return await API.postAPI('inventory/', formData, token).then(response => {
        console.log(response)
        if (response) {
          dispatch('fetchInventoryList')
        }
        return response
      })
    },
    patchInventoryDetail({ rootState, dispatch }, data) {
      const token = rootState.currentUser.access
      const formData = getFormData(data)

      const headers = { 'Content-Type': 'application/json' }
      if (token) {
        headers['authorization'] = `Bearer ${token}`
      }

      return axios
        .patch(`/api/inventory/${data.id}/`, formData, {
          headers: headers
        })
        .then(response => {
          return response
        })
        .finally(() => {
          dispatch('fetchInventoryList')
        })
        .catch(error => {
          console.log(error)
          return error
        })
    }
  }
}
