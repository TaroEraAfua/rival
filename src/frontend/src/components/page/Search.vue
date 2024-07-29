<template>
 <v-container fluid
              :class=" checkTerminal ? 'page-home' : 'page-home-mobile' "
              :style="{ 'background-image': 'url(' + backImage + ')' }"
 >

   <v-row style="margin: 0">
     <vertical-form
       :form-type="formType"
       :form-data="options"
       @changeForm="changeForm"
     >
       <template slot="bottun-area">
         <v-col class="col-span" cols="12" md="12">
           <v-btn block tile color="indigo" dark
                  style="position: relative; z-index: 1; height: 39px"
                  @click="preSearch()"
           >チームを探す</v-btn>
         </v-col>

       </template>
     </vertical-form>
   </v-row>
   <v-row style="margin: 0">
    <search-list
      :data-list="teamList"
      :formatData="searchTeamFormat"
      @changePage="preSearch"
      @onCardBtn="onCardBtn"
    />
   </v-row>
   <view-dialog
    :dialog-flg="viewDialogOption.flg"
    :dialog-key="viewDialogOption.key"
    :info-data="viewDialogOption.infoData"
    :options="viewDialogOption.option"
    :btn-key-list="viewDialogOption.btnKeyList"
    @onSubmit="onSubmitViewDialog"
   />
 </v-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import rivalHeader from '../common/Header.vue'
