<template>
 <v-container fluid class="chat">
   <v-card class="chat-body">
     <v-card-title style="background-color: white;">
       {{ title }}
     </v-card-title>
     <v-card-text>
      <v-row id="chat-message-body" style="height: 55vh; overflow: auto; ">
         <v-col style="background-color: #7da4cd;" cols="12">
           <template v-for="item in chatMessageList">
             <v-row v-if="!checkTeam(item.send_team_id) "
              class="balloon6"
                    :key="item.log_no"
             >
               <v-col cols="2" style="text-align: end; padding: 0 5px 0 5px;">
                 <p> {{ item.user_name }}</p>
               </v-col>
               <v-col cols="8"
                class="chatting"
               >
                 <div class="says">
                   <p> {{ item.message }}</p>
                 </div>
               </v-col>
             </v-row>
             <v-row
               v-else
               class="balloon6"
             >
               <v-col cols="2"></v-col>
               <v-col
                 cols="8"
                 class="mycomment"
                 style="text-align: end; padding: 0 5px 0 5px;"
               >
                 <div class="mycomment-say">
                   <p> {{ item.message }}</p>
                 </div>
               </v-col>
               <v-col style="text-align: start" cols="2" >
                 <p > {{ item.user_name }}</p>
               </v-col>
             </v-row>
           </template>
         </v-col>
      </v-row>
     </v-card-text>
     <v-row style="height: 13vh;">
       <v-col cols="12" style="padding-top: 0px; padding-bottom: 0px;">
         <v-textarea
           name="input-7-1"
           v-model="message"
           :rules="rules"
           solo
           flat
           :auto-grow="false"
           :outlined="false"
           style="min-height: 13vh; max-height: 13vh;"
         />
       </v-col>
     </v-row>
     <v-row>
       <v-col cols="12">
         <v-btn :disabled="message.length === 0 || message.length > 256 " block color="blue-grey lighten-5" @click="onChatBtn">送信</v-btn>
       </v-col>
     </v-row>
   </v-card>
 </v-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import formatMixin from "../common/formatMixin";
import ActionMixin from "../common/ActionMixin";
import SideMenu from "./SideMenu";
import CommonInfo from "./CommonInfo";
export default {
  name: 'MyPage',
  mixins: [formatMixin, ActionMixin, SideMenu],
  components: {
    SideMenu,CommonInfo
  },
  props: {
    chat_id: {
      type: [String,Number],
      default: function () {
        return ''
      }
    },
    title: {
      type: String,
      default: function () {
        return ''
      }
    }
  },
  data() {
    return {
      chatList: {
      },
      message: '',
      rules: [v => v.length <= 256 || '256文字以下で入力してください'],
    }

  },
  watch: {
    chat_id: {
      handler: function (to, from) {
        this.getChatLog(to);
      },
      deep: true
    }
  },
  computed:{
    ...mapState('auth', [
      'joinTeamList', 'userList'
    ]),
    ...mapState('chat', ['chatMessageList'])
  },
  methods: {
    ...mapActions('auth', ['getUser', 'setSelectMenu']),
    ...mapActions('chat', ['getChatMessage', 'sendChatMessage']),
    checkTeam: function (team_id) {
      return team_id === this.joinTeamList.select
    },
    getChatLog: async function (id) {
      await this.getChatMessage(id);
      this.chatList = this.chatMessageList;
      const element = document.getElementById('chat-message-body')
      const bottom = element.scrollHeight - element.clientHeight
      element.scrollTop = bottom
    },
    onChatBtn: async function () {
      if (this.message.length <= 256) {
        let param = {
          'challenge_id': this.chat_id,
          'team_id': this.joinTeamList.select,
          'user_id': this.userList.user_id,
          'message': this.message,
        };
        await this.sendChatMessage(param);
        this.message = '';
        this.getChatLog(this.chat_id);
      }

    }
  },
  created () {
    this.getChatLog(this.chat_id);
  }
}
</script>

<style lang="scss" scoped>
  .chat{
    min-height: 90vh;
    height: auto;
    .chat-body {
      height: 70vh;
      background-color: #7da4cd;
      .balloon6 {
        width: 100%;
        margin: 10px 0;
        overflow: hidden;
        .faceicon {
          float: left;
          margin-right: -50px;
          width: 40px;
        }
        .chatting {
          width: 100%;
          text-align: left;
        }
        .says {
          display: inline-block;
          position: relative;
          //margin: 0 0 0 50px;
          padding: 10px;
          max-width: 250px;
          border-radius: 12px;
          background: #edf1ee;
          p {
            white-space:pre-wrap;
            word-wrap:break-word;
            margin: 0;
            padding: 0;
          }
        }

        .says:after {
          content: "";
          display: inline-block;
          position: absolute;
          top: 3px;
          left: -19px;
          border: 8px solid transparent;
          border-right: 18px solid #edf1ee;
          -webkit-transform: rotate(35deg);
          transform: rotate(35deg);
        }
      }
      .mycomment {
        margin: 10px 0;
        .mycomment-say {
          white-space:pre-wrap;
          word-wrap:break-word;
          display: inline-block;
          position: relative;
          margin: 0 10px 0 0;
          padding: 8px;
          max-width: 250px;
          border-radius: 12px;
          background: #30e852;
          font-size: 15px;
          p {
            white-space:pre-wrap;
            word-wrap:break-word;
            text-align: start;
            margin: 0;
            padding: 0;
          }
        }
        .mycomment-say:after {
          content: "";
          position: absolute;
          top: 3px;
          right: -19px;
          border: 8px solid transparent;
          border-left: 18px solid #30e852;
          -webkit-transform: rotate(-35deg);
          transform: rotate(-35deg);
        }

      }
    }
  }
</style>
