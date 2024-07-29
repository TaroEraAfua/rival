<template>
  <div class="base-input-text">
    <v-text-field
      background-color="white"
      :label="hints"
      v-model="textMessage"
      :append-icon="changeFormType"
      :value="param"
      :type="formType"
      outlined
      autocomplete=”off”
      @click:append="formFlg = !formFlg"
    />
  </div>
</template>

<script>
export default {
  name: 'BaseInputText',
  props: {
    keyName: {
      type: String
    },
    param: {
      type: [String, Number, Object],
      default: function () {
        return ''
      }
    },
    hints: {
      type: String
    },
    option: {
      type: Object,
      default: function () {
        return {
          formType: 'text'
        }
      }
    }
  },
  data: function () {
    return {
      textMessage: '',
      formType: 'text',
      formFlg: true
    }
  },
  watch: {
    textMessage: function (to) {
      this.changeForm();
    },
    param: function (to, from) {
      if (to !== this.textMessage) {
        this.textMessage = to
      }
    },
  },
  computed: {
    changeFormType: function() {
      let res = '';
      if (Object.keys(this.option).includes('formType')) {
        switch (this.option.formType) {
          case 'text':
            break;
          case 'password':
            if (this.formFlg) {
              this.formType = 'text';
              res = 'mdi-eye-off';
            } else {
              res = 'mdi-eye';
              this.formType = this.option.formType;
            }
            break;
        }
      }
      return res
    }
  },
  methods: {
    checkType: function () {
      this.formType = this.option.formType;
      this.formFlg = this.option.formType !== 'password';
    },
    changeForm: async function () {
      this.$emit('changeForm', {key: this.keyName, val: this.textMessage} );
    },
    setParam: function () {
      this.textMessage = this.param;
    }
  },
  created () {
    this.checkType();
    this.setParam();
  },
  mounted: async function() {
  }
}
</script>

<style  lang="scss" scoped>
  .base-input-text {
    position: relative;
    z-index: 3;

    max-height: 43px;
    min-height: 43px;
    ::v-deep .v-text-field--solo, .v-text-field--outlined {
      border-radius: 0;
      height: 1vh;
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
