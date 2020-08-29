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

  static postAPI(url, body) {
    console.log(body)
    const headers = { 'Content-Type': 'application/json' }
    return axios
      .post(`${this.getBaseURL()}${url}`, body, headers)
      .then(response => {
        return response
      })
      .catch(error => {
        console.log(error)
      })
  }
}