import formatMixin from "../common/formatMixin";
import ActionMixin from "../common/ActionMixin";
import VerticalForm from "../form/VerticalForm";
import BaseSelect from "../part/BaseSelect";
import SearchList from "../form/SearchList";
import ViewDialog from "../form/ViewDialog";
export default {
  name: 'top',
  mixins: [formatMixin, ActionMixin],
  props: {
    checkTerminal: {
      type: Boolean,
      default: function () {
        return true
      }
    }
  },
  components: {
    VerticalForm, rivalHeader,BaseSelect, SearchList, ViewDialog
  },
  data() {
    return {
      backImage: require('../common/images/back.jpg'),
      leftImage: require('../common/images/our_image_jpeg.jpg'),
      formType: {line: 'ver', xs: 6, md: 3 },
      dataList: {
        prof: [],
        count: 1
      },
      formOption: {
        keyName: 'form',
        hints: '検索タイプ',
        param: {val: 1, label: '詳細'},
        option: {
          item: [{val: 1, label: '詳細'}, {val: 2, label: '日付'}],
          label: 'label'
        },
      },
      options: {},
      infoData: {
        title: '',
        list: {},
        format: {},
        btn: {},
        type: ''
      },
      infoItem: {
        team: {
          title: '',
          list: {},
          format: {},
        },
      },
      viewDialogOption: {
        key: 'detailTeam',
        flg: false,
        infoData: {},
        option: {
          width: 60,
          height: 70
        },
        btnKeyList: ['cancel']
      }
    }
  },
  watch: {
    authFlg: {
      handler: function (to, from) {
        this.checkPage();
      },
      deep: true
    },
  },
  computed:{
    ...mapState('area', [
      'prefecture', 'city', 'station'
    ]),
    ...mapState('constant', [
        'userInfo', 'teamInfo', 'challengeInfo', 'searchTeamFormat'
      ]
    ),
    ...mapState('auth',['authFlg', 'userList', 'joinTeamList']),
    ...mapState('team',['teamList']),
    ...mapState('common', [
      'purpose','gender'
    ]),
  },
  methods: {
    ...mapActions('area', [
      'getPrefecture', 'setAriaApiParam',
      'getCity', 'getStation'
    ]),
    ...mapActions('common', [
      'getConData'
    ]),
    ...mapActions('auth', [
      'setSelectMenu'
    ]),
    ...mapActions('team', [
      'getDetailTeamList', 'getDateTeamList',
      'setSearchDetailParam', 'setSearchDateParam',
      'initSearchDetailParam', 'initSearchDateParam',
      ],
    ),
    ...mapActions('challenge', ['sendChallenge', 'matchChallenge', 'deleteChallenge']),

    /**
     * 表示リストの設定
     * @returns {Promise<void>}
     */
    setSelectOption: async function () {
      await this.sendCreatApi();
      this.makeOptionData('options');
    },
    /**
     * 検索項目取得
     * @returns {Promise<void>}
     */
    sendCreatApi: async function () {
      await this.getPrefecture();
    },
    /**
     * チーム検索
     * @returns {Promise<void>}
     */
    onSearch: async function () {
      let res = await this.makeApiData(this.options);
      console.log(this.userList);
      if (Object.keys(this.userList).length > 0) {
        await this.setSearchApiParam(
          {
            user: {
              key: 'user',
              val: this.userList.user_id
            },
            team: {
              key: 'team',
              val: this.joinTeamList.select
            }
          }
        );
      }

      await this.setSearchDateParam(res);
      await this.getDateTeamList();

    },
    setSearchApiParam: function (data) {
      this.setSearchDateParam(data);
    },
    /**
     * 検索前処理
     */
    preSearch: async function (data=null) {
      if (data) {
        await this.setSearchApiParam(data);
      }
      this.onSearch();
    },
    /**
     * 検索条件変更
     * @param data
     */
    changeType: function (data) {
      this.$set(this.formOption, 'param', data.param);

      let key = 'date';
      this.initSearchDateParam();
      this.$set(this, 'options', this.getPageContent({page: 'search', part: key}));
      this.makeOptionData('options');
    },
    checkPage: function () {
      this.changeType({param: {val: 1} } );
    },
    onCardDetail: async function ({key, data}) {
      this.$set(this.infoItem.team, 'list', data);
      this.$set(this.infoItem.team, 'format', this.teamInfo);
      await this.makeInfoParam('team');
      this.$set(this.viewDialogOption, 'infoData', this.infoData);
      this.$set(this.viewDialogOption, 'flg', true);
    },
    onSubmitViewDialog: function (key) {
      this.$set(this.viewDialogOption, 'flg', false);
    },
    onCardBtn: async function ({key, data}) {
      console.log('onCardBtn');
      console.log(data);
      switch (key) {
        case 'request':
          await this.sendChallenge(
            {
              target_id: data.team_id,
              team_id: this.joinTeamList.select,
              game_date: data.game_date,
              game_time_start: data.game_time_start
            }
          );
          break;
        case 'reject':
          await this.deleteChallenge({
            challenge_id: data.challenge_id,
            }
          );
          break;
        case 'response':
          await this.matchChallenge({
              challenge_id: data.challenge_id,
            }
          );
          break;
        case 'cancel':
          await this.deleteChallenge({
              challenge_id: data.challenge_id,
            }
          );
          break;
        case 'chat':
          await this.movePage('/my_page', 'chat',{
              title: data.team_name,
              icon: '',
              chat_id:  data.challenge_id
            });
          break;
      }
      this.preSearch();
    }
  },
  created: function () {
    this.checkPage();
    this.setSelectOption();
    if (!this.teamList) {
      this.preSearch();
    } else if (this.teamList.prof.length === 0) {
      this.preSearch();
    }
  }
}
</script>

<style lang="scss" scoped>
.page-home {
  min-height: 80vh;
  height: auto;
  padding: 0;
  margin: 0;
  background-attachment: fixed;
  .main-row {
    background: no-repeat center;
    height: 80vh;
    margin: 0;
  }
  .right-form {
    .right-form-image {
      border-radius: 320px / 200px;
      border: 2px solid #1892f6;
    }

  }
  .left-form {

  }
}
.page-home-mobile {
  min-height: 150vh;
  height: auto;
  width: 100vw;
  padding: 0;
  margin: 0;
  background-attachment: fixed;
  .main-row {
    background: no-repeat center;
    height: 80vh;
    width: 100vw;
    margin: 0;
  }
  .right-form {
    .right-form-image {
      border-radius: 320px / 200px;
      border: 2px solid #1892f6;
    }

  }
  .left-form {

  }
}
</style>
