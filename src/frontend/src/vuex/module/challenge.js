import api from '@/vuex/api/api';

export default {
  namespaced: true,

  state: {
    sendTeamList: [],
    receiveTeamList: [],
    matchTeamList: [],
    challengeErrMsg: null
  },
  getters: {
    sendFlg(state, payload) {
      if (payload.mode === 'receive') {
        state.receiveTeamList[payload.col].btn = {
          type: payload.flg,
          title: payload.title
        }
      } else if (payload.mode === 'send') {
        state.sendTeamList[payload.col].btn = {
          type: payload.flg,
          title: payload.title
        }
      } else if (payload.mode === 'match') {
        state.matchTeamList[payload.col].btn = {
          type: payload.flg,
          title: payload.title
        }
      }
    },
  },
  mutations: {
    initTeamList(state) {
      state.sendTeamList = [];
      state.receiveTeamList = [];
      state.matchTeamList = [];
    },
    teamListData(state, payload) {
      console.log(payload)
      for (let key in payload) {
        switch (key) {
          case 'RES':
            state.receiveTeamList = payload[key];
            break;
          case 'SEND':
            state.sendTeamList = payload[key];
            break;
          case 'MATCH':
            state.matchTeamList = payload[key];
            break;
        }
      }
    },
    setErrorMessage (state, data=null) {
      state.challengeErrMsg = data;
    }
  },

  actions: {
    /**
     * チーム検索の結果を取得
     */
    getChallengeList: async function ({commit}, payload) {
      const data = {team_id: payload};
      commit('initTeamList');
      commit('setErrorMessage');
      try {
        let result = await api.post('/challenge/get_challenge', data);
        if (result.result_cd === '001') {
          commit('teamListData', result.data);
        } else {
          commit('setErrorMessage', result);
        }
      } catch (e) {

      } finally {
      }
    },
    /**
     * チーム送信
     */
    sendChallenge: async function ({commit}, payload) {
      commit('setErrorMessage');
      try {
        let result = await api.post('/challenge/set_challenge', payload);
        if (result.result_cd === '001') {
        } else {
          console.log(result);
          commit('setErrorMessage', result);
        }
      } catch (e) {

      } finally {

      }


    },
    cancelChallenge: async function ({commit}, payload) {
      commit('setErrorMessage');
      try {
        let result = await api.post('/challenge/set_match', payload);
        if (result.result_cd === '001') {
          commit('teamListData', result.data);
        } else {
          console.log(result);
          commit('setErrorMessage', result);
        }
      } catch (e) {

      } finally {

      }

    }
    ,
    matchChallenge: async function ({commit}, payload) {
      commit('setErrorMessage');
      try {
        let result = await api.post('/challenge/set_match', payload);
        if (result.result_cd === '001') {
          commit('teamListData', result.data);
        } else {
          console.log(result);
          commit('setErrorMessage', result);
        }
      } catch (e) {

      } finally {

      }

    }
    ,
    deleteChallenge: async function ({commit}, payload) {
      commit('setErrorMessage');
      try {
        let result = await api.post('/challenge/delete_challenge', payload);
        if (result.result_cd === '001') {
          commit('teamListData', result.data);
        } else {
          console.log(result);
          commit('setErrorMessage', result);
        }
      } catch (e) {

      } finally {

      }
    },
    setSendFlg({commit}, payload) {
      commit('sendFlg', payload)
    },
  }
}
