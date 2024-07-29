<template>
  <v-container class="base-check">
    <v-row class="base-check-row" >
      <template v-for="(item, key) in option">
        <v-col cols="auto" class="base-check-col">
          <v-checkbox
            v-model="checkPosition"
            :label="item.label"
            :value="item.val"
            @change="changeForm"
          />
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script>
  import formatData from "../common/formatMixin";

export default {
  name: 'BaseCheck',
  mixins: [formatData],
  props: {
    keyName: {
      type: String
    },
    param: {
      type: [String, Number, Object, Array]
    },
    hints: {
      type: String
    },
    option: {
      type: [Object, Array]
    }
  },
  data: function() {
    return {
      checkPosition: [],
    }
  },
  components: {

  },
  computed: {

  },
  watch: {
    param: function (to, from) {
      if (to) {
        for (let idx in to) {
          if (!this.checkPosition.includes(to[idx])) {
            this.checkPosition = to;
            break;
          }
        }
      }
    }
  },
  methods: {
    changeForm: function () {
      let r = {key: this.keyName, val: this.checkPosition };
      this.$emit('changeForm', r);
    },
  },
  created () {
  },
  mounted: async function() {
    await this.$nextTick(() => {
      this.removeClassElement('v-text-field__details')
    })
  }
}
</script>

<style  lang="scss" scoped>
  .base-check {
    padding-top: 0px;
    .base-check-row {
      padding-top: 0px;
      padding-bottom: 0px;
      .base-check-col {
        padding-top: 0px;
        padding-bottom: 0px;
      }
    }
  }
</style>
