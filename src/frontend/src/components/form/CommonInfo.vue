<template>
  <v-container fluid class="common-info">
    <v-card>
      <v-row>
        <v-col cols="8">
          <v-card-title>{{ formData.title }}</v-card-title>
        </v-col>
        <v-col>
          <slot name="info-title-button-area"/>
        </v-col>
      </v-row>
      <v-divider />
      <v-row class="common-info-body">
        <v-col cols="12" md="12">
        <v-container>
          <v-row>
            <template v-for="(param, key) in formData.format">
              <v-col
                v-if="param['type'] !== 'week'"
                class="none-padding "
                style="margin-top: 1vh; margin-bottom: 1vh;"
                :cols="param.col.label"
                :md="param.md.label"
              >
                <p v-if="param['type'] === 'img'"
                   class="subtitle-2"
                   style="margin-left: 1vw; padding-top: 1vh; margin-bottom: 0; margin-top: 0; height: 50px;"
                >{{ param.label }}
                </p>
                <p v-else
                   class="subtitle-2" style="margin-left: 1vw; padding: inherit"

                >{{ param.label }}
                </p>
                <v-divider style="margin-left: 1vw" v-if="param['type'] !== 'week' "/>
              </v-col>
              <v-col
                class="none-padding"
                style="margin-top: 1vh; margin-bottom: 1vh;"
                :cols="param.col.data"
                :md="param.md.data"
                v-if="param['type'] !== 'week'"
              >
                <v-img
                  :id="key"
                  v-if="param['type'] === 'img'"
                  :src="formData.list[key]" max-height="50" max-width="50"
                />
                <p
                  v-else-if="param['type'] === 'text'"
                  :id="key"
                  style="padding: inherit"
                  class="subtitle-2"
                >
                  {{ viewData(formData, key) }} {{ param.unit }}
                </p>
                <v-divider style="margin-right: 1vw;" v-if="param['type'] !== 'week' "/>
              </v-col>
            </template>
          </v-row>
          <template
            v-if="Object.keys(formData.format).includes('week')"
            >
            <v-row>
              <v-col
                class="none-padding "
                style="margin-top: 1vh; margin-bottom: 1vh;"
                :cols="formData.format['week'].col.label"
                :md="formData.format['week'].md.label"
              >
                <p
                   class="subtitle-2" style="margin-left: 1vw; padding: inherit"
                >{{ checkWeekData }}
                </p>
              </v-col>
              <v-col
                class="none-padding"
                style="margin-top: 1vh; margin-bottom: 1vh;"
                :cols="formData.format['week'].col.data "
                :md="formData.format['week'].md.data "
              >
                <base-week
                  id="week"
                  :param="formData.list['week']"
                  :option="formData.format['week'].option"
                />
              </v-col>
            </v-row>
          </template>
          <v-row/>
          <v-row>
            <v-row/>
            <v-row class="text-center" style="margin-top: 3vh; margin-bottom: 1vh; margin-left: 1vw;">
              <slot name="info-button-area"/>
            </v-row>
          </v-row>
        </v-container>
        </v-col>
      </v-row>
    </v-card>

  </v-container>
</template>

<script>
import BaseWeek from "../part/BaseWeek";
import formatMixin from "../common/formatMixin";
export default {
  name: 'CommonInfo',
  mixins: [formatMixin],
  props: {
    formType: {
      type: Object,
      default: function () {
        // line: ver => 横、hor => 縦
        return {line: 'ver', xs: 11, md: 10}
      }
    },
    formFormat: {
      type: Object,
      default: function () {
        return {}
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
  components: {
    BaseWeek
  },
  computed: {
    checkWeekData: function () {
      return Object.keys(this.formData.format).includes('week') ? this.formData.format['week'].label : ''


    },
    viewData: function () {
      return function (formData, key) {
        let result = null;
        if (key === "week") {
          result = formData.list[key];
        } else if ( this.checkTypeOf(formData.list[key]) === 'object') {
          result = formData.list[key].val;
        } else {
          result = formData.list[key];

        }
        return result
      }
    }
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
  .common-info {
    height: fit-content;
  }


</style>
