import Vue from 'vue'
import Vuex from 'vuex'
import products from './modules/products.js'
import inventory from './modules/inventory.js'
import API from '@/utils/utils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    barColor: 'rgba(0, 0, 0, .8), rgba(0, 0, 0, .8)',
    barImage:
      'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    currentUser: null
  },
  mutations: {
    SET_BAR_IMAGE(state, payload) {
      state.barImage = payload
    },
    SET_DRAWER(state, payload) {
      state.drawer = payload
    },
    setCurrentUser(state, user) {
      state.currentUser = user
    }
  },
  getters: {},
  actions: {
    loginUser({ commit }, data) {
      localStorage.removeItem('currentUser')
      return API.postAPI(`token/`, data).then(response => {
        const userData = { ...data, ...response.data }
        userData['expire_data'] = new Date()
        commit('setCurrentUser', userData)
        localStorage.setItem('currentUser', JSON.stringify(userData))
        return response
      })
    },

    refreshToken({ commit, rootState }) {
      const { refresh } = rootState.currentUser
      const payload = {
        refresh
      }
      return API.postAPI('token/refresh/', payload).then(response => {
        const userData = { ...payload, ...response.data }
        userData['expire_data'] = new Date()
        commit('setCurrentUser', userData)
        localStorage.setItem('currentUser', JSON.stringify(userData))
        return response
      })
    }
  },
  modules: { products, inventory }
})
