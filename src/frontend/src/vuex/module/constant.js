
export default {
  namespaced: true,
  state: {
    dialogContent: {
      add: {
        title: '登録確認',
        content: '入力した内容で登録します。よろしいですか？'
      },
      edit: {
        title: '更新確認',
        content: '入力した内容で更新します。よろしいですか？'
      },
      moveLogin: {
        title: '',
        content: '続けてチーム登録も行いますか？'
      },
      detailTeam: {
        title: 'チーム情報',
      },
      btn: {
        confirm: {label: '実行', color: 'blue'},
        cancel: {label: 'キャンセル', color: 'gray'},
        moveLogin: {label: 'ログイン画面へ', color: 'blue'},
      },
    },
    pageOption: {
      title: {
        addUser: 'アカウント登録',
        editUser: 'アカウント更新',
        addTeam: 'チーム作成',
        editTeam: 'チーム更新',
        gameDateEdit: '試合日程編集'
      },
      btn: {
        addUser: 'アカウント作成',
        editUser: 'アカウント更新',
        addTeam: 'チーム作成',
        editTeam: 'チーム更新',
        gameDateEdit: ' 試合設定',
        cancel: 'キャンセル',
      }
    },
    menuList: {
      about: { label: 'このサイトについて', icon: 'mdi-tooltip-account',},
      search: { label: '検索', icon: 'mdi-magnify' },
      my_page: {label: 'マイページ', icon: 'mdi-account-outline'},
    },
    keyList: {
      birth_dt: '誕生日',
      city_name: '市区町村',
      ex_year: '経験年数',
      gender: '性別',
      height: '身長',
      icon: 'アイコン',
      position: 'ポジション',
      prefecture_name: '都道府県',
      user_id: 'ユーザーID',
      user_name: 'ユーザー名',
      week: 'メイン活動日'
    },
    userInfo: {
      icon: {label: 'アイコン', type: 'img', col: {label: 6, data: 6}, md: {label: 3, data: 9}},
      user_id: {label: 'ユーザーID', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      birth_dt: {label: '誕生日', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      prefecture: {label: '都道府県', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      city: {label: '市区町村', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      ex_year: {label: '経験年数', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      gender: {label: '性別', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      height: {label: '身長', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      position: {label: 'ポジション', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
    },
    teamInfo: {
      team_image: {label: 'アイコン', type: 'img', col: {label: 6, data: 6}, md: {label: 3, data: 9}},
      team_id: {label: 'チームID', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      purpose: {label: '目的', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      prefecture: {label: '都道府県', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      city: {label: '市区町村', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      station: {label: '駅', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      gender: {label: '性別', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
      game_date: {label: '活動日程', type: 'text', col: {label: 6, data: 6}, md: {label: 3, data: 3}},
    },
    challengeInfo: {
      title: {
        team_name: {},
      },
      image: {
        team_image: {}
      },
      area: {
        prefecture: 'val',
        city: 'val',
      },
      data: {
        line: {},
        purpose: {},
        game_date: {},
      },
      button: {
        request: {label: '挑戦状を送る'},
        response: {label: '挑戦を受ける'},
        reject: {label: '挑戦を断る'},
        cancel: {label: '挑戦を取下'},
        chat: {label: 'チャットへ'},
      },
    },
    searchTeamFormat: {
      title: {
        team_name: {},
      },
      image: {
        team_image: {}
      },
      area: {
        prefecture: 'val',
        city: 'val',
      },
      data: {
        line: {},
        purpose: {},
        game_date: {},
      },
      button: {
        join: {label: 'チームへ参加する'},
        request: {label: '挑戦状を送る'},
        response: {label: '挑戦を受ける'},
        reject: {label: '挑戦を断る'},
        cancel: {label: '挑戦を取下'},
        chat: {label: 'チャットへ'},
      },
    },
  },
  getters: {
    getKey (state) {
      return function (key) {
        return state.keyList[key];
      };
    },
    getOption (state) {
      return function (key) {
        console.log(state);
        console.log(key);
        const tmp = state[key];
        return tmp
      };
    }
  }
}
