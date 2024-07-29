<template>
 <v-container fluid style="height: 80vh" class="change-page">
   <v-row style="height: 80vh;">
     <v-card
     :max-height='350'
     :min-height='350'
     :max-width='250'
     :min-width='250'
     class="change-card mx-auto">
     <v-container>
       <v-row>
         <v-col style="padding: 0;">
           <v-card-title>
             <p style="margin: auto;">パスワード更新</p>
           </v-card-title>
           <v-divider />
         </v-col>
       </v-row>
    <v-row class="change-row">
      <v-col>
        <base-input-text
        :hints="options.password_old.hints"
        :keyName="options.password_old.keyName"
        :param="options.password_old.param"
        :option="options.password_old.option"
        @changeForm="changeForm"
        />
      </v-col>
    </v-row>
    <v-row class="change-row">
      <v-col>
        <base-input-text
        :hints="options.password_new1.hints"
        :keyName="options.password_new1.keyName"
        :param="options.password_new1.param"
        :option="options.password_new1.option"
        @changeForm="changeForm"
        />
      </v-col>
    </v-row>
    <v-row class="change-row">
      <v-col>
        <base-input-text
        :hints="options.password_new2.hints"
        :keyName="options.password_new2.keyName"
        :param="options.password_new2.param"
        :option="options.password_new2.option"
        @changeForm="changeForm"
        />
      </v-col>
    </v-row>
    <v-row class="change-row">
      <p class='error-message'>{{ errAuthMsg }}</p>
    </v-row>
    <v-col :cols="12" align-self="center" class="text-center">
      <v-btn rounded color="primary" dark class="ma-2" @click='onPassEdit'>更新</v-btn>
    </v-col>
    </v-container>
     </v-card>
   </v-row>
 </v-container>
</template>

<script>
  import { mapActions, mapState, mapGetters } from 'vuex'
  import formatMixin from "../common/formatMixin";
  import ActionMixin from "../common/ActionMixin";
  import HorizontalForm from "./HorizontalForm";
  import BaseInputText from "../part/BaseInputText";
  import ConfirmationDialog from "../form/ConfirmationDialog";

  export default {
    name: 'UpdatePass',
    mixins: [formatMixin, ActionMixin],
    components: {
      BaseInputText, ConfirmationDialog
    },
    data() {
      return {
        options: {
          password_old: {
            base: 'text',
            hints: '今までパスワード',
            param: '',
            keyName: 'password_old',
            option: {formType: 'password'},
            col: { title: 4, content: 6},
            md: { title: 3, content: 4},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {
                ope: 'ge',
                count: 8
              }
            },
          },
          password_new1: {
            base: 'text',
            hints: '新しいパスワード',
            param: '',
            keyName: 'password_new1',
            option: {formType: 'password'},
            col: { title: 4, content: 6},
            md: { title: 3, content: 4},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {
                ope: 'ge',
                count: 8
              }
            },
          },
          password_new2: {
            base: 'text',
            hints: 'パスワード再入力',
            param: '',
            keyName: 'password_new2',
            option: {formType: 'password'},
            col: { title: 4, content: 6},
            md: { title: 3, content: 4},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {
                ope: 'ge',
                count: 8
              }
            },
          },
        }
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
      ...mapGetters('auth', ['getAuthList']),
      ...mapGetters('common', ['getComList']),
    },
    mounted() {
    },
    methods: {
      ...mapActions('user', [
        'setUserEditParam', 'setUserData'
      ]),
      ...mapActions('auth', [
        'updatePass', 'setChangePassParam', 'setErrMsg', 'setSelectMenu'
      ]),
      onPassEdit :async function () {
        let changePassParam = this.getAuthList('changePassParam');
        let errMsg= this.checkValidation(this.options, changePassParam);
        console.log(errMsg);
        if (Object.keys(errMsg).length === 0) {
          await this.updatePass();
          let authResult = this.getComList('commonMsg');
          if (authResult.result_cd === '001') {
              this.setSelectMenu({
                  path: this.$route.path,
                  main: 'user',
                  sub: null
              });
          }
        } else {
          this.setErrMsg("入力値に不備があります");
        }
      },
      changeForm : function(data) {
        this.setChangePassParam(data);
      },
    },
    created() {

    }
  }
</script>

<style lang="scss" scoped>
.change-page {
  .change-card {
    background-color: rgb(245, 245, 245);
    margin-top: 10vh;
    .change-row {
      margin: auto;
      height: 50px;
      margin-bottom: 0px;
      .error-message {
        color: red;
        margin: auto;
        text-align: center;
        font-size: 14px;
      }

    }
    .-logo {
      border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
      margin: auto;
      background-position: left top;  /* 横長画像の左上を基準に表示 */
      display: inline-block;
    }
  }

}

</style>
