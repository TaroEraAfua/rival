import axios from 'axios'
import isMobile from "ismobilejs";
import encripter from "@/vuex/api/encripter";
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.withCredentials = false;
export default {

  request: async function (method, originUrl, params) {
    let promise = null;
    let url = process.env.VUE_APP_API_URL +  originUrl;

    let headers = {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*',
      'token': sessionStorage.getItem('token')
    };
    let body = null;
    if (params && process.env.NODE_ENV !== 'development') {
      body = await encripter.encrypt(params, sessionStorage.getItem('token'));
    } else {
      body = params
    }

    let param = {param: body};
    if (method === 'get') {
      promise = axios.get(url, param, {headers: headers});
    } else if (method === 'post') {
      promise = axios.post(url, param,{headers: headers});

    } else if (method === 'put') {
      promise = axios.put(url, param,{headers: headers});
    }
    promise.catch(error => {
    });
    let result = await promise.then(　function(res) {
        return res
      }
    );

    return this.makeReturn(result)
  },
  makeReturn: async function (param) {
    let res = param.data;
    if (process.env.NODE_ENV !== 'development' && res && Object.keys(res).includes('data')) {
      res['data'] = await encripter.decrypt(res.data, sessionStorage.getItem('token'));

    }
    return res
  },
  get: function (url, params) {
    return this.request('get', url, params)
  },
  post: function (url, params) {
    return this.request('post', url, params)
  },
  put: function (url, params) {
    return this.request('put', url, params)
  },

}
