<template>
  <v-container fluid
               :class=" checkTerminal ? 'team-edit' : 'team-edit-mobile' ">
    <v-row
      align="center"
      class="team-edit-row"
    >
      <v-col class="team-edit-col">
        <v-card class="team-edit-card-body">
          <v-container fluid>
            <v-row>
              <v-col class="team-title-area" cols="12" style="padding-bottom: 0; padding-top: 0;">
                <v-card-title class="team-title"> {{ showTitle }} </v-card-title>
              </v-col>
            </v-row>
            <v-divider />
            <v-row>
              <v-col>
                <horizontal-form
                  :formData="options"
                  :errMsg="teamEditErrMsg"
                  @changeForm="changeForm"
                >
                  <template slot="button-area">
                    <v-col :cols="12" align-self="center" class="text-center">
                      <template v-for="item in pageData.param.btn">
                        <v-btn rounded color="primary" dark
                               @click="onTeamEdit(item)"
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
  import rivalHeader from '../common/Header.vue';
  import formatMixin from "../common/formatMixin";
  import ActionMixin from "../common/ActionMixin";
  import HorizontalForm from "../form/HorizontalForm";
  import ConfirmationDialog from "../form/ConfirmationDialog";
  export default {
    name: 'team',
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
      pageType: {
        type: String,
        default: function () {
          return 'addTeam'
        }
      },
      targetData: {
        type: Object,
        default: function () {
          return {}
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
      ...mapState('auth',['authFlg', 'joinTeamList']),
      ...mapState('area', [
        'prefecture', 'city', 'station'
      ]),
      ...mapState('common', [
        'purpose', 'checkWeek'
      ]),
      ...mapState('constant', [
        'pageOption', 'dialogContent'
      ]),
      ...mapState('team', [
         'teamAddApiParam', 'teamEditErrMsg'
      ]),
      ...mapState('auth', [
        'userList'
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
      ...mapActions('team', [
        'setTeamAddApiParam', 'addTeam', 'setTeamEditErrMsg', 'editTeam'
      ]),
      ...mapActions('auth', ['getUser', 'setSelectMenu']),
      checkPage: function () {
        let key = '';
        switch (this.pageType) {
          case 'editTeam':
            key = 'edit';
            break;
          case 'addTeam':
            key = 'add';
            break;
        }
        const page = this.getPageContent({page: 'teamEdit', part: key});
        this.$set(this.pageData.param, 'title', page.title);
        this.$set(this.pageData.param, 'btn', page.btn);
        this.$set(this, 'options', page.options);
      },
      setSelectOption: async function () {
        if (this.joinTeamList.team.length > 0) {
          let team = this.joinTeamList.team[Number(this.targetData.idx)];
          await this.sendCreatApi(team);
          await this.makeOptionData('options', null, team);
        } else {
          await this.sendCreatApi();
          this.makeOptionData('options');
        }
      },
      sendCreatApi: async function (team=null) {
        await this.getPrefecture();
        if (team) {
          let team_prefecture_key = {key: team.prefecture.val, val: team.prefecture.key };
          await this.setAriaApiParam(team_prefecture_key);
          await this.getCity();
          let team_city_key = {key: 'city', param: { label: team.city.val } };
          await this.setAriaApiParam(team_city_key);
          await this.getStation();
        }
      },
      onTeamEdit: async function (key) {
        let res = await this.makeApiData(this.options);
        res['user_id'] = { key: 'user_id', val: this.userList.user_id};

        this.setTeamAddApiParam(res);
        let errMsg = this.checkValidation(this.options, this.teamAddApiParam);
        await this.setTeamEditErrMsg(errMsg);
        switch (key) {
          case 'addTeam':
            if (Object.keys(this.teamEditErrMsg).length === 0) {
              await this.setConfirmationDialogOption('add');
              this.$set(this.confirmationDialogOption, 'flg', true);
            }
            break;
          case 'editTeam':
            if (Object.keys(this.teamEditErrMsg).length === 0) {
              await this.setConfirmationDialogOption('edit');
              this.$set(this.confirmationDialogOption, 'flg', true);
            }
            break;
          case 'cancel':
            const res = {
              path: this.$route.path,
              main: 'team',
              sub: this.targetData
            };
            await this.setSelectMenu(res);
            break;
        }
      },
      onConfirmationBtn: async function (param) {
        this.$set(this.confirmationDialogOption, 'flg', false);
        let key = param.btn;
        switch (param.dialog) {
          case 'add':
            if (key === 'confirm'){
              await this.addTeam();
              if (Object.keys(this.teamEditErrMsg).length === 0) {
                await this.getUser();
                const res = {
                  path: '/my_page',
                  main: 'user',
                  sub: null
                };
                await this.setSelectMenu(res);
              }
            }
            break;
          case 'edit':
            if (key === 'confirm'){
              await this.editTeam();
              if (Object.keys(this.teamEditErrMsg).length === 0) {
                await this.getUser();
                const res = {
                  path: this.$route.path,
                  main: 'team',
                  sub: this.targetData
                };
                await this.setSelectMenu(res);
              }
            }
            break;
        }
      }
    },
    created : async function () {
      await this.checkPage();
      this.setSelectOption();
    }
  }
</script>

<style lang="scss" scoped>
  .team-edit {
    .team-edit-row {
      .team-edit-col {
        .team-edit-card-body {
          background-color: rgb(245, 245, 245);
          .team-title-area {
            padding-top: 0;
            padding-bottom: 0;
            .team-title {
              padding-left: 15px;
            }
          }
          .team-edit-error-msg {
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
    }
  }
  .team-edit-mobile {
    min-height: 80vh;
    max-height: 100vh;

    .team-edit-row {
      .team-edit-col {
        .team-edit-card-body {
          max-height: 90vh;
          overflow: auto;
          background-color: rgb(245, 245, 245);
          .team-title {
            padding-left: 15px;
          }
          .team-edit-error-msg {
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
    }
  }
</style>
