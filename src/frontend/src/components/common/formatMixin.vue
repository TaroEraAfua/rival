
<script>
  import { mapActions, mapGetters, mapState } from 'vuex';
  export default {
    name: 'formatMixin',
    data() {
      return {

      }
    },
    computed: {
      ...mapGetters('common', ['getComList']),
      ...mapGetters('pageContent', ['getPageData']),
      ...mapGetters('area', ['getAreaList'])
    },
    methods: {
      ...mapActions('common', ['getConData']),
      getPageContent: function (keyList) {
        return this.getPageData(keyList);
      },
      /**
       * セレクトボックス用　フォーマット作成
       * @param data
       * @param key
       * @returns {{}}
       */
      makeSelectOption: function (data, key=null) {
        let res = {};
        if (typeof data === "undefined") {
          return res
        }
        if (data && data.length > 0) {
          let keys = Object.keys(data[0]);
          for (let k in keys) {
            res[keys[k]] = keys[k];
          }
          res.item = data;
        } else if (key === 'city') {
          res = {
            label: 'label',
            val: 'idx',
            item: [{idx: 0, label: '都道府県を選択してください', item:{city_id: ''}}]
          }
        }
        return res
      },
      /**
       * 駅選択リストデータ作成
       * @param data
       */
      makeStationParam: function (data) {
        let res = {};
        if (data.length > 0) {
          res = {
            label: 'label',
            val: 'val',
            item: data
          }
        } else if (!this.city || this.city.length === 1 || this.city.length === 0 ) {
          res = {
            label: 'label',
            val: 'val',
            item: [{val: 0, label: '都道府県を選択してください', item:{station_id: '', line_id: ''}}]
          }
        } else {
          res = {
            label: 'label',
            val: 'val',
            item: [{val: 0, label: '地域を選択してください', item:{station_id: '', line_id: ''}}]
          }
        }
        return res
      },
      /**
       * チーム・個人情報表示用
       * @param target
       */
      makeInfoParam: async function (target={}) {
        let tmp = {};
        if (!this.getComList('stateFlg')) {
          await this.getConData();
        }
        if (Object.keys(this.infoItem[target]['list']).length > 0) {
          for (let k in this.infoItem[target]['list']) {
            let param = "";
            let optionData = this.getComList(k);
            if (k === 'week') {
              param = this.infoItem[target]['list'][k]
            } else if (k === 'game_date') {
              param = this.infoItem[target]['list'][k] ? this.infoItem[target]['list'][k].join('、') : ' - ';
            } else if (k === 'station_name') {
              tmp['station'] = this.infoItem[target]['list']['line_name'] + ' - ' + this.infoItem[target]['list']['station_name']
              continue
            } else if (optionData) {
              if (this.infoItem[target]['list'][k] instanceof Array) {
                let t = [];
                for (let i in this.infoItem[target]['list'][k]) {
                  for (let j in optionData) {
                    if (String(optionData[j]['val']) === String(this.infoItem[target]['list'][k][i])) {
                      t.push(optionData[j]['label']);
                      break;
                    }
                  }
                }
                param = t.join('、')
              } else {
                let targetVal = '';
                for (let t in optionData) {
                  if (optionData[t].val === this.infoItem[target]['list'][k]) {
                    targetVal = optionData[t]['label'];
                  }
                }
                param = targetVal;
              }
            } else {
              param = this.infoItem[target]['list'][k]
            }
            tmp[k] = param
          }
        }

        this.$set(this.infoData, "type", target);
        this.$set(this.infoData, "title", this.infoItem[target]["title"]);
        this.$set(this.infoData, "list", tmp);
        this.$set(this.infoData, "format", this.infoItem[target]["format"]);
        const btn = Object.keys(this.infoItem[target]).includes("btn") ? this.infoItem[target]["btn"] : {} ;
        this.$set(this.infoData, "btn", btn);
      },
      /**
       * セレクトボックス一括設定
       * @param key　表示するjsonリスト
       * @param target　指定する項目
       * @param param 初期値
       */
      makeOptionData: async function (key='options', target=null, param=null) {
        if (!this.getComList('stateFlg')) {
          await this.getConData();
        }
        if (target) {
          let optionData = this.getComList(target);
          await this.setOptionData(this[key], target, optionData);
        } else {
          for (let k in this[key]) {
            let optionData = this.getComList(k);
            this.setOptionData(this[key], k, optionData);
            if (param) {
              switch (this[key][k]['base']) {
                case 'week':
                  await this.$set(this[key][k], 'param', param[k]);
                  break;
                case 'multiple':
                  let tmp = [];

                  for (let idx in this[key][k].option.item) {
                    for (let i in param[k]) {
                      if (this[key][k].option.item[idx].val === param[k][i] ) {
                        tmp.push(this[key][k].option.item[idx]);
                        continue;
                      }
                    }
                  }
                  console.log(param[k]);
                  console.log(this[key][k].option.item);
                  await this.$set(this[key][k], 'param', tmp);
                  this[key][k]['api'] = {key: k, val: tmp};
                  break;
                case 'select':
                  if (k === 'station') {
                    let areaList = this.getAreaList('station');
                    let tmp_val;
                    for (let i in areaList) {
                      if ((areaList[i].item.line_id === param.line.key) && (areaList[i].item.station_id === param.station.key)) {
                        tmp_val = areaList[i].val;
                      }
                    }
                    let station_info = {
                      item: {
                        line_id: param.line.key,
                        line_name: param.line.val,
                        station_id: param.station.key,
                        station_name: param.station.val
                      },
                      label: param.line.val + ' - ' + param.station.val,
                      val: tmp_val
                    };
                    await this.$set(this[key][k], 'param', tmp_val);
                    this[key][k]['api'] = {key: k, val: tmp_val};
                  } else {
                    this[key][k]['api'] = {key: k, val: param[k]['key']};
                    await this.$set(this[key][k], 'param', param[k]['key']);
                  }
                  break;
                default:
                  this[key][k]['api'] = {key: k, val: param[k]};
                  await this.$set(this[key][k], 'param', param[k]);
              }
            }
          }
        }
      },
      delGender: async function () {
        for (let i in this.options.gender.option) {
          if (this.options.gender.option[i].id === 3) {
            let del_gender = this.options.gender.option.slice(0, i);
            await this.$set(this.options.gender, 'option', del_gender);
          }
        }
      },
      setOptionData: function (data, target, optionData) {
        const optionType = this.checkTypeOf(data[target]['option']);
        if (target === 'station') {
          this.$set(data[target], 'option', this.makeStationParam(this[target]));
        } else if (optionData) {
          if ( data[target]['base'] === 'multiple'){
            this.$set(data[target], 'option', this.makeSelectOption(optionData));

          } else if ( data[target]['base'] === 'select' ) {
            this.$set(data[target], 'option', this.makeSelectOption(optionData));
          } else {
            this.$set(data[target], 'option', optionData);
          }
        } else if (data[target]['option']) {
          if (Object.keys(data[target]['option']).length > 0) {
            if (this[target]) {
              this.$set(data[target], 'option', this.makeSelectOption(this[target], target));
            }
          } else if (Object.keys(data[target]).includes('base') && data[target]['base'] === 'text') {
          } else if (target === 'week') {

          } else {
            this.$set(data[target], 'option', this.makeSelectOption(this[target], target));
          }
        }
      },
      checkTypeOf: function (obj) {
        let toString = Object.prototype.toString;
        return toString.call(obj).slice(8, -1).toLowerCase();
      },
      makeApiData: function (options) {
        let result = {};
        for (let key in options) {
          if ('multiple' === options[key]['base']) {
            let tmp = [];
            console.log(options[key]['api']);
            if (options[key]['api']) {
              for (let idx in options[key]['api']['val']) {
                tmp.push(options[key]['api']['val'][idx]['val']);
              }
            }
            result[key] = {key: key, val: tmp};
          } else if (key === 'station') {
            if (options[key]['api']) {
              const stationList = options[key].option.item[options[key]['api']['val']];
              if (stationList) {
                result[key] = {
                  key: key,
                  val: {
                    line_id: stationList.item.line_id,
                    station_id: stationList.item.station_id
                  }
                };
              }

            } else {
              result[key] = {
                key: key,
                val: {
                  line_id: '',
                  station_id: '',
                }
              };
            }

          } else if ('icon' === options[key]['base']) {
            if (options[key]['api']) {
              result[key] = {};
            } else {
              result[key] = options[key]['api'];
            }
          } else {
            result[key] = options[key]['api'];
          }

        }
        return result
      },
      removeClassElement :function(className) {
        let elements = document.getElementsByClassName(className);
        for (let i = 0; i < elements.length; i++) {
          let e = elements[i];
          if (e) {
            e.parentNode.removeChild(e);
          }
        }
      }
    }
  }

</script>
