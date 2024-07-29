<template>

  <v-navigation-drawer
    class="my-page-side-menu"
    v-model="drawer"
    :mini-variant.sync="mini"
    mini-variant-width="70"

    permanent
  >
    <template v-slot:prepend>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img :src="userList.icon" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> {{ userList.user_name }} </v-list-item-title>
        </v-list-item-content>
        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>
    </template>
    <v-divider />
    <sub-side-menu
    />
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import SubSideMenu from "./SubSideMenu";
export default {
  name: 'SideMenu',
  components: {
    SubSideMenu
  },
  props: {

  },
  data: function() {
    return {
      drawer: true,
      arrow:'mdi-chevron-left',
      move: 'account',
      mini: false,
    }
  },
  computed: {
    ...mapState('auth', ['userList']),
  },
  watch: {
    mini: function (flg) {
      let size = flg ? 0 : 2;
      this.$emit('changeSize', size);
    },
  },
  methods: {
    ...mapActions('auth', ['setSelectMenu']),
    selectMenu: function (main, sub=null) {
      // this.$route.path
      this.setSelectMenu({
        path: this.$route.path,
        main: main,
        sub: sub
      });
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
 .my-page-side-menu {
   width: 256px;
 }
</style>
