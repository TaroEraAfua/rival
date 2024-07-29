<template>
  <div class="base-select">
    <v-select
      outlined
      background-color="white"
      return-object
      multiple
      v-model="items"
      :label="hints"
      :value="param"
      :items="option.item"
      :item-text="option.label"
      :item-value="option.val"
      @change="changeForm"
    >
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="index === 0">
          <span>{{ item.label }}</span>
        </v-chip>
        <span
          v-if="index === 1"
          class="grey--text caption"
        >(+{{ items.length - 1 }} others)</span>
      </template>
    </v-select>
  </div>
</template>

<script>


export default {
  name: 'BaseSelect',
  props: {
    keyName: {
      type: String
    },
    param: {
      type: [Array]
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
      items: []
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
          if (!this.items.includes(to[idx])) {
            this.items = to;
            break;
          }
        }
      }
    }
  },
  methods: {
    changeForm: function () {
      let r = {key: this.keyName, val: this.items };
      this.$emit('changeForm', r);
    },
    checkMultiple: function () {
      return this.baseType === 'multiple'
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
  .base-select {
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
