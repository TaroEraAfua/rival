
export default {
  namespaced: true,
  state: {
    userEdit: {
      add: {
        title: 'addUser',
        btn: ['addUser'],
        options: {
          'user_icon': {
            base: 'icon',
            hints: '',
            param: '',
            option: {},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {
                ope: 'ge',
                count: 5
              }
            },
            title: 'アイコン',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
          },
          'user_id': {
            base: 'text',
            hints: '半角英数字5文字以上',
            param: '',
            option: {},
            title: 'ユーザーID',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {
                ope: 'ge',
                count: 5
              }
            },
          },

          password1: {
            base: 'text',
            hints: '半角英数字8文字以上',
            param: '',
            option: {formType: 'password'},
            title: 'パスワード',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
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
          password2: {
            base: 'text',
            hints: '半角英数字8文字以上',
            param: '',
            option: {formType: 'password'},
            title: 'パスワード（再入力）',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
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
          'user_name': {
            base: 'text',
            hints: '',
            param: '',
            option: {},
            title: 'ユーザー名',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'string',
              option: {
                ope: 'ge',
                count: 5
              }
            },
          },
          mail: {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'email'},
            title: 'メールアドレス',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'mail',
              option: {}
            },
          },
          prefecture: {
            base: 'select',
            hints: '都道府県',
            param: '',
            option: {},
            title: '都道府県',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          city: {
            baseType: '',
            base: 'select',
            hints: '市区町村',
            param: '',
            option: {},
            title: '市区町村',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'birth_dt': {
            baseType: '',
            base: 'date',
            hints: '生年月日',
            param: '',
            option: {
              yearFlg : true
            },
            title: '生年月日',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gender: {
            baseType: '',
            base: 'radio',
            hints: '性別',
            param: '',
            option: {},
            title: '性別',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          position: {
            base: 'multiple',
            hints: '',
            param: [],
            option: {},
            title: 'ポジション',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          height: {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'number'},
            title: '身長',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: 'number',
              option: {}
            },
          },
          'ex_year': {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'number'},
            title: '経験年数',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: 'number',
              option: {}
            },
          },
          'ex_width': {
            base: 'multiple',
            hints: '',
            param: [],
            option: {},
            title: '経験',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          message: {
            base: 'textArea',
            hints: '',
            param: '',
            option: {},
            title: 'メッセージ',
            col: { title: 11, content: 11},
            md: { title: 11, content: 10 },
            primary: false,
            validation: {
              check: true,
              type: 'string',
              option: {}
            },
          },
        }
      },
      edit: {
        title: 'editUser',
        btn: ['editUser', 'cancel'],
        options: {
          'user_icon': {
            base: 'icon',
            hints: '',
            param: '',
            option: {},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {
                ope: 'ge',
                count: 5
              }
            },
            title: 'アイコン',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
          },
          'user_id': {
            base: 'output',
            hints: '半角英数字5文字以上',
            param: '',
            option: {},
            title: 'ユーザーID',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {
                ope: 'ge',
                count: 5
              }
            },
          },
          'user_name': {
            base: 'text',
            hints: '',
            param: '',
            option: {},
            title: 'ユーザー名',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'string',
              option: {
                ope: 'ge',
                count: 5
              }
            },
          },
          mail: {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'email'},
            title: 'メールアドレス',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'mail',
              option: {}
            },
          },
          prefecture: {
            base: 'select',
            hints: '都道府県',
            param: '',
            option: {},
            title: '都道府県',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          city: {
            baseType: '',
            base: 'select',
            hints: '市区町村',
            param: '',
            option: {},
            title: '市区町村',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'birth_dt': {
            baseType: '',
            base: 'date',
            hints: '生年月日',
            param: '',
            option: {
              yearFlg : true
            },
            title: '生年月日',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gender: {
            baseType: '',
            base: 'radio',
            hints: '性別',
            param: '',
            option: {},
            title: '性別',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          position: {
            base: 'multiple',
            hints: '',
            param: [],
            option: {},
            title: 'ポジション',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          height: {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'number'},
            title: '身長',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: 'number',
              option: {}
            },
          },
          'ex_year': {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'number'},
            title: '経験年数',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: 'number',
              option: {}
            },
          },
          'ex_width': {
            base: 'multiple',
            hints: '',
            param: [],
            option: {},
            title: '経験',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          message: {
            base: 'textArea',
            hints: '',
            param: '',
            option: {},
            title: 'メッセージ',
            col: { title: 12, content: 12},
            md: { title: 11, content: 10},
            primary: false,
            validation: {
              check: true,
              type: 'string',
              option: {}
            },
          }
        }
      }
    },
    search: {
      date: {
        prefecture: {
          base: 'select',
          hints: '都道府県',
          param: '',
          api: null,
          option: {}
        },
        city: {
          base: 'select',
          hints: '地域',
          param: '',
          api: null,
          option: {}
        },
        station: {
          base: 'select',
          hints: '最寄駅',
          param: '',
          api: null,
          option: {}
        },
        date: {
          base: 'date',
          hints: '活動日',
          param: [],
          api: null,
          option: {multiple: true}
        },
        purpose: {
          base: 'multiple',
          hints: '目的',
          param: [],
          api: null,
          option: {}
        },
        gender: {
          base: 'select',
          hints: '性別',
          param: '',
          api: null,
          option: {}
        },
      },
      detail: {
        prefecture: {
          base: 'select',
          hints: '都道府県',
          param: '',
          api: null,
          option: {}
        },
        city: {
          base: 'select',
          hints: '地域',
          param: '',
          api: null,
          option: {}
        },
        station: {
          base: 'select',
          hints: '最寄駅',
          param: '',
          api: null,
          option: {}
        },
        purpose: {
          base: 'multiple',
          hints: '目的',
          param: [],
          api: null,
          option: {}
        },
        gender: {
          base: 'select',
          hints: '性別',
          param: '',
          api: null,
          option: {}
        },
      }
    },
    teamEdit: {
      add: {
        title: 'addTeam',
        btn: ['addTeam'],
        options: {
          'image': {
            base: 'icon',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: 'アイコン',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'team_id': {
            base: 'text',
            hints: '半角英数字5文字以上',
            param: '',
            api: null,
            option: {},
            title: 'チームID',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {}
            },
          },
          'team_name': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: 'チーム名',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          prefecture: {
            base: 'select',
            hints: '都道府県',
            param: '',
            api: null,
            option: {},
            title: '都道府県',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          city: {
            base: 'select',
            hints: '市区町村',
            param: '',
            api: null,
            option: {},
            title: '市区町村',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          station: {
            base: 'select',
            hints: '最寄り駅',
            param: '',
            api: null,
            option: {},
            title: '最寄り駅',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gender: {
            base: 'radio',
            hints: 'チーム構成',
            param: '',
            api: null,
            option: {},
            title: 'チーム構成',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'average_age': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {formType: 'number'},
            title: '平均年齢',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          purpose: {
            base: 'multiple',
            hints: '目的',
            param: [],
            api: null,
            option: {},
            title: '目的',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          feature: {
            base: 'multiple',
            hints: 'チームの特徴',
            param: [],
            api: null,
            option: {},
            title: 'チームの特徴',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gym: {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '有り', val: 1},
              {label: '無し', val: 0},
            ],
            title: '体育館有無',
            col: { title: 12, content: 12},
            md: { title: 3, content: 9},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'main_place': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {formType: ''},
            title: 'メイン活動場所',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'member_num': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {formType: 'number'},
            title: 'メンバー数\n（リアル含）',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'stray_flg': {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '希望する', val: 1},
              {label: '希望しない', val: 0}
            ],
            title:
              `チーム外ユーザの\n試合・練習参加`,
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'solicitation': {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '希望する', val: 1},
              {label: '希望しない', val: 0},
            ],
            title: 'メンバー募集',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          c_comment: {
            base: 'textArea',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: '挑戦者へ一言',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          u_comment: {
            base: 'textArea',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: '勧誘メッセージ',
            col: { title: 12, content: 12},
            md: { title: 11, content: 10},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
        }
      },
      edit: {
        title: 'editTeam',
        btn: ['editTeam', 'cancel'],
        options: {
          'image': {
            base: 'icon',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: 'アイコン',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'team_id': {
            base: 'output',
            hints: '半角英数字5文字以上',
            param: '',
            api: null,
            option: {},
            title: 'チームID',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: 'halfStr',
              option: {}
            },
          },
          'team_name': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: 'チーム名',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          prefecture: {
            base: 'select',
            hints: '都道府県',
            param: '',
            api: null,
            option: {},
            title: '都道府県',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          city: {
            base: 'select',
            hints: '市区町村',
            param: '',
            api: null,
            option: {},
            title: '市区町村',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          station: {
            base: 'select',
            hints: '最寄り駅',
            param: '',
            api: null,
            option: {},
            title: '最寄り駅',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gender: {
            base: 'radio',
            hints: 'チーム構成',
            param: '',
            api: null,
            option: {},
            title: 'チーム構成',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'average_age': {
            base: 'text',
            hints: '',
            param: '',
            option: {formType: 'number'},
            title: '平均年齢',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          purpose: {
            base: 'multiple',
            hints: '目的',
            param: [],
            api: null,
            option: {},
            title: '目的',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          feature: {
            base: 'multiple',
            hints: 'チームの特徴',
            param: [],
            api: null,
            option: {},
            title: 'チームの特徴',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          gym: {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '有り', val: 1},
              {label: '無し', val: 0},
            ],
            title: '体育館有無',
            col: { title: 4, content: 8},
            md: { title: 3, content: 9},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'main_place': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {formType: ''},
            title: 'メイン活動場所',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'member_num': {
            base: 'text',
            hints: '',
            param: '',
            api: null,
            option: {formType: 'number'},
            title: 'メンバー数\n（リアル含）',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'stray_flg': {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '希望する', val: 1},
              {label: '希望しない', val: 0}
            ],
            title:
              `チーム外ユーザの\n試合・練習参加`,
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          'solicitation': {
            base: 'radio',
            hints: '',
            param: [],
            api: null,
            option: [
              {label: '希望する', val: 1},
              {label: '希望しない', val: 0},
            ],
            title: 'メンバー募集',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: true,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          c_comment: {
            base: 'textArea',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: '挑戦者へ一言',
            col: { title: 12, content: 12},
            md: { title: 11, content: 6},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
          u_comment: {
            base: 'textArea',
            hints: '',
            param: '',
            api: null,
            option: {},
            title: '勧誘メッセージ',
            col: { title: 12, content: 12},
            md: { title: 11, content: 10},
            primary: false,
            validation: {
              check: true,
              type: '',
              option: {}
            },
          },
        }
      }
    }
  },
  getters: {
    getPageData (state) {
      return function (keyList) {
        if ( Object.keys(keyList).includes('page')
          && Object.keys(keyList).includes('part') ) {
          return JSON.parse(JSON.stringify(state[keyList.page][keyList.part]));
        } else if ( Object.keys(keyList).includes('page') ) {
          return JSON.parse(JSON.stringify(state[keyList.page]));
        }
        return null
      };
    },
  }
}
