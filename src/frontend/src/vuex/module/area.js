import api from '@/vuex/api/api';

export default {
  namespaced: true,
  state: {
    city: [],
    prefecture: [],
    station: [],
    checkStationId: 0,
    apiCity: {},
    apiStation: {},
  },
  getters: {
    getAreaList (state) {
      return function (key) {
        return state[key]
      }
    }
  },
  mutations: {
    setPrefectureData: function (state, param=null) {
      if (param) {
        state.prefecture = param.prefecture;
      } else {
        state.prefecture = [];
      }

    },
    setCityData: function (state, param=null) {
      if (param) {
        state.city = param.city;
      } else {
        state.city = [];
      }
    },
    setStation: function (state, param=null) {
      if (param) {
        state.station = param.station;
      } else {
        state.station = [];
      }
    },
    setCityApiParam: function (state, data) {
      state.apiCity = {id: data.val};
    },
    setStationApiParam: function (state, data) {
      state.apiStation = {
        prefecture_id: state.apiCity.id,
        city_name: data.param.label
      };
    }
  },

  actions: {
    /**
     * 都道府県のリストを取得
     */
    async getPrefecture ({ commit, state , dispatch}) {
      try {

        let result = await api.post('/area/get_prefecture', {test: 'あああ'});
        console.log(result);
        if (result.result_cd === '001') {
          commit('setPrefectureData', result.data);
          commit('setCityData');
          commit('setStation');
        } else {
          await dispatch('common/setMessage', result, {root: true})
        }

      } catch (e) {
        await dispatch('common/setMessage', result, {root: true})
      }　finally {

      }

    },

    /**
     * 市区町村のリストを取得
     */
    getCity: async function  ({ commit, state ,dispatch}) {
      try {
        let result = await api.post('/area/get_city', state.apiCity);
        if (result.result_cd === '001') {
          commit('setCityData', result.data);
          commit('setStation');
        } else {
          await dispatch('common/setMessage', result, {root: true});
        }
      } catch (e) {

      }
    },
    /**
     * 駅取得
     * @param commit
     * @param state
     * @returns {Promise<void>}
     */
    async getStation ({ commit, state }) {
      try {
        let result = await api.post('/area/get_station', state.apiStation);
        console.log(result);
        if (result.result_cd === '001') {
          commit('setStation', result.data);
        }
      } catch (e) {

      }
    },
    setAriaApiParam ({commit}, data) {
      if (data.key === 'city') {
        commit('setStationApiParam', data)
      } else {
        commit('setCityApiParam', data)
      }
    }
  }
}
