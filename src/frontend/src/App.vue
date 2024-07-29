<template>
  <v-app
    id="rival"
    :style="changeStyle"
    @keydown.esc="onkeydown"
  >
    <ViewMessage/>
    <div class="body">
      <v-container fluid class="main-container" >
        <v-sheet
          v-if="overFlowFlg"
          class="over-ray-color"
          @click="changeOverFlow(false)"
        >
        </v-sheet>
        <transition  name="head-fade">
          <header-mobile
            v-if="overFlowFlg"
          />
        </transition>

        <v-row style="margin: 0">
          <rival-header/>
        </v-row>
        <transition name="page-fade">
          <router-view
            :checkTerminal="mobileFlg"
            :rootPage="rootPage"
          />
        </transition>
        <v-container fluid class="footer-container">
          <rival-footer />
        </v-container>
      </v-container>
      <template v-if="joinTeamList.team.length > 0">
        <v-fab-transition>
          <v-btn
            class="change_team"
            key="success"
            color="success"
            fab
            large
            dark
            right
            @click="onTeam"
          >
            <v-icon>mdi-account-group-outline</v-icon>
          </v-btn>
        </v-fab-transition>
        <team-menu v-if="teamMenuFlg"/>
      </template>
    </div>

  </v-app>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex';
import rivalHeader from './components/common/Header';
import rivalFooter from './components/common/Footer';
import HeaderMobile from "./components/common/HeaderMobile";
import ActionMixin from "./components/common/ActionMixin";
import TeamMenu from "./components/form/TeamMenu";
import ViewMessage from "./components/form/ViewMessage";
//import store from './vuex';
export default {
  name: 'rival',
  mixins: [ActionMixin],
  components: {
    rivalFooter, rivalHeader, HeaderMobile, TeamMenu, ViewMessage
  },
  data() {
    return {
      rootFlg: false,
      mobileFlg: false,
      teamMenuFlg: false,
      rootPage: '',
    }
  },
  watch: {
    $route: function (to, from) {
      this.rootPage = to.path;
      this.initTarget(to.path, from.path);
      if (to !== from) {
        this.teamMenuFlg = false;
      }
    },
    commonMsg: function (to, from) {

    }
  },
  computed: {
    ...mapState('common', ['overFlowFlg', 'commonMsg']),
    ...mapState('auth', ['authFlg', 'joinTeamList']),
    changeStyle ( ) {
      return this.overFlowFlg ? 'height: 100vh; overflow: hidden;' : ''
    }
  },
  mounted() {
    window.onload=function(){
      document.getElementById("rival").addEventListener('keydown',function(){
        //"b"（keyCode=27）escが押された場合は入力を無効にする
        if(process.env.NODE_ENV === 'production' && (event.keyCode === 27 || event.keyCode === 123)) {
          event.preventDefault();
        }
      });
    };
    document.oncontextmenu = function () {
      return process.env.NODE_ENV === 'development';
    };
    this.mobileFlg = this.checkMobile();
  },
  methods: {
    ...mapActions('common', ['changeOverFlow']),
    ...mapActions('auth', ["getUser", "initLoginParam"]),
    ...mapActions('team', ['initSearchTeamList', "initSearchDetailParam", "initSearchDateParam"]),
    /**
     * 認証情報、定数取得
     * @returns {Promise<void>}
     */
    checkAuth: async function () {
      if (this.authFlg) {
        await this.getUser();
      }
    },
    initTarget: function (to, from) {
      this.initSearchDetailParam();
      this.initSearchDateParam();
      this.initLoginParam();
      if (to === '/search' && from === '/') {
      } else {
        this.initSearchTeamList();
      }
    },
    keyDown: function (e) {
      console.log('key');
      console.log(e);
    },
    onTeam: function () {
      this.teamMenuFlg =! this.teamMenuFlg;
    }
  },
  created() {
    this.checkAuth();
    this.rootPage = this.$route.path;
  },

}
</script>

<style lang="scss">
  #rival {
    padding: 0;
    overflow: hidden;

    .body {
      position: relative;
      overflow: auto;
      flex-direction: column;
      display: flex;
      .change_team {
        bottom: 10px;
        position: fixed;
        right: 10px;
        z-index: 4;
      }
      .main-container {
        padding: 0;
        margin: 0;
        /*width: 100vw;*/
        overflow: auto;
      }
      .footer-container {
        padding: 0;
        margin: 0;
        width: 100vw;
      }
      .none-padding {
        padding: 0;
      }
      .col-span {
        padding: 3px 1px 1px 1px;
      }
      .over-ray-color {
        z-index: 5;
        opacity: 0.46;
        background-color: rgb(33, 33, 33);
        border-color: rgb(33, 33, 33);
        border-radius: inherit;
        bottom: 0;
        height: 100%;
        left: 0;
        position: absolute;
        right: 0;
        top: 0;
        -webkit-transition: inherit;
        transition: inherit;
        width: 100%;
        will-change: opacity;
      }
      .head-fade-enter-active {
        transition: all .3s ease;
      }

      .head-fade-leave-active {
        transition: all .3s ease;
      }

      .head-fade-enter, .head-fade-leave-to
        /* .slide-fade-leave-active below version 2.1.8 */
      {
        transform: translateX(10px);
        opacity: 0;
      }
      .page-fade-enter-active {
        transition: all .3s ease;
      }

      .page-fade-leave-active {
        transition: all .3s ease;
      }

      .page-fade-enter, .page-fade-leave-to
        /* .slide-fade-leave-active below version 2.1.8 */
      {
        transform: translateX(10px);
        opacity: 0;
      }
    }
    ::v-deep .row {
      margin: 0;
    }

    h4 {
      padding: .25em 0 .25em .75em;
      border-left: 6px solid #ffaa1a;
    }
    .main-body {
      min-height: 80vh;
    }
    .border-test1 {
      border: 1px solid black;
    }
    .border-test1 {
      border: 1px solid blue;
    }
    .border-test2 {
      border: 1px solid red;
    }
    .main-footer{position:-webkit-sticky; position:sticky; bottom:0; border-color:red;}
    img {
      width: 100px;
      margin: auto;
      border-color: gray;
      border-bottom: medium solid;
    }
  }


</style>
