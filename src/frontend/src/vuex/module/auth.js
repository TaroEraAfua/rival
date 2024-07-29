import api from '@/vuex/api/api';
const md5 = require('js-md5');
const encrypt = (userId, password) => md5(userId + password);

export default {
  namespaced: true,

  state: {
    loginParam: {
      user_id: '',
      password: ''
    },
    changePassParam: {
      password_old: '',
      password_new1: '',
      password_new2: '',
    },
    errAuthMsg: '',
    joinTeamList: {
      team: [],
      select: ''
    },
    userList: {

    },
    authFlg: null,
    menuPathList: {path: '',main: 'user', sub: null},
  },
  getters: {
    getAuthList (state) {
      return function (key) {
        return state[key]
      }
    }
  },
  mutations: {
    setLoginParam: function (state, data) {
      state.loginParam[data.key] = data.val;
    },
    setChangePassParam: function (state, data) {
      state.changePassParam[data.key] = data.val;
    },
    logIn: function (state, data) {
      // TODO ユーザーテーブルにデフォルトチームIDを設定する必要あり
      sessionStorage.setItem('rda', Math.random().toString(36).substring(7));
      state.errAuthMsg = '';
      state.userList = data.user;
      state.joinTeamList.team = data.team;
      state.joinTeamList.select = data.team.length > 0 ? data.team[0]['team_id']: '';
      state.authFlg = true;
    },
    setDefaultTeamData: function (state,data) {
      state.joinTeamList.select = data;
    },
    logOut: function (state) {
      state.errAuthMsg = '';
      state.joinTeamList = {
        team: [],
        select: ''
      };
      state.userList = {};
      state.authFlg = false;
      sessionStorage.removeItem('rds');
      sessionStorage.removeItem('ini');
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('rda');
    },
    setUser: function (state, data) {
      state.authFlg = true;
      state.userList = data.user;
      state.joinTeamList.team = data.team;
      state.joinTeamList.select = data.team[2].team_id;
    },
    setMenu: function (state, data) {
      state.menuPathList = data;
    },
    authData: function (state, payload) {
      state.userId = payload.userId;
      if (payload.pass1.length > 0) {
        state.passLength.pass1 = payload.pass1.length
      }
      if (payload.pass2.length > 0) {
        state.passLength.pass2 = payload.pass2.length
      }
      state.pass1 = encrypt(payload.userId, payload.pass1)
      state.pass2 = encrypt(payload.userId, payload.pass2)
    },
    errAuthMsgData (state, msg) {
      state.errAuthMsg = msg
    },
    initLoginParam (state) {
      state.loginParam = {
        user_id: '',
        password: ''
      };
    }
  },

  actions: {
    /**
     * ログイン
     * パスワードはMD5でハッシュ化
     */
    logIn: async function ({ commit, dispatch , state }) {
      commit('errAuthMsgData', '');
      // どちらかが未入力ならAPI投げない
      console.log(state.loginParam);
      if (state.user_id !== '' && state.password !== '') {
        const data = {
          user_id: state.loginParam.user_id,
          password: encrypt(state.loginParam.user_id, state.loginParam.password)
        };
        let result = await api.post('/user/sign_in', data);
        console.log(result);
        if (result.result_cd === '001') {
          let data = result.data;
          await commit('logIn' , data);
          await dispatch('SET_STATE', null, {root: true})
        } else if (result.result_cd === '002') {
          commit('errAuthMsgData', result.message);
        }
      } else {
        commit('errAuthMsgData', 'IDまたはパスワードが空白です')
      }
    },
    /**
     * ユーザー情報取得
     * @returns {Promise<void>}
     */
    getUser: async function ({ commit , state, dispatch}) {
      let result = await api.post('/user/get_user', { user_id: state.userList.user_id });
      if (result.result_cd === '001') {
        const response = result.data;
        commit('logIn' , response);
        await dispatch('SET_STATE', null, {root: true})
      }
    },
    setSelectMenu: async function ({commit, dispatch}, data) {
      commit('setMenu', data);
      await dispatch('SET_STATE', null, {root: true})
    },
    /**
     * 選択チーム設定
     */
    setDefaultTeam: function ({commit, dispatch}, data) {
      commit('setDefaultTeamData', data);
      dispatch('SET_STATE', null, {root: true})
    },
    /* パスワード更新 */
    updatePass: async function ({ commit, dispatch, state }) {
      commit('errAuthMsgData', '');
      if (state.changePassParam.password_old !== '' && state.changePassParam.password_new1 !== '' && state.changePassParam.password_new2 !== '') {
        if (state.changePassParam.password_new1 === state.changePassParam.password_new2) {
          const old_data = {
            user_id: state.userList.user_id,
            password: encrypt(state.userList.user_id, state.changePassParam.password_old)
          };
          const new_data = {
            user_id: state.userList.user_id,
            password_old: encrypt(state.userList.user_id, state.changePassParam.password_old),
            password_new: encrypt(state.userList.user_id, state.changePassParam.password_new1)
          };
          let new_result = await api.post('/user/update_pass', new_data);
          if (new_result.result_cd === '001') {
            dispatch('common/setMessage', new_result, {root: true});
            await dispatch('SET_STATE', null, {root: true})
          } else if (new_result.result_cd === '002') {
            commit('errAuthMsgData', new_result.message);
          }
        } else {
          commit('errAuthMsgData', '再入力されたパスワードが違います')
        }
      } else {
        //commit('errAuthMsgData', '空白欄が存在します')
      }
    },
    checkUserId ({ commit }, param) {
      const data = {
        user_id: param
      }
      api.post('/user/check_user', data)
        .then((res) => {
          let result = res.data
          if (result.status !== 200) {
            commit('errSignMsgData', data.message)
          } else {
            commit('errSignMsgData', '')
          }
      })
    },
    /**
     * ログアウト
     */
    logOut ({ commit }, payload) {
      commit('logOut')
    },
    resetErr ({ commit } ) {
      commit('errAuthMsgData')
    },
    setLoginParam: function ({commit}, data) {
      commit('setLoginParam', data);
    },
    setChangePassParam: function ({commit}, data) {
      commit('setChangePassParam', data);
    },
    initLoginParam: function ({commit}) {
      commit('initLoginParam');
    },
    setErrMsg: function ({commit}, data) {
      commit('errAuthMsgData', data);
    },
  }
}
