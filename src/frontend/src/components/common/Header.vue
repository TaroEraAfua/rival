<template>
  <v-app-bar
    dense
    flat
    class="rival-header"
    style="background: rgba(25, 0, 0, 0.25);"
  >
    <v-app-bar-nav-icon
      v-if="!checkMobileState"
      style="margin-left: 1vw"
      @click="onMenu"
    />

    <v-toolbar-title @click="movePage('/')">
      <a style="margin-left: 1vw; color: red;">Rival </a>
    </v-toolbar-title>

    <template v-if="checkMobileState" v-for="(row, key) in menuList">
      <v-btn
        v-if=" authFlg "
        text
        @click="onAuthHeaderBtn(key)"
      >
        <a style="color: red;"> {{ row.label }} </a>
      </v-btn>
      <v-btn
        v-else-if=" 'my_page' !== key "
        text
        @click="movePage('/' + key)"
      >
        <a style="color: red;"> {{ row.label }} </a>
      </v-btn>
    </template>
    <v-spacer />

    <v-btn
      v-if="checkMobileState"
      icon
      @click="onUser"
      style="margin-right: 7px"
    >
      <v-icon>mdi-account-circle-outline</v-icon>
    </v-btn>
    <transition class="user-fade">
      <v-card
        v-if="menuFlg"
        class="user-card"
        @blur="onUser"
      >
        <template  v-if="authFlg">
          <v-card-title>
            <v-img
              :src="userList.icon"
              class="user-image"
              max-width="70"
              max-height="70"
              dark
            >
            </v-img>
          </v-card-title>
          <v-card-title style="padding: 0;">
            <p style="margin: auto"> {{ userList.user_name }} </p>
          </v-card-title>
          <v-divider class="mx-4" />
          <template v-if="itemList.length > 0">
            <v-list dense>
              <v-list-item-group v-model="item" color="primary">
                <v-list-item
                  v-for="(item, i) in itemList"
                  :key="i"
                  @click="selectItem(item.team_id)"
                >
                  <v-list-item-icon
                    style="margin-bottom: 0px"
                  >
                    <v-img
                      class="team-image"
                      :src="item.icon"
                      dark
                    />
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title> {{ item.title }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </template>
          <template v-else>
            <div class="pa-2" >
              <v-btn block color="blue-grey lighten-5" @click="onAddTeam">チーム作成</v-btn>
            </div>
          </template>
        </template>
        <div class="pa-2">
          <v-btn block dark color="indigo" @click="onSignBtn(btnItem.path)">{{ btnItem.label }}</v-btn>
        </div>
        <div class="pa-2" v-if="!authFlg">
          <v-btn block color="blue-grey lighten-5" @click="movePage('/user_add')">アカウント作成</v-btn>
        </div>
        <div class="pa-2">
          <v-btn block color="blue-grey lighten-5" @click="onUser">close</v-btn>
        </div>
      </v-card>
    </transition>



  </v-app-bar>
</template>

<script>
import { mapActions, mapGetters,mapState } from 'vuex'
import formatMixin from "./formatMixin";
import ActionMixin from './ActionMixin'
export default {
  name: 'Header',
  mixins: [formatMixin, ActionMixin],
  components: {
  },
  data () {
    return {
      menuFlg: false,
      image_src: require('./images/logo.png'),
      mobileFlg: false,
      item: 1,
      itemList: [],
      btnOption: {
        logOut: {label: 'ログアウト', flg: false, path: '/'},
        logIn: {label: 'ログイン', flg: true, path: 'login'},
      },
      btnItem : {}
    }
  },
  watch: {
    item: function (to, from) {
    },
    authFlg: function (flg) {
      this.btnItem = flg ? this.btnOption.logOut : this.btnOption.logIn;
      this.makeMenuList(this.joinTeamList);
    },
    $route: function (to, from) {
      if (to !== from) {
        this.menuFlg = false;
      }
    },
    joinTeamList: {
      handler: function (to, from) {
        this.makeMenuList(to);

      },
      deep: true
    }
  },
  computed: {
    ...mapState('constant', ['menuList']),
    ...mapState('auth', ['authFlg', 'userList', 'joinTeamList']),
    checkMobileState () {
      return this.checkMobile();
    },
    changeSystemBtn: function () {
      for (let key in this.btnOption) {
        if (this.btnOption[key].flg === this.authFlg) {
          return this.btnOption[key]
        }
      }
    }
  },
  methods: {
    ...mapActions('common', ['changeOverFlow']),
    ...mapActions('auth', ['logOut','setDefaultTeam']),
    onAuthHeaderBtn: function (key) {
      switch (key) {
        case 'my_page':
          this.movePage('/' + key, 'user');
          break;
        default:
          this.movePage('/' + key);
          break;
      }
    },
    onMenu: function () {
      this.changeOverFlow(true);
    },
    onUser: function () {
      this.menuFlg =!this.menuFlg;
    },
    makeMenuList: function (teamList) {
      let tmp = [];
      for (let idx in teamList.team) {
        if (teamList.select === teamList.team[idx].team_id) {
          this.item  = Number(idx);
        }
        tmp.push({
          team_id: teamList.team[idx].team_id,
          title: teamList.team[idx].team_name,
          icon: teamList.team[idx].team_image,
        })
      };
      this.itemList = tmp;
    },
    selectItem: function (id) {
      if(id === this.joinTeamList.select) {
        id = ''
      }
      this.setDefaultTeam(id);
    },
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
    onAddTeam: async function () {
      this.movePage('/my_page', 'addTeam', null);
    }
  },
  created () {
    this.btnItem = this.authFlg ? this.btnOption.logOut : this.btnOption.logIn;
    if ( this.authFlg ) {
      this.makeMenuList(this.joinTeamList);
    } else {

    }

  }
}
</script>

<style lang='scss' scoped>
  .rival-header {
    background: rgba(25, 0, 0, 0.25);
    position: relative;
    z-index: 10;
    .user-card {
      position: absolute;
      width: 300px;
      height: auto;
      top: 6px;
      right: 1vw;
      .user-image {
        border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
        margin: auto;
        background-position: left top;  /* 横長画像の左上を基準に表示 */
        display: inline-block;
      }
      .team-image {
        border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
        height: 30px;
        width: 30px;
        background-position: left top;  /* 横長画像の左上を基準に表示 */
        display: inline-block;
      }
    }

    .user-fade-enter-active {
      transition: all .3s ease;
    }
    .user-fade-leave-active {
      transition: all .3s ease;
    }
    .user-fade-enter, .slide-fade-leave-to
      /* .slide-fade-leave-active below version 2.1.8 */ {
      transform: translateX(10px);
      opacity: 0;
    }
  }
</style>
