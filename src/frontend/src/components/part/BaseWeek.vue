<template>
  <div justify="center" class="base-week">
    <template v-if="option.formType === 'input' ">
      <v-text-field
        background-color="white"
        :label="hints"
        v-model="label"
        outlined
        readonly
        @click="onForm"
      />
    </template>
    <template v-else-if="option.formType === 'button' ">
      <v-btn
        block
        tile
        color="indigo"
        dark
        style="position: relative; z-index: 1;"
        @click="onForm"
      > 詳細表示
      </v-btn>
    </template>
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">

      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>曜日時間選択</v-toolbar-title>
          <v-spacer />
          <v-toolbar-items v-if="!option.isDisable">
            <v-btn dark text @click="onSubmit">登録</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <template>
          <v-row>
            <v-col>
              <v-sheet>
                <div class="week-calender">
                  <div class="week-header" >
                    <div class="week-header-empty-col" style="width: 45px">
                    </div>
                    <div
                      class="week-header-col"
                      v-ripple="{ center: true }"
                      v-for="(val, key) in week"
                      @click="allRowSelect(key)"
                    >
                      {{ val }}
                    </div>
                  </div>
                  <div class="week-body">
                    <div class="week-body-scroll-area">
                      <div class="week-body-container" style="height: 640px">
                        <div class="week-body-area">
                          <div class="week-body-time-col-area">
                            <div
                              class="week-body-time-col"
                              v-for="(val, key) in time"
                              v-ripple="{ center: true }"
                              @click="allColSelect(key)"
                            >
                              <span v-if="key !== '99'">{{ val }}時</span>
                              <span v-else-if="key === '99'">{{ val }}</span>
                            </div>
                          </div>
                          <div class="week-body-col-area" v-for="(val, key) in week">
                            <div
                              v-for="(val2, key2) in time"
                              class="week-body-col"
                              :class='{check_week_col: checkParam({week_id:key, time_id:key2}) }'
                              v-ripple="{ center: true }"
                              @click="itemSelect({ week_id:key, time_id:key2 })"
                            >
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </v-sheet>
            </v-col>
          </v-row>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import {mapGetters, mapState, mapActions} from 'vuex'
  import formatData from "../common/formatMixin";

  export default {
    name: 'BaseWeek',
    mixins: [formatData],
    props: {
      keyName: {
        type: String
      },
      param: {
        type: [Object],
        default: function () {
          return {
            '0': [],
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
          }
        }
      },
      hints: {
        type: String
      },
      option: {
        type: [Object],
        default: function () {
          return {
            dataList: [],
            isDisable: false,
            formType: 'input'
          }
        }
      }
    },
    data() {
      return {
        dialog: false,
        label: '',
        week: {
          '0': "日",
          '1': "月",
          '2': "火",
          '3': "水",
          '4': "木",
          '5': "金",
          '6': "土"
        },
        time: {
          8: 8,
          9: 9,
          10: 10,
          11: 11,
          12: 12,
          13: 13,
          14: 14,
          15: 15,
          16: 16,
          17: 17,
          18: 18,
          19: 19,
          20: 20,
          21: 21,
          22: 22,
          99: '深夜'
        },
        selectedItem: {
          '0': [],
          '1': [],
          '2': [],
          '3': [],
          '4': [],
          '5': [],
          '6': [],
        }
      }
    },
    watch: {
      param: function (to, from) {
        let flg = false;
        for ( let k in to ) {
          for ( let idx in to[k]) {
            if (!this.selectedItem[k].includes(to[k][idx])) {
              this.setParam();
            }
          }
        }

      }
    },
    methods: {
      open: function (data) {
        console.log(data);
      },
      onForm: function () {
        this.dialog = true;
      },
      allColSelect: function (col) {
        if (!this.option.isDisable) {
          let cnt = 0;
          let tmp = [];
          for (let i=0; i < 7; i++) {
            let week_id = String(i);
            if (this.selectedItem[week_id].includes(String(col))) {
              cnt += 1;
            }
          }
          if (cnt === 7) {
            for (let i=0; i < 7; i++) {
              let week_id = String(i);
              this.selectedItem[String(week_id)].splice(this.selectedItem[String(week_id)].indexOf(String(col)), 1);
            }
          } else {
            for (let i=0; i < 7; i++) {
              let week_id = String(i);
              if (!this.selectedItem[week_id].includes(String(col))) {
                this.selectedItem[String(week_id)].push(String(col));
              }
            }
          }
        }

      },
      allRowSelect: function (row) {
        if (!this.option.isDisable) {
          if (this.selectedItem[String(row)].length === 16) {
            this.selectedItem[String(row)] = [];
          } else {
            let tmp = [];
            for (let k in this.time) {
              tmp.push(String(k));
            }
            this.$set(this.selectedItem, String(row), tmp);
          }
        }
      },
      itemSelect: function (val) {
        if (!this.option.isDisable) {
          if (this.selectedItem[String(val.week_id)].includes(String(val.time_id))) {
            this.selectedItem[String(val.week_id)].splice(this.selectedItem[String(val.week_id)].indexOf(String(val.time_id)), 1);
          } else {
            this.selectedItem[String(val.week_id)].push(String(val.time_id));
          }
        }

      },
      checkParam: function (val) {
        if ( Object.keys(this.selectedItem).includes(String(val.week_id)) ) {
          return this.selectedItem[String(val.week_id)].indexOf(String(val.time_id)) !== -1 ;
        } else {
          return false
        }
      },
      onSubmit: function () {
        let tmp = [];
        for (let k in this.week) {
          if (this.selectedItem[String(k)].length > 0) {
            tmp.push(this.week[String(k)]);
          }
        }
        this.label = tmp.join('、');
        this.$emit('changeForm', {
          key: this.keyName,
          val: this.selectedItem
        });
        this.dialog = false;

      },
      setParam: function () {
        if (Object.keys(this.param).length > 0) {
          for (let key in this.param) {
            this.selectedItem[String(key)] = this.param[key];
          }
        }
        this.onSubmit();
      }
    },
    created: function () {
      this.setParam();
    },
    mounted: async function() {
      await this.$nextTick(() => {
        this.removeClassElement('v-text-field__details')
      })
    }
  }
