import Vue from 'vue'
import Vuex from 'vuex'
import auth from './module/auth'
import area from './module/area'
import team from './module/team'
import chat from './module/chat'
import challenge from './module/challenge'
import common from './module/common'
import user from './module/user'
import constant from './module/constant'
import pageContent from "./module/pageContent";

Vue.use(Vuex);
const crypto = require('crypto');
const encoding = require('encoding-japanese');
const actions = {
  SET_STATE: function ({commit}) {
    commit('RDS_ENCRYPT');
  }
};
const base64Encode = function (...parts) {
  return new Promise(resolve => {
    const reader = new FileReader();
    reader.onload = () => {
      const offset = reader.result.indexOf(",") + 1;
      resolve(reader.result.slice(offset));
    };
    reader.readAsDataURL(new Blob(parts));
  });
};
const mutations = {
  // State初期化用
  RESET_VUEX_STATE (state) {
    console.log("RESET_VUEX_STATE");
    let decipher = crypto.createDecipher('aes-256-ctr', sessionStorage.token);
    let dec = decipher.update(sessionStorage.getItem('ini'),'hex','utf8');
    dec += decipher.final('utf8');
    Object.assign(state, JSON.parse(dec));
    console.log(state);
  },
  // ブラウザリロード
  RELOAD_STATE (state) {
    console.log("RESET_VUEX_STATE");
    let decipher = crypto.createDecipher('aes-256-ctr', sessionStorage.token);
    let dec = decipher.update(sessionStorage.getItem('rds'),'hex','utf8');
    dec += decipher.final('utf8');
    Object.assign(state, JSON.parse(dec));
  },
  // 画面遷移時、state設定
  RDS_ENCRYPT (state) {
    let cipher = crypto.createCipher('aes-256-ctr', sessionStorage.token);
    let crypt = cipher.update(JSON.stringify(state),'utf8','hex');
    crypt += cipher.final('hex');
    sessionStorage.setItem('rds', crypt);
  },
  // 初期値設定
  INI_ENCRYPT (state) {

    const PASSWORD = crypto.randomBytes(32);
    const SALT = crypto.randomBytes(16);
    // const key = crypto.scryptSync(PASSWORD, SALT, 32);
    let key = base64Encode(PASSWORD);
    sessionStorage.setItem('token', key);

    let cipher = crypto.createCipher('aes-256-ctr', sessionStorage.token);
    let crypt = cipher.update(JSON.stringify(state),'utf8','hex');
    crypt += cipher.final('hex');
    sessionStorage.setItem('ini', crypt);
  },
};

export default new Vuex.Store({
  actions: actions,
  mutations: mutations,
  modules: {
    auth,
    area,
    user,
    team,
    common,
    chat,
    challenge,
    pageContent,
    constant
  },
  strict: true
})
