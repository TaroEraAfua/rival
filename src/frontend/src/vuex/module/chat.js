import api from '@/vuex/api/api';

export default {
  namespaced: true,

  state: {
    checkChatRoomId: '',
    chatMessageList: [],
    chatErrMsg: {}
  },
  mutations: {
    setChatMessageList(state, payload) {
      state.chatMessageList = payload
    },
    setChatRoomList (state, payload) {
      state.chatRoomList = payload
    },
    setCheckChatRoomId (state, payload) {
      state.checkChatRoomId = payload
    },
    setErr (state, data) {
      state.chatErrMsg = data;

    }
  },

   actions: {
    /**
     * チャット内容取得
     */
    getChatMessage : async function ({ commit }, payload) {
      const data = {challenge_id: payload};
      try {
        let result = await api.post('/chat/get_chat_log', data);
        if (result.result_cd === '001') {
          commit('setChatMessageList', result.data)
        }
      } catch (e) {

      } finally {
      }

    },
    async sendChatMessage ({ commit }, payload) {
      try {
        let result = await api.post('/chat/set_chat_log', {
          'challenge_id': payload.challenge_id,
          'team_id': payload.team_id,
          'user_id': payload.user_id,
          'message': payload.message,
        });
      } catch (e) {

      } finally {

      }

    },
    /**
     * 選択した情報を初期化
     */
    resetCheckArea ({ commit }, payload) {
      commit('resetCheckAreaData')
    }
  }
}
