import api from '@/vuex/api/api';

export default {
  namespaced: true,
  state: {
    teamList: {
      prof: [],
      count: 1
    },
    search_detail: {
      user: '',
      team: '',
      prefecture: '',
      city: '',
      station: '',
      line: '',
      gender: '',
      purpose: [],
      page: 1
    },
    search_date: {
      user: '',
      team: '',
      prefecture: '',
      city: '',
      station: '',
      line: '',
      date: [],
      page: 1
    },
    teamAddApiParam: {
      team_id: '',
      team_name: '',
      user_id: '',
      admin: 1,
      image: {},
      prefecture: '',
      city: '',
      station: {
        line_id: null,
        station_id: null
      },
      gender: '',
      purpose: '',
      feature: [],
      game_date: [],
      gym: '',
      stray_flg: null,
      average_age: null,
      main_place: '',
      member_num: null,
      solicitation: null,
      c_comment: '',
      u_comment: '',
    },
    teamEditErrMsg: {},
    gameDateEditApiParam: []
  },
  mutations: {
    resultSearch: function (state, data) {
      state.teamList = data
    },
    setDetailApiParam: function (state, data=null) {
      if (data) {
        for (let key in data) {
          let row = data[key];
          if (row) {
            state.search_detail[row.key] = row.val;
          }
        }
      } else {
        state.search_detail = {
          user: '',
          team: '',
          prefecture: '',
          city: '',
          station: '',
          line: '',
          gender: '',
          purpose: [],
          page: 1
        };
      }
    },
    setDateApiParam: function (state, data=null) {
      if (data) {
        for (let key in data) {
          let row = data[key];
          if (row) {
            state.search_date[row.key] = row.val;
          }
        }
      } else {
        state.search_date = {
          user: '',
          team: '',
          prefecture: '',
          city: '',
          station: '',
          line: '',
          date: [],
          page: 1
        };
      }
    },
    setEditErr: function (state, data={}) {
      state.teamEditErrMsg = data;
    },
    setAddApiParam: function (state, data=null) {
      if (data) {
        for (let key in data) {
          let row = data[key];
          if (row) {
            state.teamAddApiParam[row.key] = row.val;
          }
        }
      } else {
        state.teamAddApiParam = {
            team_id: '',
            team_name: '',
            user_id: '',
            admin: 1,
            image: {},
            prefecture: '',
            city: '',
            station: {
              line_id: null,
              station_id: null
            },
            gender: '',
            purpose: '',
            feature: [],
            game_date: [],
            gym: '',
            stray_flg: null,
            average_age: null,
            main_place: '',
            member_num: null,
            solicitation: null,
            c_comment: '',
            u_comment: '',
        }
      }

    },
    initTeamList: function (state) {
      state.teamList = {
        prof: [],
        count: 1
      }
    },
    setGameDateApiParam: function (state, data) {
      if (data) {
        state.gameDateEditApiParam = state.gameDateEditApiParam.concat(data);
      } else {
        state.gameDateEditApiParam = [];
      }
    },
    rowDeleteGameDate: function(state, index) {
      state.gameDateEditApiParam.splice(index, 1)
    },
    setGameDateApiRowParam(state, data) {
      state.gameDateEditApiParam[data.index][data.fieldName] = data.val;
    }

  },
  actions: {
    /**
     * チーム検索の結果を取得
     */
    getDetailTeamList: async function ({ commit, state }) {

      try {
        let result = await api.post('/team/search_detail', state.search_detail);
        if (result.result_cd === '001') {
          commit('resultSearch', result.data);
        }
      } catch (e) {

      } finally {
        commit('setDetailApiParam');
      }

    },
    /**
     * チーム検索の結果を取得
     */
    getDateTeamList: async function ({ commit, state }) {
      try {
        let result = await api.post('/team/search_date', state.search_date);
        if (result.result_cd === '001') {
          commit('resultSearch', result.data);
        }
      } catch (e) {

      } finally {

      }

    },
    addTeam: async function ( { commit, state } ) {
      commit('setEditErr');
      try {
        let result = await api.post('/team/add_account', state.teamAddApiParam);
        if (result.result_cd === '001') {
          commit('resultSearch', result.data);
        } else {
          commit('setEditErr', result);
        }
      } catch (e) {

      } finally {
        commit('setAddApiParam');
      }
    },
    editTeam: async function ( { commit, state } ) {
      commit('setEditErr');
      try {
        let result = await api.post('/team/update_team_profile', state.teamAddApiParam);
        if (result.result_cd === '001') {
          commit('resultSearch', result.data);
        } else {
          commit('setEditErr', result);
        }
      } catch (e) {

      } finally {
        commit('setAddApiParam');
      }
    },
    editGameDate: async function({commit, state}, data) {
      commit('setEditErr');
      console.log('editGameDate')
      let apiParam = {
        team_id: data.team_id,
        game_date: state.gameDateEditApiParam
      };
      try {
        let result = await api.post('/team/update_team_game_date', apiParam);
        if (result.result_cd === '001') {

        } else {
          commit('setEditErr', result);
        }
      } catch (e) {
        
      } finally {

      }
    },
    setSearchDetailParam: function ({commit}, data) {
      commit('setDetailApiParam', data)
    },
    setSearchDateParam: function ({commit}, data) {
      commit('setDateApiParam', data)
    },
    initSearchDetailParam: function ({commit}, data) {
      commit('setDetailApiParam');
    },
    initSearchDateParam: function ({commit}, data) {
      commit('setDateApiParam');
    },
    initSearchTeamList: function ({commit}) {
      commit('initTeamList');
    },
    setTeamAddApiParam: function ({commit}, data) {
      commit('setAddApiParam', data);
    },
    setTeamEditErrMsg: function ({commit}, data) {
      commit('setEditErr', data);
    },
    setGameDateApiParam: function ({commit}, data) {
      commit('setGameDateApiParam', data)
    },
    rowDeleteGameDate: function ({commit},index) {
      commit('rowDeleteGameDate', index)
    },
    setGameDateApiRowParam: function ({commit},data) {
      commit('setGameDateApiRowParam', data)
    }
  }

}
