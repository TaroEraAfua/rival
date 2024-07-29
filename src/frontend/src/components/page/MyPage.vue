<template>
 <v-container class="my-page" fluid>
   <v-row>
     <div class="none-padding" :cols="sideRange">
       <side-menu
         v-if="checkTerminal"
         @changeSize="changeSize"
       />
     </div>
     <v-col>
       <v-row style="height: 100vh; margin: 0; overflow: auto;">

         <v-col class="mx-auto" cols="12" :md="11 - sideRange" >
           <common-info
             v-if="['user', 'team'].includes(infoData.type)"
             :formData="infoData"
           >
             <template slot="info-button-area">
               <template v-for="(value, key, index) in infoData.btn">
                 <v-btn rounded color="primary" dark
                        @click="onBtn(key)">
                   {{ value }}
                 </v-btn>
               </template>
             </template>
           </common-info>
           <challenge
             v-else-if="infoData.type === 'challenge'"
           />
           <chat
             v-else-if="infoData.type === 'chat'"
             :chat_id="infoData.chat_id"
             :title="infoData.title"
           />
           <team-edit
             v-else-if="infoData.type === 'addTeam' || infoData.type === 'editTeam'"
             :pageType="infoData.type"
             :targetData="infoData.list"
             :checkTerminal="checkTerminal"
           />
           <user-edit
             v-else-if="infoData.type === 'editUser'"
             :rootPage='rootPage'
             :checkTerminal="checkTerminal"
           />
           <update-pass
             v-else-if="infoData.type === 'updatePass'"
             :rootPage='rootPage'
             :checkTerminal="checkTerminal"
           />
           <game-date-edit
               v-else-if="infoData.type === 'gameDateEdit'"
               :rootPage='rootPage'
               :targetData="infoData.list"
               :checkTerminal="checkTerminal"
           />
         </v-col>

       </v-row>
     </v-col>

   </v-row>

 </v-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import formatMixin from "../common/formatMixin";
