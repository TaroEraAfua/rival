import api from '@/vuex/api/api';
const md5 = require('js-md5')
const encrypt = (userId, password) => md5(userId + password);

export default {
  namespaced: true,

  state: {
    userEditParam: {
      user_icon: {},
      user_id: '',
      user_name: '',
      mail: '',
      password1: '',
      password2: '',
      prefecture: '',
      city: '',
      birth_dt: '',
      gender: null,
      position: [],
      height: null,
      ex_year: null,
      ex_width: [],
      message: null
    },
    errUserEditMsg: {}
  },
  mutations: {
    setUserInfo (state, payload) {
      state.userInfo = payload.user;
      state.joinTeamInfo =payload.team;
    },
    setUserApiParam: function (state, data=null) {
      if (data) {
        for (let key in data) {
          let row = data[key];
          if (row) {
            state.userEditParam[row.key] = row.val;
          }
        }
      } else {
        state.userEditParam = {
          user_icon: {},
          user_id: '',
          user_name: '',
          mail: '',
          password1: '',
          password2: '',
          prefecture: '',
          city: '',
          birth_dt: '',
          gender: null,
          position: [],
          height: null,
          ex_year: null,
          ex_width: [],
          message: null
        }
      }


    },
    setErrMsg: function (state, msg={}) {
      console.log(msg);
      state.errUserEditMsg = msg;
    }
  },

  actions: {
    async updateUserData ({ commit, state }) {
      commit('setErrMsg');
      let request = {};
      for (let key in state.userEditParam) {
        if ( ['password1', 'password2'].includes(key) ) {
          request['password'] = encrypt(state.userEditParam['user_id'], state.userEditParam[key]);
        } else {
          request[key] = state.userEditParam[key]
        }
      }
      let result = await api.post('/user/update_user', request);
      if (result.result_cd === '001') {
        commit('setUserApiParam');
        commit('setErrMsg');
      } else {
        commit('setErrMsg', result);
      }
    },
    async setUserData ({ commit, state }) {
      let request = {};
      for (let key in state.userEditParam) {
        if ( ['password1', 'password2'].includes(key) ) {
          request['password'] = encrypt(state.userEditParam['user_id'], state.userEditParam[key]);
        } else {
          request[key] = state.userEditParam[key]
        }
      }
      let result = await api.post('/user/set_user', request);
      if (result.result_cd === '001') {
        commit('setUserApiParam');
        commit('setErrMsg');
      } else {
        commit('setErrMsg', result);
      }
    },
    setUserEditParam: function ({commit}, data) {
      commit('setUserApiParam', data)
    },
    setUserEditErrMsg: function({commit}, data) {
      commit('setErrMsg', data);
    }
  }
}
