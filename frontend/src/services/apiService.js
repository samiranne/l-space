import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

const API_URL = 'http://localhost:8000/api'
Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = API_URL

export class APIService {
  get (resource, id = '') {
    return Vue.axios
      .get(`${resource}/${id}`).then((response) => response.data)
  }
}
export default APIService
