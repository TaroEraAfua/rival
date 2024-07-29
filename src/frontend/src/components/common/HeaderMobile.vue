<template>
  <v-sheet class='rival-header-mobile'>
    <v-navigation-drawer
      absolute
      permanent
    >
      <template v-slot:prepend>
        <template v-if="authFlg">
          <v-list-item two-line>
            <v-list-item-avatar>
              <v-img :src="userList.icon" />
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title> {{ userList.user_name }} </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <v-divider/>
      </template>




      <v-list dense>
        <template
          v-for="(row, key) in menu"

        >
          <v-list-item
            :key="key"
            v-if=" 'my_page' !== key "
            @click="movePage(key)"
          >
            <v-list-item-icon style="margin-left: 10px; margin-right: 10px;" >
              <v-icon>{{ row.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ row.label }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>

        <template v-if="authFlg">
          <sub-side-menu />
        </template>
      </v-list>
      <template v-slot:append>
        <div style="margin-bottom: 13vh;">
          <div class="pa-2">
            <v-btn block dark color="indigo" @click="onSignBtn(btnItem.path)">{{ btnItem.label }}</v-btn>
          </div>
          <div class="pa-2" v-if="!authFlg">
            <v-btn block color="blue-grey lighten-5" @click="movePage('/user_add')">アカウント作成</v-btn>
          </div>
          <div class="pa-2">
            <v-btn block color="blue-grey lighten-5" @click="onClose">close</v-btn>
          </div>
        </div>
      </template>
    </v-navigation-drawer>
  </v-sheet>
</template>

<script>
import { mapActions, mapGetters,mapState } from 'vuex'
import ActionMixin from "./ActionMixin";
import formatMixin from "./formatMixin";
import SubSideMenu from "../form/SubSideMenu";
export default {
  name: 'HeaderMobile',
  mixins: [ActionMixin,formatMixin],
  components: {
    SubSideMenu
  },
  data () {
    return {
      items: [
        { title: 'Home', icon: 'dashboard' },
        { title: 'About', icon: 'question_answer' },
      ],
      btnOption: {
        logOut: {label: 'ログアウト', flg: false, path: '/'},
        logIn: {label: 'ログイン', flg: true, path: 'login'},
      },
      btnItem : {}
    }
  },
  watch: {
    authFlg: function (flg) {
      this.btnItem = flg ? this.btnOption.logOut : this.btnOption.logIn;
    }
  },
  computed: {
    ...mapState('constant', ['menuList']),
    ...mapState('auth', ['authFlg', 'userList']),
    menu: function () {
      return this.menuList
    },
    changeSystemBtn: function () {
      for (let key in this.btnOption) {
        if (this.btnOption[key].flg === this.authFlg) {
          return this.btnOption[key]
        }
      }
    },
  },
  methods: {
    ...mapActions('common', ['changeOverFlow']),
    ...mapActions('auth', ['logOut']),
    /**
     * ログイン状態判定
     * @param path
     * @returns {Promise<void>}
     */
    onSignBtn: async function (path) {
      if (path === 'login') {
        this.movePage(path);
      } else {
        await this.movePage(path);
        await this.logOut();
        this.reload();
      }
    },

    async reload() {
      this.$router.go({path: this.$router.currentRoute.path, force: true});
    },
    /**
     * サイドメニュー閉じる
     */
    onClose: function () {
      this.changeOverFlow();
    }
  },
  created () {
    this.btnItem = this.authFlg ? this.btnOption.logOut : this.btnOption.logIn;
  }
}
</script>

<style lang='scss' scoped>
  .rival-header-mobile {
    width: 256px;
    background-color: white;
    z-index: 20;
    height: 100vh;
    position: absolute;
    overflow: hidden;
  }
</style>
