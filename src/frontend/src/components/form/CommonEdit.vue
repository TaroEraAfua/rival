<template>
  <v-container fluid class="base-select">
    <v-row>
      <v-col
        :xs="formData.xs"
        :md="formData.md"
      >
        <template v-for="(param, key) in formData">
          {{ key }} - {{ param }}
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BaseSelect from "../part/BaseSelect";

export default {
  name: 'CommonForm',
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
  component: {
    BaseSelect
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

  },
  methods: {
    changeForm: function (val) {
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
  .base-select {
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