</script>


<style lang="scss" scoped>
  .base-week {
    position: relative;
    z-index: 3;

    max-height: 43px;
    min-height: 43px;
    ::v-deep .v-text-field--solo, .v-text-field--outlined {
      border-radius: 0;
      height: 1vh;
    }

    ::v-deep .theme--light.v-text-field--outlined fieldset {
      border-color: white;
    }

    ::v-deep .v-text-field--outlined > .v-input__control > .v-input__slot {
      -webkit-box-align: stretch;
      -ms-flex-align: stretch;
      align-items: stretch;
      max-height: 43px;
      min-height: 43px;
    }

    ::v-deep .v-text-field.v-text-field--outlined .v-input__control {
      max-height: 43px;
      min-height: 43px;
    }

    ::v-deep .v-text-field > .v-input__control > .v-input__slot > .v-text-field__slot {
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
      flex: 1 1 auto;
      position: relative;
      padding: 8px 0;
    }

    .slide-fade-enter-active {
      transition: all .3s ease;
    }

    .slide-fade-leave-active {
      transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }

    .slide-fade-enter, .slide-fade-leave-to
      /* .slide-fade-leave-active below version 2.1.8 */
    {
      transform: translateX(10px);
      opacity: 0;
    }
  }

  .week-calender {
    display: flex;
    flex-direction: column;

    overflow-y: auto;
    .week-header {
      display: flex;
      border-bottom: #e0e0e0 1px solid;

      .week-header-empty-col {
        border-right: #e0e0e0 1px solid;
      }

      .week-header-col {
        border-right: #e0e0e0 1px solid;
        flex: 1 1 auto;
        position: relative;
        text-align: center;
      }
    }

    .week-body {
      display: flex;
      flex-direction: column;
      overflow: hidden;
      height: 100%;

      .week-body-scroll-area {
        flex: 1 1 auto;
        display: flex;
        align-items: flex-start;

        .week-body-container {
          width: 100%;
          overflow-y: hidden;
          flex: none;
          display: flex;
          align-items: flex-start;

          .week-body-area {
            display: flex;
            flex: 1;
            width: 100%;
            height: 100%;

            .week-body-time-col-area {
              flex: none;
              width: 45px;
              border-right: #e0e0e0 1px solid;

              .week-body-time-col {
                height: 40px;
                text-align: right;
                padding-right: 4px;
                border-bottom: none;
              }
            }

            .week-body-col-area {
              flex: 1;
              width: 0;
              position: relative;

              .week-body-col {
                border-right: #e0e0e0 1px solid;
                border-bottom: #e0e0e0 1px solid;
                height: 40px;
              }
              .check_week_col {
                background: #ff9800;
              }
            }
          }
        }

      }
    }
  }
</style>
