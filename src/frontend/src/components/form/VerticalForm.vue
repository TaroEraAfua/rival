<template>
  <v-container class="vertical-formm">
    <v-row>
      <template v-for="(item, key) in formData">
        <v-col
          class="col-span"
          cols="6"
          md="4"
          style="max-height: 45px; min-height: 45px;"
        >
          <base-select
            v-if="item.base === 'select' "
            :hints="item.hints"
            :keyName="key"
            :param="item.param"
            :option="item.option"
            @changeForm="changeForm"
          />
          <base-week
            v-if="item.base === 'week' "
            :keyName="key"
            :hints="item.hints"
            :param="item.param"
            :option="item.option"
            @changeForm="changeForm"
          />
          <base-multiple-select
            v-if="item.base === 'multiple' "
            :hints="item.hints"
            :keyName="key"
            :param="item.param"
            :option="item.option"
            @changeForm="changeForm"
          />
          <base-date
            v-if="item.base === 'date' "
            :hints="item.hints"
            :keyName="key"
            :param="item.param"
            :option="item.option"
            @changeForm="changeForm"
          />
        </v-col>
      </template>
    </v-row>
    <v-row>
      <slot name="bottun-area"></slot>
    </v-row>
  </v-container>
</template>

<script>
  import BaseSelect from "../part/BaseSelect";
  import BaseWeek from "../part/BaseWeek";
  import BaseMultipleSelect from "../part/BaseMultipleSelect";
  import BaseDate from "../part/BaseDate";
export default {
  name: 'VerticalForm',
  components: {
    BaseSelect, BaseWeek, BaseMultipleSelect,BaseDate
  },
  props: {
    formType: {
      type: Object,
      default: function () {
        // line: ver => 横、hor => 縦
        return {line: 'ver', xs: 11, md: 10}
      }
    },
    formData: {
      type: Object,
      default: function () {
        return {}
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
    changeForm: function (val) {
      this.$emit('changeForm', val);
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
  .vertical-formm {

    ::v-deep .v-text-field--solo, .v-text-field--outlined {
      border-radius: 0;
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
    ::v-deep .v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)>.v-input__control>.v-input__slot {
      -webkit-box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
      box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
      height: 5vh;
    }
    ::v-deep .v-text-field.v-text-field--solo .v-input__control {
      min-height: 5vh;
    }
  }

</style>
