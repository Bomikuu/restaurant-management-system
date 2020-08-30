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

  static postAPI(url, params, token) {
    console.log(params)
    const headers = { 'Content-Type': 'application/json' }

    if (token) {
      headers['Authorization'] = `Bearer ${token}`
    }

    return axios
      .post(`${this.getBaseURL()}${url}`, params, { headers: headers })
      .then(response => {
        return response
      })
      .catch(error => {
        console.log(error)
      })
  }
}

export const getFormData = payload => {
  const formData = new FormData()

  Object.entries(payload).map(data => {
    formData.append(data[0], data[1])
  })
  return formData
}
