import axios from 'axios'

export default class Utils {
  static getBaseURL() {
    return '/api/'
  }

  static getAPI(url, token) {
    const headers = { 'Content-Type': 'application/json' }

    if (token) {
      headers['authorization'] = `Bearer ${token}`
    }

    return axios
      .get(`${this.getBaseURL()}${url}`, {
        headers: headers
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
      headers['authorization'] = `Bearer ${token}`
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
  const isEditMode = Object.prototype.hasOwnProperty.call(payload, 'id')
  Object.entries(payload).map(data => {
    if (isEditMode && data[0] === 'image' && !(data[1] instanceof File)) {
      // do nothing
    } else {
      formData.append(data[0], data[1])
    }
  })
  return formData
}
