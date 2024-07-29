
<script>
  import { mapActions, mapGetters, mapState } from 'vuex';
  import isMobile from 'ismobilejs'
  import formatMixin from "./formatMixin";
  export default {
    name: 'ActionMixin',
    mixins: [formatMixin],
    data() {
      return {

      }
    },
    computed: {
      ...mapState('auth', ['userList'])
    },
    methods: {
      ...mapActions('common', ['resetFlg']),
      ...mapActions('auth', ['setSelectMenu']),

      /**
       * フォーム入力項目設定
       * @param param
       * @returns {Promise<void>}
       */
      changeForm: async function (param) {
        if (param.key === 'city') {
          await this.setAriaApiParam(param);
          await this.getStation();
          if (Object.keys(this.options).includes('station') ) {
            await this.makeOptionData('options', 'station');
            await this.$set(this.options['station'], 'param', '');
            await this.$set(this.options['station'], 'api', null);
          }
        } else if (param.key === 'prefecture') {
          await this.setAriaApiParam(param);
          await this.getCity();
          await this.makeOptionData('options', 'city');
          if (Object.keys(this.options).includes('station') ) {
            await this.makeOptionData('options', 'station');
            await  this.$set(this.options['station'], 'param', '');
            await this.$set(this.options['station'], 'api', null);
          }

          await this.$set(this.options['city'], 'param', '');
          await this.$set(this.options['city'], 'api', null);
        }
        this.$set(this.options[param.key], 'param', param.val);
        this.$set(this.options[param.key], 'api', param);
      },
      movePage: async function (path, main=null, sub=null) {
        this.resetFlg();
        const res = {
          path: path,
          main: main,
          sub: sub
        };
        if (path !== this.$route.path ){
          await this.setSelectMenu(res);
          this.$router.push(path);
        } else if ('/my_page' === this.$route.path) {
          this.setSelectMenu(res);
        }
      },
      checkMobile () {
        let res = isMobile().phone;
        return !res;
      },
      checkType: function (val) {
        return Object.prototype.call(val).slice(8. -1)
      },
      checkRequired: function (param) {
        // 存在チェックのみ 問題なければ空文字返却
        let tmp = '';
        switch (this.checkTypeOf(param)) {
          case 'null':
            tmp = '入力が必須の項目です';
            break;
          case 'undefined':
            tmp = '入力が必須の項目です';
            break;
          case 'number':
            tmp = param !== 'NaN' ? '' : '入力が必須の項目です';
            break;
          case 'object':
            tmp = Object.keys(param).length > 0 ? '' : '入力が必須の項目です';
            break;
          case 'string':
          case 'array':
            tmp = param.length > 0 ? '' : '入力が必須の項目です';
            break;
        }
        return tmp
      },
      checkLength : function (param, ope, count) {
        // パラメータによって以上か以下かの比較方法を変更する
        let formula = '';
        // 以上・以下の文字列を入れる
        let comStr = '';
        // gt: 以上 | eq: 同一 | lt:以下
        switch (ope) {
          case 'ge':
            comStr = '以上の';
            formula = (param.length >= count);
            break;
          case 'eq':
            comStr = 'の';
            formula = (param.length === count);
            break;
          case 'le':
            comStr = '以下の';
            formula = (param.length <= count);
            break;
        }
        return formula ? '' : comStr
      },
      checkHalfStr: function(str, ope, count) {
        // 半角英数字と文字数チェック(count=文字数) 問題なければfalse返却
        let tmp = '';
        if (str) {
          if (str.match(/^[A-Za-z0-9]+$/) === null) {
            tmp = '半角英数字以外の文字が含まれています';
          } else {
            let comStr = this.checkLength(str, ope, count);
            if (comStr !== '') {
              tmp = count + '文字' + comStr + '半角英数字を入力してください';
            }
          }
        }
        return tmp
      },
      checkNumeric: function(num, ope, count) {
        // ニューメリックと桁数チェック(count=桁数) 問題なければfalse返却
        let tmp = '';
        if (num) {
          let Snum = num;
          if (this.checkTypeOf(num) === 'number') {
             Snum = String(num);
          }
          if (Snum.match(/^[0-9]+$/) === null) {
            tmp = '半角数字以外の文字が含まれています';
          } else if (Snum < 0) {
            tmp = '0以上の数値を入力してください'
          } else {
            let comStr = this.checkLength(Snum, ope, count);
            if (comStr !== '') {
              tmp = count + '桁' + comStr + '半角数字を入力してください';
            }
          }
        }
        return tmp
      },
      checkWeekReq: function (param) {
        let tmp = '';
        if (param && Object.keys(param).length > 0) {
          let sum = 0;
          for (let key in param) {
            sum += param[String(key)].length
          }
          if (sum === 0) {
            tmp = '入力が必須の項目です'
          }
        }
        return tmp
      },
      checkMail: function (param) {
        let result = '';
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        if (!pattern.test(param)) {
          result = '入力値に不備があります'
        }

        return result
      },
      checkValidation: function (opt, param) {
        let options = JSON.parse(JSON.stringify(opt));
        let res = {};
        for (let key in options) {
          console.log(key);
          let msgtmp = '';
          // 順番にチェックしていきメッセージを配列で追加
          if (['password1'].includes(key)) {
            if (param["password1"] !== param["password2"]) {
              msgtmp = 'パスワードが一致しません';
              res[key] = msgtmp;
              continue;
            }
          }
          if (options[key].validation.check) {
            if (options[key].primary) {
              msgtmp = this.checkRequired(param[key]);
              if (msgtmp.length > 0) {
                res[key] = msgtmp;
                continue;
              }
            }


            switch (options[key].validation.type) {
              case 'number':
                msgtmp = this.checkNumeric(
                  param[key]
                  , options[key].validation.option.ope
                  , options[key].validation.option.count
                );
                break;
              case 'halfStr':
                msgtmp = this.checkHalfStr(
                  param[key]
                  , options[key].validation.option.ope
                  , options[key].validation.option.count
                );
                break;
              case 'week':
                msgtmp = this.checkWeekReq(param[key]);
                break;
              case 'mail':
                msgtmp = this.checkMail(param[key]);
                break;
            }

            if (msgtmp !== '') {
              res[key] = msgtmp;
            }
          }
        }
        return res
      },
      checkJoinTeamId: function (checkId) {
        return checkId === this.userList.user_id
      },
      setConfirmationDialogOption: function (key) {
        this.$set(this.confirmationDialogOption.param, 'dialogKey', this.confirmationDialogOption[key].dialogKey);
        this.$set(this.confirmationDialogOption.param, 'btnKeyList', this.confirmationDialogOption[key].btnKeyList);
      }
    },
  }

</script>
