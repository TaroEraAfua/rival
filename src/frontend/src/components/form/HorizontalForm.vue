<template>
  <v-container fluid class="horizontal-form">
    <template v-for="(item, key) in formData">

      <v-row class="horizontal-form-row">
        <v-col cols="11">
          <v-row
            style="padding: 0">
            <v-col
              style="padding: 0; margin-left: 2vw;"
              v-if="Object.keys(item).includes('title')"
              :cols="item.col.title" :md="item.md.title"
            >
              <p>
                {{ item.title }}
                <template v-if="Object.keys(item).includes('title')" :cols="1" >
                  <span class="horizontal-require" v-if="item.primary">　- 必須</span>
                </template>
              </p>

            </v-col>
          </v-row>
          <v-row
            style="padding: 0;"
            :style="item.title ? 'margin-left: 5vw;' : '' "
          >
            <v-col
              style="padding: 0"
              :cols="checkColContent(item)"
              :md="checkMdContent(item)"
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
              <base-input-text
                v-if="item.base === 'text'"
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
              <base-radio
                v-if="item.base === 'radio' "
                :hints="item.hints"
                :keyName="key"
                :param="item.param"
                :option="item.option"
                @changeForm="changeForm"
              />
              <base-text-area
                v-if="item.base === 'textArea' "
                :hints="item.hints"
                :keyName="key"
                :param="item.param"
                :option="item.option"
                @changeForm="changeForm"
              />
              <base-check
                v-if="item.base === 'check' "
                :hints="item.hints"
                :keyName="key"
                :param="item.param"
                :option="item.option"
                @changeForm="changeForm"
              />
              <base-input-file
                v-if="item.base === 'icon' "
                :hints="item.hints"
                :keyName="key"
                :param="item.param"
                :option="item.option"
                @changeForm="changeForm"
              />
              <base-output-text
                v-if="item.base === 'output' "
                :hints="item.hints"
                :keyName="key"
                :param="item.param"
                :option="item.option"
                @changeForm="changeForm"
              />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-row v-if=" Object.keys(errMsg).includes(key) && errMsg[key] !== '' ">
        <v-col class="horizontal-form-row-err" style="margin-left: 2vw;">
          {{ errMsg[key] }}
        </v-col>
      </v-row>
    </template>
    <v-row class="horizontal-form-row">
      <v-col cols="11">
        <v-row>
          <slot name="button-area" />
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BaseSelect from "../part/BaseSelect";
import BaseWeek from "../part/BaseWeek";
import BaseMultipleSelect from "../part/BaseMultipleSelect";
import BaseInputText from "../part/BaseInputText";
import BaseDate from "../part/BaseDate";
import BaseRadio from "../part/BaseRadio";
import BaseCheck from "../part/BaseCheck";
import BaseTextArea from "../part/BaseTextArea";
import BaseInputFile from "../part/BaseInputFile";
import BaseOutputText from "../part/BaseOutputText";

export default {
  name: 'HorizontalForm',
  components: {
    BaseSelect, BaseWeek, BaseMultipleSelect, BaseInputText,
    BaseDate, BaseRadio, BaseCheck, BaseTextArea, BaseInputFile,
    BaseOutputText
  },
  props: {
    formData: {
      type: Object,
      default: function () {
        return {}
      }
    },
    errMsg: {
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
    },
    checkColContent(item) {
      return Object.keys(item).includes('col') ? item.col.content : ''
    },
    checkMdContent(item) {
      return Object.keys(item).includes('md') ? item.md.content : ''
    }
  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>
  .horizontal-form {
    padding: 0;
    .horizontal-form-row {
      min-height: 8vh;
      height: auto;
      margin-bottom: 0px;
      p {
        font-size: 20px;
        margin-top: 5px;
        margin-left: 10px;
        padding-left: 10px;
        padding-top: 5px;
        border-left: 6px solid #ffaa1a;
        white-space: pre-line;
      }
      .horizontal-require {
          font-size: 13px;
          border: none;
          color: #686c6d;
      }
    }
    .horizontal-form-row-err {
      padding-top: 0px;
      margin-top: 0px;
      color: red;
      font-size: 10px;
    }
  }

</style>
