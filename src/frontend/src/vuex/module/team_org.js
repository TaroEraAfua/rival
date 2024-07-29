import api from '../api/api.js'

export default {
  namespaced: true,
  state: {
    teamList: [],
    teamImgList: [],
    teamId:'',
    checkPro: 0,
    checkAdvanced: 0,
    checkIntermediate: 0,
    checkElementary: 0,
    checkBeginner: 0,
    teamImageData: '',
    teamImageName: '',
    teamName: '',
    searchType: 0,
    totalCount: 0,
    weekList: [],
    searchFlg: false,
    teamInfo: {},
    teamWeek: [],
    teamMember: [],
    teamMemberList: [],
    checkGym: 0,
    mainPlace: '',
    memberNum: null,
    checkStray: 0,
    solicitation: 0,
    teamCount: 0,
    registerFlg: false
  },

  getters: {
    resultTeamList (state) {
      return state.teamList
    },
    resultTeamId (state) {
      return state.teamId
    },
    resultWeekList (state) {
      return state.weekList
    },
    resultTeamMemberList (state) {
      return state.teamMemberList
    },
    resultTeamImgList (state) {
      return state.teamImgList
    },
    checkPro (state) {
      return state.checkPro
    },
    checkAdvanced (state) {
      return state.checkAdvanced
    },
    checkIntermediate (state) {
      return state.checkIntermediate
    },
    checkElementary (state) {
      return state.checkElementary
    },
    checkBeginner (state) {
      return state.checkBeginner
    },
    checkTeamImageData (state) {
      return state.teamImageData
    },
    checkTeamImageName (state) {
      return state.teamImageName
    },
    checkTeamName (state) {
      return state.teamName
    },
    checkSearchType (state) {
      return state.searchType
    },
    checkTotalCount (state) {
      return state.totalCount
    },
    checkSearchFlg (state) {
      return state.searchFlg
    },
    getTeamInfo(state) {
      return state.teamInfo
    },
    getTeamWeek(state) {
      return state.teamWeek
    },
    getTeamMember(state) {
      return state.memberNum
    },
    getGym(state) {
      return state.checkGym
    },
    getTeamMemberNum(state) {
      return state.memberNum
    },
    getMainPlace(state) {
      return state.mainPlace
    },
    getStray(state) {
      return state.checkStray
    },
    getSolicitation(state) {
      return state.solicitation
    },
    getTeamCount (state) {
      return state.teamCount
    },
    getRegisterFlg (state) {
      return state.registerFlg
    }
  },

  mutations: {
    teamListData (state, payload) {
      console.log(payload)
      state.totalCount = payload.count
      state.weekList = payload.week
      let member = payload.prof
      let team_id = sessionStorage.signInId
      for (let i = 0; i < member.length; i++) {
        if (!team_id) {
          member[i].btn = null
        } else if (member[i].status === 1) {
          member[i].btn  = {
            type: true,
            title: 'マッチングしてるよ'
          }
        } else if (member[i].send_team_id === team_id) {
          member[i].btn = {
            type: false,
            title: '取り消すよ'
          }
        } else if (member[i].res_team_id === team_id) {
          member[i].btn = {
            type: false,
            title: '挑戦状を受ける'
          }
        } else {
          member[i].btn = {
            type: false,
            title: '挑戦状を叩きつける'
          }
        }
      }
      state.teamList = member

    },
    checkProData (state, payload) {
      state.checkPro = parseInt(payload)
    },
    checkAdvancedData (state, payload) {
      state.checkAdvanced = parseInt(payload)
    },
    checkIntermediateData (state, payload) {
      state.checkIntermediate = parseInt(payload)
    },
    checkElementaryData (state, payload) {
      state.checkElementary = parseInt(payload)
    },
    checkBeginnerData (state, payload) {
      state.checkBeginner = parseInt(payload)
    },
    checkTeamImageData (state, payload) {
      state.teamImageData = payload
    },
    setImageName (state, payload) {
      state.teamImageName = payload
    },
    checkTeamNameData (state, payload) {
      state.teamName = payload
    },
    searchTypeData (state, payload) {
      state.search_type = payload
    },
    searchFlg (state, payload) {
      state.searchFlg = payload
    },
    resetAllCheckData (state) {
      state.checkPro = 0
      state.checkAdvanced = 0
      state.checkIntermediate = 0
      state.checkElementary = 0
      state.checkBeginner = 0
      state.teamList = []
      state.weekList = []
    },
    setTeamInfo (state, payload) {
      state.teamInfo = payload.profile[0]
      state.teamWeek = payload.week
      state.teamMember = payload.member
    },
    setTeamCount (state, payload) {
      state.teamCount = payload
    },
    sendFlg (state, payload) {
      state.teamList[payload.col].btn = {
        type: payload.flg,
        title: payload.title
      }
    },
    setTeamId (state, payload) {
      state.teamId = payload
    },
    setGymData (state, payload) {
      state.checkGym = payload
    },
    setMainPlace (state, payload) {
      state.mainPlace = payload
    },
    setTeamMemberNum (state, payload) {
      state.memberNum = parseInt(payload)
    },
    setStrayData (state, payload) {
      state.checkStray = payload
    },
    setSolicitationData (state, payload) {
      state.solicitation = payload
    },
    setAllTeam(state, payload) {
      state.teamList = payload.team
      state.teamCount = payload.count
    },
    setRegisterFlg(state, payload) {
      state.registerFlg = payload
    }
  },

  actions: {
    /**
     * チーム検索の結果を取得
     */
    getDetailTeamList ({ commit }, payload) {
      commit('searchTypeData', 0)
      api.post('/team/search_detail', payload)
        .then((res) => {
          let result = res.data
          console.log(result)
          console.log(typeof result);
          commit('teamListData', result)

        })
    },
    /**
     * チーム検索の結果を取得
     */
    getDateTeamList ({ commit }, payload) {
      commit('searchTypeData', 1)
      api.post('/team/search_date', payload)
        .then((res) => {
          let result = res.data
          commit('teamListData', result)

      })
    },
    async setTeamData ({ commit }, data) {
      await api.post('/team/add_account', data)
        .then((res) => {
          let result = res.data
          if (result.status === 200) {
            commit('setRegisterFlg', true)
          } else {
            alert("SERVER ERR")
          }
        })
    },
    async updateGameDate ({ commit }, data) {
      await api.post('/team/update_game_date', data)
        .then((res) => {
          alert("登録したよ")
        })
    },
    async getAllTeamData ({ commit }, data) {
      await api.post('/team/get_all', data)
        .then((res) => {
          let result = res.data
          commit('setAllTeam', result)
        })
    },
    getTeam ({ commit }, param) {
      const data = {
        team_id: sessionStorage.signInId
      }
      let prof = null
      api.post('/team/get_team_info', data)
        .then((res) => {
          prof = res.data
          commit('setTeamInfo', prof)
      })
    },
    updateTeamInfo ({ commit }, param) {
      let prof = null
      api.post('/team/update_team_info', param)
        .then((res) => {
          prof = res.data
          commit('setTeamInfo', prof)
        })
    },
    getCountTeamAll ({ commit }, param) {

      let prof = null
      api.post('/team/get_all', param)
        .then((res) => {
          prof = res.data
          commit('setTeamCount', prof['count'])
        })
    },
    setCheckProData ({ commit }, payload) {
      commit('checkProData', payload)
    },
    setCheckAdvancedData ({ commit }, payload) {
      commit('checkAdvancedData', payload)
    },
    setCheckIntermediateData ({ commit }, payload) {
      commit('checkIntermediateData', payload)
    },
    setCheckElementaryData ({ commit }, payload) {
      commit('checkElementaryData', payload)
    },
    setCheckBeginnerData ({ commit }, payload) {
      commit('checkBeginnerData', payload)
    },
    setCheckTeamNameData ({ commit }, payload) {
      commit('checkTeamNameData', payload)
    },
    setCheckTeamImageData ({ commit }, payload) {
      commit('checkTeamImageData', payload)
    },
    setImageName  ({ commit }, payload) {
      commit('setImageName', payload)
    },
    setSearchType ({ commit }, payload) {
      commit('searchFlg', payload)
    },
    setSendFlg ({ commit }, payload) {
      commit('sendFlg', payload)
    },
    checkTeamId ({ commit }, payload) {
      commit('setTeamId', payload)
    },
    resetTeamAllCheck ({ commit }) {
      commit('resetAllCheckData')
    },
    setGym ({ commit }, payload) {
      commit('setGymData', payload)
    },
    setMainPlace ({ commit }, payload) {
      commit('setMainPlace', payload)
    },
    setTeamMemberNum({ commit }, payload) {
      commit('setTeamMemberNum', payload)
    },
    setStray({ commit }, payload) {
      commit('setStrayData', payload)
    },
    setSolicitation({ commit }, payload) {
      commit('setSolicitationData', payload)
    },
    setRegisterFlg({commit}) {
      commit('setRegisterFlg', true)
    }
  }
}
