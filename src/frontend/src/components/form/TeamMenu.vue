<template>
  <v-overlay style="z-index: 3;">
    <div class="team-menu-head">

    </div>
    <v-card class="team-menu">
      <template  v-if="authFlg">
        <v-card-title style="padding: 0;">
          <p style="margin: auto; padding-top: 5px; padding-bottom: 5px">チーム切替</p>
        </v-card-title>

        <v-divider class="mx-4"/>

        <template v-if="itemList.length > 0">
          <v-container
          id="scroll-target"
          style="max-height: 220px"
          class="overflow-y-auto"
          >
            <v-row v-scroll
              align="center"
              justify="center"
            >
              <v-list dense style="width: 100vw;">
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item
                    v-for="(item, i) in itemList"
                    :key="i"
                    @click="selectItem(item.team_id)"
                  >
                    <v-list-item-icon>
                      <v-img
                        class="team-image"
                        :src="item.icon"
                        dark
                      />
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title> {{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-row>
          </v-container>
        </template>

      </template>

    </v-card>
  </v-overlay>
</template>

<script>
import { mapActions, mapGetters,mapState } from 'vuex';
import formatMixin from "../common/formatMixin";
import ActionMixin from '../common/ActionMixin';
export default {
  name: 'TeamMenu',
  mixins: [formatMixin, ActionMixin],
  components: {
  },
  props: {

  },
  data: function() {
    return {
      itemList: [],
      item: 1,
    }
  },
  computed: {
    ...mapState('auth', ['authFlg', 'userList', 'joinTeamList']),
  },
  watch: {
    joinTeamList: {
      handler: function (to, from) {
        this.makeMenuList(to);
      },
      deep: true
    }
  },
  methods: {
    ...mapActions('auth', ['logOut', 'setDefaultTeam']),
    makeMenuList: function (teamList) {
      let tmp = [];
      for (let idx in teamList.team) {
        if (teamList.select === teamList.team[idx].team_id) {
          this.item  = Number(idx);
        }
        tmp.push({
          team_id: teamList.team[idx].team_id,
          title: teamList.team[idx].team_name,
          icon: teamList.team[idx].team_image,
        })
      };
      this.itemList = tmp;
    },
    selectItem: function (id) {
      if(id === this.joinTeamList.select) {
        id = ''
      }
      this.setDefaultTeam(id);
    },
  },
  created () {
    if ( this.authFlg ) {
      this.makeMenuList(this.joinTeamList);
    } else {

    }
  }
}
</script>

<style  lang="scss" scoped>
  .team-menu-head{
    height: 55vh;
    z-index: 1;
  }
  .team-menu {
    height: 45vh;
    bottom: 0;
    width: 100vw;
    z-index: 2;
    .user-image {
      border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
      //margin: auto;
      background-position: left top;  /* 横長画像の左上を基準に表示 */
      display: inline-block;
    }
    .team-image {
      border-radius: 50%;  /* 角丸半径を50%にする(=円形にする) */
      height: 30px;
      width: 30px;
      display: inline-block;
    }
  }

</style>
