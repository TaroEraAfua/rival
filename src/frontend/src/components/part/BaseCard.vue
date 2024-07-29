<template>
  <v-card class="base-card mx-auto">
    <v-container>
      <v-row>
        <v-col cols="12" md="3">
          <v-img
            height="200"
            width="200"
            src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
            style="margin: auto;"
          ></v-img>

        </v-col>
        <v-col cols="12" md="9">
          aaa<br />
          aaa<br />
          aaa<br />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { mapGetters, mapState,mapActions } from 'vuex'
export default {
  name: 'BaseCard',
  props: {
    keyName: {
      type: String
    },
    param: {
      type: [String, Number,Array, Object]
    },
    hints: {
      type: String
    },
    option: {
      type: Object,
      default: function () {
        return {
          label: '',
          val: '',
          item: [] ,
        }
      }
    }
  },
  data: function() {
    return {


    }
  },
  computed: {
  },
  watch: {

  },
  methods: {

  },
  created () {


  }
}
</script>

<style  lang="scss" scoped>
  .base-card {

  }

</style>
