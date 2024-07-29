<template>
  <v-container fluid>
    <v-card>
      <v-row>
        <v-col style="padding-top: 0px;">
          <v-toolbar
            color="#FFB74D"
          >
            <v-tabs
              background-color="transparent"
              fixed-tabs
              centered
            >
              <v-tab
                v-for="(item, key, idx) in tabTitle"
                :key="key"
                @click="onTab(key)"
              >
                {{ item.title }}
              </v-tab>
            </v-tabs>
          </v-toolbar>
        </v-col>
      </v-row>
      <v-row>
        <v-col style="padding-top: 0px;">
        <v-tabs-items v-model="tabItem">
          <v-tab-item
            v-for="(item, key, idx) in tabTitle"
            :value="key"
            style=" overflow-y: auto;max-height: 70vh;"
          >
            <v-card flat>
              <div style="margin-left: 2vw; margin-right: 2vw">
                <template v-for="rowData in selectTeamList(key)">
                  <v-row>
                    <v-col class="col-span">
                      <base-list-card
                              :formatData="challengeInfo"
                              :rowData="rowData"
                              @onCardBtn="onCardBtn"
                              @onCardDetail="onCardDetail"
                      />
                    </v-col>
                  </v-row>
                </template>
              </div>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
        </V-col>
      </v-row>

    </v-card>
  </v-container>
</template>

<script>
  import { mapActions, mapGetters, mapState } from 'vuex';
  import SearchList from "./SearchList";
  import BaseListCard from "../part/BaseListCard";
  import ActionMixin from "../common/ActionMixin";
  export default {
    name: 'Challenge',
    mixins: [ActionMixin],
    components: {
      SearchList,BaseListCard
    },
    props: {

    },
    data: function() {
      return {
        tabItem: 'send',
        tabTitle: {
          send: {title: '送った'},
          receive: {title: '受けた'},
          match: {title: '成立'},
        }
      }
    },
    computed: {
      ...mapState('challenge',['sendTeamList', 'receiveTeamList', 'matchTeamList']),
      ...mapState('constant', ['challengeInfo']),
      ...mapState('auth', ['joinTeamList']),
    },
    watch: {

    },
    methods: {
      ...mapActions('challenge', ['getChallengeList','matchChallenge', 'deleteChallenge', 'cancelChallenge']),
      ...mapActions('auth', [
        'setSelectMenu'
      ]),
      onTab: function (key) {
        this.$nextTick(() => { this.tabItem = key })
      },
      selectTeamList: function (key) {
        return this[key + 'TeamList']
      },
      onCardDetail: function ({key, data}) {

      },
      onCardBtn: async function ({key, data}) {
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
      },
      getChallengeData: async function () {
        console.log(this.joinTeamList.select);
        if (this.joinTeamList.select) {
          await this.getChallengeList(this.joinTeamList.select);
        }
      },
    },
    created: async function () {
      this.getChallengeData();
    }
  }
</script>

<style  lang="scss" scoped>
  .toolbar-des {
    background-color: #90a4ae;
  }
</style>
