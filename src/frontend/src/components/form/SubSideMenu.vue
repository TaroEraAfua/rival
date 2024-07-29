<template>
  <v-list dense>
    <template v-for="(item, key, idx) in menuList">

      <template v-if=" idx === 1 && checkAddTeam ">
        <v-list-item
          @click="selectMenu('addTeam')"
        >
          <v-list-item-icon style="margin-left: 10px; margin-right: 10px;">
            <i class="fas fa-users"></i>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>チーム作成</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
      <template
        v-if="Object.keys(item).indexOf('sub') !== -1"
      >
        <v-list-group
          style="margin-left: 10px; margin-right: 10px;"
          :prepend-icon="item.icon"
          v-model="item.select"
          :value="!!item.select"
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item
            v-for="(subItem, idx ) in item.sub"
            :key="idx"
            link
            @click="selectMenu(key, subItem)"
            :style="checkSelectStyle(subItem)"
          >
            <v-list-item-avatar>
              <v-img :src="subItem.icon" />
            </v-list-item-avatar>
            <v-list-item-title> {{ subItem.title }}</v-list-item-title>
          </v-list-item>
        </v-list-group>
      </template>
      <template v-else>
        <v-list-item
          @click="selectMenu(key)"
        >
          <v-list-item-icon style="margin-left: 10px; margin-right: 10px;">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </template>
  </v-list>

</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import ActionMixin from "../common/ActionMixin";
import formatMixin from "../common/formatMixin";
import SideMenu from "./SideMenu";
export default {
  name: 'SubSideMenu',
  mixins: [ActionMixin],
  components: {
  },
  props: {

  },
  data: function() {
    return {
      selectItem : {},
      menuList: {
        user: { title: 'アカウント情報', icon: 'mdi-account', type: ''},
        team: { title: '所属チーム情報', icon: 'mdi-account-group-outline', type: 'team',
          sub: [], select: null,
        },
        challenge: { title: '挑戦状一覧', icon: 'mdi-yin-yang'},
        chat: { title: 'チャットルーム', icon: 'mdi-wechat',
          sub: [],
          select: '',
        },
      }
    }
  },
  computed: {
    ...mapState('auth', [
      'joinTeamList', 'userList'
    ]),
    checkAddTeam: function () {
      if (this.joinTeamList.team) {
        for (let idx in this.joinTeamList.team) {
          if (this.joinTeamList.team[idx].admin === 1) {
            return false;
          }
        }
      }
      return  true
    }
  },
  watch: {
    mini: function (flg) {
      let size = flg ? 0 : 2;
      this.$emit('changeSize', size);
    },
    joinTeamList: {
      handler: function (to, from) {
        this.makeMenuList(to);
      },
      deep: true
    }
  },
  methods: {
    ...mapActions('auth', ['setSelectMenu']),
    ...mapActions('common', ['changeOverFlow']),
    checkSelectStyle: function (item) {
      return item.team_id === this.joinTeamList.select ? 'background-color: ;' : ''
    },
    makeMenuList: function (teamList) {
      let tmpTeam = [];
      let tmpChat = [];
      console.log('makeMenuList');
      for (let idx in teamList.team) {
        let row = teamList.team[idx];
        tmpTeam.push({
          idx: idx,
          team_id: row.team_id,
          title: row.team_name,
          icon: row.team_image,
        });
        for (let i in row.challenge) {
          let cha = row.challenge[i];
          if (cha.status) {
            if (cha.status === 1 && cha['send_id'] === teamList.select) {
              tmpChat.push({
                title: cha.res_name,
                icon: '',
                chat_id: cha.id
              });
            } else if ( cha.status === 1 && cha['res_id'] === teamList.select ) {
              tmpChat.push({
                title: cha.send_name,
                icon: '',
                chat_id: cha.id
              });
            }
          }
        }
      }
      this.$set(this.menuList.team, 'sub', tmpTeam);
      this.$set(this.menuList.chat, 'sub', tmpChat);
    },
    selectMenu: function (main, sub=null) {
      this.changeOverFlow();
      if (this.$route.path !== '/my_page') {
        this.movePage('/my_page', main, sub);

      } else {
        const res = {
          path: this.$route.path,
          main: main,
          sub: sub
        };
        this.setSelectMenu(res);
      }
    },

  },
  created () {
    this.makeMenuList(this.joinTeamList);
  }
}
</script>

<style  lang="scss" scoped>
 .my-page-side-menu {
   width: 256px;
   min-height: 80vh;
 }
</style>
