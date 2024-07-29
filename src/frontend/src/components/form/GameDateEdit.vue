<template>
  <v-container fluid
               :style=" checkTerminal ? 'width: 70vw' : 'width: 90vw'"
  >
    <v-row
        align="center"
        style="padding: 0;"
        class="game-date-edit"
    >
      <v-col cols="12" md="12" align-self="center">
        <v-card class="card-body">
          <v-container fluid>
            <v-row>
              <v-col cols="12" style="padding-bottom: 0; padding-top: 0;">
                <v-card-title> {{ pageOption.title.gameDateEdit }}</v-card-title>
              </v-col>
            </v-row>
            <v-divider/>
            <v-row class="game-date-edit-form-row">
              <v-col cols="11">
                <v-row style="padding: 0">
                  <v-col style="padding: 0; margin-left: 2vw;">
                    <p>試合日程</p>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <template v-if="checkTerminal">
              <v-row>
                <v-col cols="4">
                  日付
                </v-col>
                <v-col cols="2">
                  開始
                </v-col>
                <v-col cols="2">
                  終了
                </v-col>
                <v-col cols="4">
                  場所
                </v-col>
              </v-row>
              <v-row v-for="(detail ,index) in gameDateEditApiParam">
                <v-col cols="4">
                  <base-date
                      :hints="form.game_date.hints"
                      :keyName="form.game_date.keyName  + '-' + index "
                      :param="detail.game_date"
                      :option="form.game_date.option"
                      @changeForm="changeForm"
                  >
                  </base-date>
                </v-col>
                <v-col cols="2">
                  <base-input-text
                      :hints="form.game_time_start.hints"
                      :keyName="form.game_time_start.keyName  + '-' + index "
                      :param="detail.game_time_start"
                      :formType="form.game_time_start.formType"
                      :option="form.game_time_start.option"
                      @changeForm="changeForm"
                  >
                  </base-input-text>
                </v-col>
                <v-col cols="2">
                  <base-input-text
                      :hints="form.game_time_end.hints"
                      :keyName="form.game_time_end.keyName + '-' + index "
                      :param="detail.game_time_end"
                      :formType="form.game_time_end.formType"
                      :option="form.game_time_end.option"
                      @changeForm="changeForm"
                  >
                  </base-input-text>
                </v-col>
                <v-col cols="3">
                  <base-input-text
                      :hints="form.comment.hints"
                      :keyName="form.comment.keyName + '-' + index "
                      :param="detail.comment"
                      :option="form.comment.option"
                      @changeForm="changeForm"
                  >
                  </base-input-text>
                </v-col>
                <div cols="1">
                  <v-btn small icon color="gray" style="margin-top: 17px; margin-left: 5px"
                         @click="deleteGameDate(index)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </div>
              </v-row>
            </template>
            <template v-else>
              <template v-for="(detail,index) in gameDateEditApiParam">
                <v-row>
                  <v-col cols="3">
                    {{ '日程' + (index +1) }}
                  </v-col>
                  <div cols="1">
                    <v-btn small icon color="gray" style="margin-top: 10px;"
                           @click="deleteGameDate(index)">
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </div>
                </v-row>
                <v-row>
                  <v-col cols="2">
                    日付
                  </v-col>
                  <v-col cols="10">
                    <base-date
                        :hints="form.game_date.hints"
                        :keyName="form.game_date.keyName + '-' + index "
                        :param="detail.game_date"
                        :option="form.game_date.option"
                        @changeForm="changeForm"
                    >
                    </base-date>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="2">
                    開始
                  </v-col>
                  <v-col cols="4">
                    <base-input-text
                        :hints="form.game_time_start.hints"
                        :keyName="form.game_time_start.keyName + '-' + index"
                        :param="detail.game_time_start"
                        :formType="form.game_time_start.formType"
                        :option="form.game_time_start.option"
                        @changeForm="changeForm"
                    >
                    </base-input-text>
                  </v-col>
                  <v-col cols="2">
                    終了
                  </v-col>
                  <v-col cols="4">
                    <base-input-text
                        :hints="form.game_time_end.hints"
                        :keyName="form.game_time_end.keyName + '-' + index"
                        :param="detail.game_time_end"
                        :formType="form.game_time_end.formType"
                        :option="form.game_time_end.option"
                        @changeForm="changeForm"
                    >
                    </base-input-text>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="2">
                    場所
                  </v-col>
                  <v-col cols="10">
                    <base-input-text
                        :hints="form.comment.hints"
                        :keyName="form.comment.keyName + '-' + index "
                        :param="detail.comment"
                        :option="form.comment.option"
                        @changeForm="changeForm"
                    >
                    </base-input-text>
                  </v-col>
                </v-row>
              </template>
            </template>
            <v-row>
              <v-col cols="4" v-if="this.gameDateEditApiParam.length < 3">
                <v-btn outlined small fab color="indigo"
                       @click="addGameDate">
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn rounded color="primary" dark
                       @click="onGameDateEdit"
                >日程更新
                </v-btn>
              </v-col>
            </v-row>
            <v-row v-if="teamEditErrMsg">
              <v-col>
                {{ teamEditErrMsg.message }}
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
  import {mapActions, mapGetters, mapState} from 'vuex';
  import ConfirmationDialog from "@/components/form/ConfirmationDialog";
  import BaseDate from "@/components/part/BaseDate";
  import BaseInputText from "@/components/part/BaseInputText";
  import ActionMixin from "@/components/common/ActionMixin";

  export default {
    name: "GameDateEdit",
    mixins: [ActionMixin],
    components: {BaseInputText, BaseDate, ConfirmationDialog},
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
        confirmationDialogOption: {
          param: {
            flg: false,
            dialogKey: '',
            btnKeyList: [],
          },
          edit: {
            dialogKey: 'edit',
            btnKeyList: ['confirm', 'cancel']
          }
        },
        form: {
          game_date: {
            base: 'text',
            hints: '',
            param: '',
            keyName: 'game_date',
            option: {},
            col: {title: 4, content: 6},
            md: {title: 3, content: 4},
            primary: true,
          },
          game_time_start: {
            base: 'text',
            hints: '',
            param: '',
            keyName: 'game_time_start',
            option: {
              formType: 'time',
            },
            col: {title: 4, content: 6},
            md: {title: 3, content: 4},
            primary: true,
          },
          game_time_end: {
            base: 'text',
            hints: '',
            param: '',
            keyName: 'game_time_end',
            option: {
              formType: 'time',
            },
            col: {title: 4, content: 6},
            md: {title: 3, content: 4},
            primary: true,
          },
          comment: {
            base: 'text',
            hints: '',
            param: '',
            keyName: 'comment',
            option: {},
            col: {title: 4, content: 6},
            md: {title: 3, content: 4},
            primary: true,
          }
        }
      }
    },
    computed: {
      ...mapState('auth', ['authFlg', 'userList', 'joinTeamList']),
      ...mapState('constant', [
        'pageOption', 'dialogContent'
      ]),
      ...mapState('user', [
        'errUserEditMsg', 'userEditParam'
      ]),
      ...mapState('team', ['teamList', 'gameDateEditApiParam', 'teamEditErrMsg'])
    },
    watch: {
      teamEditErrMsg: {
        handler: function (to, from ) {
          if (Object.keys(to).includes('message')) {
            let team = this.joinTeamList.team[Number(this.targetData.idx)];
            this.setGameDateApiParam();
            this.setGameDateApiParam(team.game_date);
          }
        },
        deep: true
      }
    },
    mounted() {
      this.getTeamDate();
    },
    methods: {
      ...mapActions('team', ['getDetailTeamList', 'getDateTeamList',
        'setSearchDetailParam', 'setGameDateApiParam', 'setGameDateApiParam',
        'rowDeleteGameDate', 'setGameDateApiRowParam', 'editGameDate']),
      getTeamDate: async function () {
        let team = this.joinTeamList.team[Number(this.targetData.idx)];
        await this.setGameDateApiParam(team.game_date);
        if (this.gameDateEditApiParam.length === 0) {
          await this.setGameDateApiParam([{
            "game_date": '',
            "game_time_start": '',
            "game_time_end": '',
            "comment": '',
          }]);
        }
      },
      onGameDateEdit: async function () {
        await this.setConfirmationDialogOption('edit');
        this.$set(this.confirmationDialogOption, 'flg', true);
      },
      changeForm(data) {
        let keys = data.key.split('-');
        this.setGameDateApiRowParam({fieldName: keys[0], index: keys[1], val: data.val})
      },
      addGameDate() {
        console.log("addGameDate");
        if (this.gameDateEditApiParam.length < 3) {
          this.setGameDateApiParam([{
            "game_date": '',
            "game_time_start": '',
            "game_time_end": '',
            "comment": '',
          }]);
        }
      },
      deleteGameDate(index) {
        this.rowDeleteGameDate(index);
      },
      onConfirmationBtn: async function (param) {
        this.$set(this.confirmationDialogOption, 'flg', false);
        let key = param.btn;
        let team = this.joinTeamList.team[Number(this.targetData.idx)];
        switch (param.dialog) {
          case 'edit':
            if (key === 'confirm') {
              await this.editGameDate(team);
              if (Object.keys(this.teamEditErrMsg).length === 0) {
                this.movePage(
                  '/my_page',
                  'team', this.targetData
                );
              }
            }
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .game-date-edit {
    padding: 0;

    .game-date-edit-form-row {
      min-height: 8vh;
      height: auto;
      margin-bottom: 0px;

      p {
        font-size: 20px;
        margin-top: 5px;
        margin-left: 10px;
        padding-left: 10px;
        padding-top: 5px;
        border-left: 6px solid #ffaa1a;
        white-space: pre-line;
      }

      .horizontal-require {
        font-size: 13px;
        border: none;
        color: #686c6d;
      }
    }

    .card-body {
      background-color: rgb(245, 245, 245);
    }

  }
</style>