import api from '@/vuex/api/api';

export default {
  namespaced: true,
  state: {
    commonMsg: {},
    stateFlg: false,
    // week: [],
    gender: [],
    timezone: [],
    purpose: [],
    position: [],
    averageAge: [],
    exWidth: [],
    feature: [],
    iconList: [],
    overFlowFlg: false,
    ex_width: [],
    checkWeek: {
      '0': [],
      '1': [],
      '2': [],
      '3': [],
      '4': [],
      '5': [],
      '6': [],
    },
  },
  getters: {
    getComList (state) {
      return function (key) {
        return state[key]
      }

    }
  },
  mutations: {
    constListData:function (state, payload) {
      state.stateFlg = true;
      // state.week = payload.week;
      state.gender = payload.gender;
      state.timezone = payload.time_zone;
      state.purpose = payload.purpose;
      state.averageAge = payload['average_age'];
      state.feature = payload.feature;
      state.ex_width = payload['experience'];
      state.position = payload.position;
      state.level = payload.level;
      state.iconList = payload['icon'];
    },
    setWeek (state, data) {
      state.checkWeek = data;
    },
    setWeekCol (state, data) {
      let tmp = state.checkWeek;
      if (tmp[data.week_id].indexOf(data.time_id) === -1) {
        tmp[data.week_id].push(data.time_id);
      } else {
        tmp[data.week_id].splice(tmp[data.week_id].indexOf(data.time_id), 1);
      }
      state.checkWeek = tmp;
    },
    setWeekHead (state, data) {
      let tmp = state.checkWeek;

      if (state.checkWeek[data.week_id].length === 4) {
        state.checkWeek[data.week_id] = []
      }
      else{
        for (let i in state.timezone) {
          let t = state.timezone[i].val;
          if (tmp[data.week_id].indexOf(t) === -1) {
            tmp[data.week_id].push(t);
          }
        }
      }
      state.checkWeek = tmp;
    },
    setTimeHead (state, data) {
      let cnt = 0;
      let tmp = state.checkWeek;
      for (let i in state.week) {
        let w = String(i);
        if (tmp[w].indexOf(data.time_id) === -1) {
          tmp[w].push(data.time_id);
        } else {
          cnt += 1;
        }
      }
      if (cnt === 7) {
        for (let i in state.week) {
          let w = String(i);
          tmp[w].splice(tmp[w].indexOf(data.time_id), 1);
        }
      }
      state.checkWeek = tmp;
    },
    overFlow (state, data) {
      state.overFlowFlg = data;
    },
    resetFlgData (state) {
      state.overFlowFlg = false;
    },
    resetAllCheckData (state) {

    },
    setMessage (state, data) {
      state.commonMsg = data;
    }
  },

  actions: {
    /**
     * 各共通情報の取得
     */
    async getConData ( { commit } ) {
      const data = {};
      let result = await api.post('/const/get_const_data');
      console.log(result);
      if (result.result_cd === '001') {
        commit('constListData', result.data);
      }

    },
    changeOverFlow ({commit}, data=false) {
      commit('overFlow', data);
    },
    setMessage ({commit}, data) {
      commit('setMessage', data);
    },
    resetFlg: function ({commit}) {
      commit('resetFlgData');
    }
  }
}
