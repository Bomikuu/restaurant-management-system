import axios from 'axios'

export default class Utils {
  static getBaseURL() {
    return '/api/'
  }

  static getAPI(url) {
    return axios
      .get(`${this.getBaseURL()}${url}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        return response
      })
      .finally(() => {})
      .catch(error => {
        console.log(error)
      })
  }

  static postAPI(url, params) {
    console.log(params)
    // const headers = { 'Content-Type': 'application/json' }
    return axios
      .post(`${this.getBaseURL()}${url}`, params)
      .then(response => {
        return response
      })
      .catch(error => {
        console.log(error)
      })
  }
}