import ActionMixin from "../common/ActionMixin";
import SideMenu from "../form/SideMenu";
import CommonInfo from "../form/CommonInfo";
import Challenge from "../form/Challenge";
import Chat from "../form/Chat";
import TeamEdit from "./TeamEdit";
import UserEdit from "./UserEdit";
import UpdatePass from "../form/UpdatePass";
import GameDateEdit from "../form/GameDateEdit";
export default {
  name: 'MyPage',
  mixins: [formatMixin, ActionMixin, SideMenu],
  props: {
    checkTerminal: {
      type: Boolean,
      default: function () {
        return true
      }
    },
    rootPage:{
      type:String,
      default: function () {
        return ''
      }
    }
  },
  components: {
    GameDateEdit,
    SideMenu,CommonInfo,Challenge,Chat,TeamEdit,UserEdit,UpdatePass
  },
  data() {
    return {
      sideRange: 2,
      infoData: {
        title: '',
        list: {},
        format: {},
        btn: {},
        type: ''
      },
      infoItem: {
        user: {
          title: 'ユーザー情報',
          list: {},
          format: {},
          btn: {
            editUser: 'ユーザー編集',
            updatePass: 'パスワード更新'
         }
        },
        addTeam: {
          title: 'チーム作成',
          list: {},
          format: {}
        },
        editUser: {
          title: 'ユーザー編集',
          list: {},
          format: {},
          btn: { editUser: '編集' }
        },
        team: {
          title: 'チーム情報',
          list: {},
          format: {},
          btn: { editTeam: 'チーム編集', gameDateEdit: '試合日程編集'}
        },
        editTeam: {
          title: 'チーム編集',
          list: {},
          format: {},
          btn: { editTeam: '編集' }
        },
        challenge: {
          title: '挑戦状一覧',
          list: {},
          format: {}
        },
        chat: {
          title: 'チャット',
          chat_id: ''
        },
        updatePass: {
          title: 'パスワード更新',
          list: {},
          format: {}
        },
        gameDateEdit: {
          title: '試合日程編集',
          list: {},
          format: {}
        }
      }
    }

  },
  watch: {
    item: function(val){
    },
    menuPathList: {
      handler: function (to, from) {
        console.log('menuPathList');
        switch (to.main) {
          case "user":
            this.getUserInfo();
            break;
          case "team":
            this.getTeamInfo(to.sub);
            break;
          case "challenge":
            this.getChallengeInfo(to.sub);
            break;
          case "chat":
            this.getChatInfo(to.sub);
            break;
          case "addTeam":
            this.makeInfoParam('addTeam');
            break;
          case "editTeam":
            this.makeInfoParam('editTeam');
            this.$set(this.infoData, "type", 'editTeam');
            this.$set(this.infoData, "title", this.infoItem['editTeam']["title"]);
            this.$set(this.infoData, "list", to.sub);
            this.$set(this.infoData, "format", this.infoItem['editTeam']["format"]);
            const btn = Object.keys(this.infoItem['editTeam']).includes("btn") ? this.infoItem['editTeam']["btn"] : {} ;
            this.$set(this.infoData, "btn", btn);
            break;
          case "editUser":
            this.makeInfoParam('editUser');
            break;
          case "updatePass":
            this.$set(this.infoData, "type", 'updatePass');
            this.$set(this.infoData, "title", this.infoItem['updatePass']["title"]);
            this.$set(this.infoData, "format", this.infoItem['updatePass']["format"]);
            break;
          case "gameDateEdit":
            this.$set(this.infoData, "type", 'gameDateEdit');
            this.$set(this.infoData, "title", this.infoItem['gameDateEdit']["title"]);
            this.$set(this.infoData, "format", this.infoItem['gameDateEdit']["format"]);
            this.$set(this.infoData, 'list', to.sub);
            break;
        }
      },
      deep: true
    },

  },
  computed:{
    ...mapState('auth', [
      'joinTeamList', 'userList', 'menuPathList'
    ]),
    ...mapState('constant', [
      'userInfo', 'teamInfo', 'challengeInfo'
      ]
    ),
    ...mapState('constant', [
      'pageOption', 'dialogContent'
    ]),
  },
  methods: {
    ...mapActions('auth', ['setSelectMenu', 'getUser']),
    ...mapActions('common', [
      'getConData'
    ]),
    getUserInfo: async function () {
      if (Object.keys(this.userList).length === 0) {
        await this.getViewData();
      }
      await this.getUser();
      this.$set(this.infoItem.user, 'list', this.userList);
      this.$set(this.infoItem.user, 'format', this.userInfo);
      this.makeInfoParam('user');
    },
    getTeamInfo: async function (sub) {
      if (this.joinTeamList.team === 0) {
        await this.getViewData();
      }
      this.$set(this.infoItem.team, 'list', this.joinTeamList.team[sub.idx]);
      this.$set(this.infoItem.team, 'format', this.teamInfo);
      await this.makeInfoParam('team');

    },
    onBtn: function (key) {
      switch (key) {
        case "editUser":
          this.setSelectMenu({
            path: this.$route.path,
            main: key,
            sub: null
          });
          break;
        case "editTeam":
          this.setSelectMenu({
            path: this.$route.path,
            main: key,
            sub: this.menuPathList.sub
          });
          break;
        case "updatePass":
          this.setSelectMenu({
            path: this.$route.path,
            main: key,
            sub: null
          });
          break;
        case "gameDateEdit":
          this.setSelectMenu({
            path: this.$router.path,
            main:key,
            sub: this.menuPathList.sub
          })
      }
      console.log(key);
    },
    changeSize: function (val) {
      this.sideRange = val;
    },
    getViewData: async function () {
      await this.getConData();
    },
    getChallengeInfo: async function () {
      this.$set(this.infoData, "type", 'challenge');
    },
    getChatInfo: async function (sub) {
      this.$set(this.infoData, 'chat_id', sub.chat_id);
      this.$set(this.infoData, 'title', sub.title);
      this.$set(this.infoData, "type", 'chat');
    },
    checkMenu: function () {
      switch (this.menuPathList.main) {
        case "user":
          this.getUserInfo();
          break;
        case "team":
          this.getTeamInfo(this.menuPathList.sub);
          break;
        case "challenge":
          this.getChallengeInfo(this.menuPathList.sub);
          break;
        case "chat":
          this.getChatInfo(this.menuPathList.sub);
          break;
        case "addTeam":
          this.makeInfoParam('addTeam');
          break;
        case "editTeam":
          break;
      }
    }
  },
  created () {
    this.checkMenu();
  }
}
</script>

<style lang="scss" scoped>
.my-page {
  padding: 0;
  min-height: 100vh;
  .side-menu {
    min-height: 100vh;
  }
}
</style>
