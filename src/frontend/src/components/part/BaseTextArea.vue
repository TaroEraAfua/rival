<template>
  <div class="base-text-area">
    <v-textarea
      solo
      :label="hints"
      :value="param"
      v-model="textMessage"
      @blur="changeForm"
      name="input-7-4"
    />

  </div>
</template>

<script>
import { mapGetters, mapState,mapActions } from 'vuex'
export default {
  name: 'BaseTextArea',

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
          icon: null,
          formType: 'text'
        }
      }
    }
  },
  data: function () {
    return {
      textMessage: ''
    }
  },
  watch: {
    param: function (to, from) {
      if (to !== this.textMessage) {
        this.textMessage = to
        this.changeForm();
      }
    }
  },
  computed: {

  },
  methods: {
    changeForm: async function () {
      this.$emit('changeForm', {key: this.keyName, val: this.textMessage} );
    }
  },
  created () {
    if ('pass' in this.option) {
      this.formType = this.option.pass;
    }
  }
}
</script>

<style  lang="scss" scoped>
  .base-input-text {
    position: relative;
    z-index: 3;
    ::v-deep .v-text-field--solo {
      border-radius: 0;
      height: auto;
    }
    ::v-deep .theme--light.v-text-field--outlined fieldset {
      border-color: white;
    }
    ::v-deep .v-text-field--outlined>.v-input__control>.v-input__slot {
      -webkit-box-align: stretch;
      -ms-flex-align: stretch;
      align-items: stretch;
      max-height: 43px;
      min-height: 43px;
    }
    ::v-deep .v-text-field.v-text-field--outlined .v-input__control {
      max-height: 43px;
      min-height: 43px;
    }

    ::v-deep .v-text-field>.v-input__control>.v-input__slot>.v-text-field__slot {
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
      flex: 1 1 auto;
      position: relative;
      padding: 8px 0;
    }
    ::v-deep .v-text-field.v-text-field--enclosed .v-input__append-inner {
      margin-top: 10px;
    }
  }

</style>
