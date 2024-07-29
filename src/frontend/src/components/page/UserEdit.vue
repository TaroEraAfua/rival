<template>
  <v-container fluid
    :class=" checkTerminal ? 'user-edit' : 'user-edit-mobile' "
    :style=" checkTerminal ? rootPage !== '/my_page' ? 'width: 70vw' : '' : rootPage !== '/my_page' ? 'width: 90vw' : '' "
  >
    <v-row
      align="center"
      style="padding: 0;"
    >
      <v-col cols="12" md="12" align-self="center">
        <v-card class="card-body">
          <v-container fluid>
            <v-row >
              <v-col cols="12" style="padding-bottom: 0; padding-top: 0;">
                <v-card-title class="user-title"> {{ showTitle }} </v-card-title>
              </v-col>
            </v-row>
            <v-divider />
            <v-row>
              <v-col>
                <horizontal-form
                  :formData="options"
                  :errMsg="errUserEditMsg"
                  @changeForm="changeForm"
                >
                  <template slot="button-area">
                    <v-col :cols="12" align-self="center" class="text-center">
                      <template v-for="item in pageData.param.btn">
                        <v-btn rounded color="primary" dark class="ma-2"
                               @click="onUserEdit(item)"
                        >{{ pageOption.btn[item] }}</v-btn>
                      </template>

                    </v-col>
                  </template>
                </horizontal-form>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
    <confirmation-dialog
      :dialogFlg="confirmationDialogOption.flg"
      :dialogKey="confirmationDialogOption.param.dialogKey"
      :btnKeyList="confirmationDialogOption.param.btnKeyList"
      @onBtn="onConfirmationBtn"
    />
  </v-container>
</template>

<script>
  import { mapActions, mapGetters, mapState } from 'vuex';
  import formatMixin from "@/components/common/formatMixin";
  import ActionMixin from "@/components/common/ActionMixin";
  import HorizontalForm from "@/components/form/HorizontalForm";
  import ConfirmationDialog from "@/components/form/ConfirmationDialog";
  export default {
    name: 'UserEdit',
    mixins: [formatMixin, ActionMixin],
    components: {
      HorizontalForm, ConfirmationDialog
    },
    props: {
      checkTerminal: {
        type: Boolean,
        default: function () {
          return true
        }
      },
      rootPage: {
        type: String,
        default: function () {
          return '/'
        }
      }
    },
    data() {
      return {
        options: {},
        pageData: {
          param: {
            title: '',
            btn: [],
          },
        },
        confirmationDialogOption: {
          param: {
            flg: false,
            dialogKey: '',
            btnKeyList: [],
          },
          add: {
            dialogKey: 'add',
            btnKeyList: ['confirm', 'cancel']
          },
          edit: {
            dialogKey: 'edit',
            btnKeyList: ['confirm', 'cancel']
          }
        },
      }
    },
    watch: {
      authFlg: {
        handler: function (to, from) {
          this.setSelectOption();
          this.checkPage();
        },
        deep: true
      },
    },
    computed:{
      ...mapState('auth',['authFlg', 'userList']),
      ...mapState('area', [
        'prefecture', 'city', 'station'
      ]),
      ...mapState('common', [
        'purpose', 'checkWeek'
      ]),
      ...mapState('constant', [
        'pageOption', 'dialogContent'
      ]),
      ...mapState('user', [
        'errUserEditMsg', 'userEditParam'
      ]),
      showTitle: function () {
        return this.pageOption.title[this.pageData.param.title]
      },
    },
    methods: {
      ...mapActions('area', [
        'getPrefecture', 'setAriaApiParam',
        'getCity', 'getStation'
      ]),
      ...mapActions('common', [
        'getConData'
      ]),
      ...mapActions('user', [
        'setUserEditParam', 'setUserData', 'setUserEditErrMsg', 'updateUserData'
      ]),
      ...mapActions('auth', [
        'logIn', 'setLoginParam', 'getUser'
      ]),
      checkPage: function () {
        let key = '';
        switch (this.rootPage) {
          case '/my_page':
            key = 'edit';
            break;
          case '/user_add':
            key = 'add';
            break;
        }
        const page = this.getPageContent({page: 'userEdit', part: key});
        this.$set(this.pageData.param, 'title', page.title);
        this.$set(this.pageData.param, 'btn', page.btn);
        this.$set(this, 'options', page.options);
        this.setConfirmationDialogOption(key);
      },
      setSelectOption: async function () {
        await this.sendCreatApi();
        switch (this.rootPage) {
          case '/my_page':
            await this.makeOptionData('options', null, this.userList);
            break;
          case '/user_add':
            this.makeOptionData('options');
            break;
        }
        await this.delGender();
      },
      sendCreatApi: async function () {
        await this.getPrefecture();
        if (Object.keys(this.userList).length > 0) {
          let prefecture_key = {key: this.userList.prefecture.val, val: this.userList.prefecture.key };
          await this.setAriaApiParam(prefecture_key);
          await this.getCity();
        }
      },
      onUserEdit: async function (key) {
        let res = await this.makeApiData(this.options);
        this.setUserEditParam(res);
        let errMsg = this.checkValidation(this.options, this.userEditParam);
        await this.setUserEditErrMsg(errMsg);
        switch (key) {
          case 'addUser':
            if (Object.keys(this.errUserEditMsg).length === 0) {
              this.$set(this.confirmationDialogOption, 'flg', true);
            }
            break;
          case 'editUser':
            if (Object.keys(this.errUserEditMsg).length === 0) {
              this.$set(this.confirmationDialogOption, 'flg', true);
            }
            break;
        }
      },
      onConfirmationBtn: async function (param) {
        let key = param.btn;
        this.$set(this.confirmationDialogOption, 'flg', false);
        switch (param.dialog) {
          case 'edit':
            if (key === 'confirm') {
              await this.updateUserData();
              if (Object.keys(this.errUserEditMsg).length === 0) {
                this.movePage(this.$route.path,'user');
              }
            }
            break;
          case 'add':
            if (key === 'confirm') {
              await this.setUserData();
              if (Object.keys(this.errUserEditMsg).length === 0) {
                await this.movePage("/login");
              }
            }
            break;
        }
      }
    },
    created : async function () {
      // エラーメッセージ初期化
      let errMsg = {};
      await this.setUserEditErrMsg(errMsg);
      await this.checkPage();
      this.setSelectOption();
    }
  }
</script>

<style lang="scss" scoped>
.user-edit {
  padding: 0;
  .card-body {
    background-color: rgb(245, 245, 245);
    .user-title {
      padding-left: 15px;
    }
    .user-edit-error-msg {
      ul {
        list-style: none;
      }
      li {
        padding-left: 20px;
        padding-bottom: 5px;
        color: red;
        font-size: 15px;
      }
    }
  }
}
.user-edit-mobile {
  width: 100vw;
  padding: 0;
  .card-body {
    background-color: rgb(245, 245, 245);
    .user-edit-button {
      padding: 2.5px 5px 2.5px 5px;
      border-radius: 30px;
    }
    .user-edit-error-msg {
      ul {
        list-style: none;
      }
      li {
        color: red;
        font-size: 10px;
      }
    }
  }

}
</style>
