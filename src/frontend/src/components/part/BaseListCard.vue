<template>
  <v-card class="base-card mx-auto">
    <v-container>
      <v-row>
        <v-col cols="12" v-for="(item, key) in formatData.title">
          <p class="base-card-title"> {{ rowData[key] }} </p>
          <v-divider />
        </v-col>
      </v-row>
      <v-row
        @click="onDetail"
      >
        <v-col cols="12" md="3">
          <template v-for="(item, key) in formatData.image">
            <v-img
              height="200"
              width="200"
              :src="rowData[key]"
              style="margin: auto; border: solid 1px #a8b7c5;"
            />
          </template>
        </v-col>
        <v-col cols="12" md="9">
          <v-row>
            <v-col class="base-card-col">
              <p>{{ viewArea }}</p>
              <v-divider />
            </v-col>
          </v-row>
          <template v-for="(item, key) in formatData.data">
            <v-row>
              <v-col v-if=" key === 'line' " class="base-card-col">
                <p>{{ rowData.line.val }} {{ rowData.station.val }}</p>
                <v-divider />
              </v-col>
              <v-col v-else-if="key === 'game_date' && !authFlg " class="base-card-col ">
                <p style="white-space: pre-line;" >{{ viewContent(key, rowData[key]) }}</p>
                <v-divider />
              </v-col>
              <v-col v-else-if="key !== 'game_date'" class="base-card-col ">
                <p style="white-space: pre-line;" >{{ viewContent(key, rowData[key]) }}</p>
                <v-divider />
              </v-col>
            </v-row>
          </template>
        </v-col>
        <v-col cols="12" md="12" class="base-card-col">
          <v-divider />
        </v-col>
      </v-row>
      <v-row v-if="authFlg">
        <template v-for="(item, idx) in rowData.game_date">
          <v-col>
            <v-btn block tile color="indigo" dark
                   style="position: relative; z-index: 1;"
                   @click="onCardBtn(idx, item)"
            >{{ checkViewBtn(item) }}</v-btn>
          </v-col>
        </template>
      </v-row>
    </v-container>
    <select-dialog
      :dialog-flg="dialog.flg"
      :btn-key-list="dialog.btnKeyList"
      :title="dialog.title"
      :row-data="dialog.rowData"
      @onSubmit="onDialogBtn"
    />
  </v-card>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'
import ActionMixin from "@/components/common/ActionMixin";
import SelectDialog from "@/components/form/SelectDialog";

export default {
  name: 'BaseListCard',
  mixins: [ActionMixin],
  components: {
    SelectDialog
  },
  props: {
    formatData: {
      type: Object,
      default: function () {
        return {
          title: {},
          image: {},
          data: {},
          area: {},
          button: {}
        }
      }
    },
    rowData: {
      type: Object,
      default: function () {
        return {}
      }
    },

  },
  data: function() {
    return {
      dialog: {
        flg: false,
        keyList: {},
        title: '',
        rowData: null
      }
    }
  },
  computed: {
    ...mapGetters('common', ['getComList']),
    ...mapState('auth', ['authFlg', 'joinTeamList']),
    viewArea: function () {
      let res = '';
      for (let key in this.formatData.area) {
        res += this.rowData[key][this.formatData.area[key]];
      }
      return res
    }
  },
  watch: {

  },
  methods: {
    viewContent: function (key, data) {
      if (data) {
        let res;
        switch (key) {
          case 'purpose':
            let t = [];
            const p = this.getComList(key);
            for ( let idx in p) {
              if ( data.includes(p[idx].val) ) {
                t.push(p[idx].label);
              }
            }
            res = t.join(' / ');
            break;
          case 'game_date':
            res = "";
            for (let idx in data) {
              let game_date = data[idx]['game_date'];
              let start = data[idx]['game_time_start'] ? data[idx]['game_time_start'] : '';
              let end = data[idx]['game_time_end'] ? data[idx]['game_time_end'] : ' - ';
              let comment = data[idx]['comment'] ? data[idx]['comment'] : ' - ';
              if (Number(idx) !== 0) {
                res += '\n' + game_date + ' ' + start + ' ~ ' + end + ' : ' + comment;
              } else {
                res += game_date + ' ' + start + ' ~ ' + end + ' : ' + comment;
              }
            }
            break;
        }
        return res
      } else {
        return data
      }
    },
    checkViewBtn: function (item) {
      let flg = false;
      console.log(item);
      if (item) {
        switch (item.exec_type) {
          case 'SEND':
            return item.game_date + ' ' + item.game_time_start + '送信済'
            break;
          case 'MATCH':
            return '成立！'
            break;
          case 'RES':
            return item.game_date + ' ' + item.game_time_start
            break;
          case 'NONE':
          default:
            return item.game_date + ' ' + item.game_time_start
        }
      } else {

      }
    },
    onCardBtn: function (idx) {
      let game_date = this.rowData.game_date[idx];
      game_date['team_id'] = this.rowData.team_id;
      this.$set(this.dialog, 'title', game_date['game_date']);
      this.$set(this.dialog, 'btnKeyList', this.checkStatus(game_date));
      const data = {data: this.rowData, content: this.makeDialogBody(game_date), target: game_date};
      this.$set(this.dialog, 'rowData', data);
      this.$set(this.dialog, 'flg', true );
    },
    makeDialogBody: function (game) {
      let result = [{},{},{}];
      console.log(game);
      for (let key in game) {
        switch (key) {
          case 'game_time_start':
            result[0] = {title: '開始', content: game[key]};
            break;
          case 'game_time_end':
            result[1] = {title: '終了', content: game[key]};
            break;
          case 'comment':
            result[2] = {title: '場所', content: game[key]};
            break;
        }
      }

      console.log(result);
      return　result
    },
    onDialogBtn: function (data) {
      this.$set(this.dialog, 'flg', false );
      this.$emit('onCardBtn', data);
    },
    checkStatus: function (data) {
      let result = {};
      let flg = false;
      console.log(data);
      if (data) {
        switch (data.exec_type) {
          case 'SEND':
            result = {cancel: '挑戦状を取り下げる'};
            break;
          case 'RES':
            result = {
              response: '挑戦を受ける',
              reject: '挑戦を断る'
            };

            break;
          case 'MATCH':
            result = {
              chat: 'チャットへ'
            };
            break;
          case 'NONE':
            result = {request: '挑戦状を送る'};
            break;
        }
      } else {

      }
      result['close'] = '閉じる';
      return result
    },
    onDetail: function () {
      const data = {key: 'detail', data: this.rowData};
      this.$emit('onCardDetail', data);
    }
  },
  created () {


  }
}
</script>

<style  lang="scss" scoped>
  .base-card {
    .base-card-title {
        font-size: 20px;
        margin-top: 5px;
        margin-left: 10px;
        padding-left: 10px;
        padding-top: 5px;
        border-left: 6px solid #ffaa1a;
    }
    .base-card-col {
      padding-bottom: 0;
    }
  }

</style>
