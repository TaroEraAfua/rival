<template>
  <v-card>
    <v-snackbar
      v-model="snackbar"
      :color="color"
      :timeout="timeout"
      top
      right
      vertical
    >
      {{ text }}
      <v-btn
        dark
        text
        @click="onClose"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-card>
</template>

<script>
  import { mapActions, mapGetters, mapState } from 'vuex';
export default {
  name: 'ViewMessage',
  components: {
  },
  props: {
    message: {
      type: [Object, Boolean],
      default: function () {
        return null
      }
    }
  },
  data: function() {
    return {
      color: '',
      text: '',
      snackbar: false,
      showFlg: false,
      timeout: 4000,
    }
  },
  computed: {
    ...mapState('common', ['commonMsg']),
  },
  watch: {
    commonMsg: {
      handler: function (to, from) {
        if ( to.message && to.message !== this.text ) {
          this.viewSnack(to);
        }
      },
      deep: true
    },
    snackbar: function (to) {
      if (!to) {
        this.text = '';
      }
    }
  },
  methods: {
    viewSnack: function (messageData) {
      switch (messageData.result_cd) {
        case '001':
          this.color = 'blue lighten-2';
          break;
        case '002':
          this.color = 'error';
          break;
        case '900':
          this.color = 'error';
          break;
      }
      this.text = messageData.message;
      this.snackbar = true;
    },
    onClose: function () {
      this.snackbar = false;
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>

</style>
