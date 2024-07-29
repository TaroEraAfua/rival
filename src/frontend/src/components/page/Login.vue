<template>
 <v-container fluid style="height: 80vh" class="login-page">
   <v-row style="height: 80vh;">
     <v-card
     :max-height='320'
     :min-height='320'
     :max-width='250'
     :min-width='250'
     class="login-card mx-auto">
     <v-container>
       <v-row>
         <v-col style="padding: 0;">
           <v-card-title>
             <v-img
               :src="image_src"
               class="login-logo"
               max-width="70"
               max-height="70"
               dark
             >
             </v-img>
           </v-card-title>
         </v-col>
       </v-row>
    <v-row class="login-row">
      <v-col>
        <base-input-text
        :hints="userId.hints"
        :keyName="userId.keyName"
        :param="userId.param"
        :option="userId.option"
        @changeForm="changeForm"
        />
      </v-col>
    </v-row>
    <v-row class="login-row">
      <v-col>
        <base-input-text
        :hints="passWord.hints"
        :keyName="passWord.keyName"
        :param="passWord.param"
        :option="passWord.option"
        @changeForm="changeForm"
        @keydown.enter="onLogIn"
        />
      </v-col>
    </v-row>
    <v-row class="login-row">
      <p class='error-message'>{{ errAuthMsg }}</p>
    </v-row>
    <v-row>
      <v-col style="padding-top: 0;">
        <v-btn block dark color="indigo" @click='onLogIn'>ログイン</v-btn>
      </v-col>
    </v-row>
    </v-container>
     </v-card>
   </v-row>
 </v-container>
</template>

<script>
  import { mapActions, mapState, mapGetters } from 'vuex'
  import formatMixin from "../common/formatMixin";
  import ActionMixin from "../common/ActionMixin";
  import BaseInputText from "../part/BaseInputText";
  export default {
    name: 'login',
    mixins: [formatMixin, ActionMixin],
    components: {
      BaseInputText
    },
    data() {
      return {
        userId: {
          keyName: 'user_id',
          hints: 'ユーザーID',
          param: '',
          option: {}
        },
        passWord: {
          keyName: 'password',
          hints: 'パスワード',
          param: '',
          option: {formType: 'password'}
        },
        image_src: require('../common/images/logo.png')
      }
    },
    watch: {
      authFlg: function(to, from){
        if (to) {
          this.movePage('/');
        }
      }
    },
    computed: {
      ...mapState('auth', ['errAuthMsg', 'authFlg']),
    },
    mounted() {
    },
    methods: {
      ...mapActions('auth', [
        'logIn', 'setLoginParam'
      ]),
      onLogIn :async function() {
        await this.logIn();
      },
      changeForm : function(data) {
        this.setLoginParam(data);
      },
    },
    created() {

    }
  }
</script>

<style lang="scss" scoped>
.login-page {
  .login-card {
    background-color: rgb(245, 245, 245);
    margin-top: 10vh;
    .login-row {
      margin: auto;
      height: 50px;
      margin-bottom: 3px;
      .error-message {
        color: red;
        margin: auto;
        text-align: center;
        font-size: 14px;
      }

    }
    .login-logo {
      border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
      margin: auto;
      background-position: left top;  /* 横長画像の左上を基準に表示 */
      display: inline-block;
    }
  }

}

</style>
