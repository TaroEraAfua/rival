<template>
  <div class="base-radio">
    <v-radio-group
      :value="param"
      row
    >
      <template v-for="(item, key) in option">
        <v-radio
          :label="item.label"
          :value="item.val"
          @change="changeForm(item)"
        />
      </template>
    </v-radio-group>
  </div>
</template>

<script>


export default {
  name: 'BaseRadio',
  props: {

    keyName: {
      type: String
    },
    param: {
      type: [String, Number, Object, Array, Boolean],
      default: function () {
        return null
      }
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

    }
  },
  components: {

  },
  computed: {

  },
  watch: {
    param: function (to, from) {
      if ( to !== from ) {
        this.changeForm({label: '',val: to});
      }
    }
  },
  methods: {
    changeForm: function (param) {
      let r = {key: this.keyName, val: param.val, param: param};
      this.$emit('changeForm', r);
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
  .base-radio {
    ::v-deep .theme--light.v-text-field--outlined fieldset {
      border-color: white;
    }
    ::v-deep .v-menu__content {
      position: absolute;
      display: inline-block;
      border-radius: 0;
      max-width: 80%;
      overflow-y: auto;
      overflow-x: hidden;
      contain: content;
      will-change: transform;
      -webkit-box-shadow: 0 5px 5px -3px rgba(0,0,0,.2), 0 8px 10px 1px rgba(0,0,0,.14), 0 3px 14px 2px rgba(0,0,0,.12);
      box-shadow: 0 5px 5px -3px rgba(0,0,0,.2), 0 8px 10px 1px rgba(0,0,0,.14), 0 3px 14px 2px rgba(0,0,0,.12);
    }
    // outline
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
    ::v-deep .v-icon.v-icon {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      display: -webkit-inline-box;
      display: -ms-inline-flexbox;
      display: inline-flex;
      -webkit-font-feature-settings: "liga";
      font-feature-settings: "liga";
      font-size: 24px;
      -webkit-box-pack: center;
      -ms-flex-pack: center;
      justify-content: center;
      letter-spacing: normal;
      line-height: 1;
      text-indent: 0;
      -webkit-transition: .3s cubic-bezier(.25,.8,.5,1);
      transition: .3s cubic-bezier(.25,.8,.5,1);
      vertical-align: middle;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      // 追加
      margin-bottom: 1vh;
    }
    //solo
    /*::v-deep .v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)>.v-input__control>.v-input__slot {
      -webkit-box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
      box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
      height: 5vh;
    }
    ::v-deep .v-text-field.v-text-field--solo .v-input__control {
      min-height: 5vh;
    }*/
    ::v-deep .v-text-field--solo, .v-text-field--outlined {
      border-radius: 0;
    }
  }

</style>
