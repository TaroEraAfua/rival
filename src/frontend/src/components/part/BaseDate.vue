<template>
  <div class="base-date">
    <v-text-field
      background-color="white"
      :label="hints"
      :hide-details="false"
      v-model="label"
      outlined
      readonly
      @click="onForm"
    ></v-text-field>
    <transition name="slide-fade">
      <v-date-picker
        ref="picker"
        @blur="onCancel"
        v-if="dateFlg"
        v-model="date"
        :multiple="checkMultiple"
        no-title
        scrollable
        width="269px"
        style="z-index: 8;"
      >
        <v-spacer />
        <v-btn text color="primary" @click="onCancel">Cancel</v-btn>
        <v-btn text color="primary" @click="onSubmit">OK</v-btn>

      </v-date-picker>
    </transition>
  </div>
</template>

<script>
  import formatData from "../common/formatMixin";
  export default {
    name: 'BaseDate',
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
        type: [Object, Boolean],
        default: function () {
          return {}
        }
      },
    },
    data() {
      return {
        date: null,
        preDate: null,
        dateFlg: false,
        label: '',
      }
    },
    computed: {
      checkMultiple: function () {
        let res = this.checkType();
        if (res) {
          this.date = [];
        } else {
          this.date = null;
        }
        return res
      }
    },
    watch: {
      param: {
        handler: function (to, from) {
          let res = this.checkType();
          if (res && !this.date) {
            this.date = to;
            this.onSubmit();
            this.dateFlg = false;
          } else if (!this.date) {
            this.date = to;
            this.onSubmit();
            this.dateFlg = false;
          }
        },
        immediate: true,
        deep: true
      },
      dateFlg (val) {
        let self = this;
        if ( this.checkTypeOf(this.option) === 'object' ){
          if( this.option['yearFlg'] ) {
            val && setTimeout(function() {
              if (self.$refs.picker) {
                self.$refs.picker.activePicker = 'YEAR'
              }

            })

          }
        }
      },
    },
    methods: {
      checkType: function () {
        return Object.keys(this.option).includes('multiple') ? this.option.multiple : false
      },
      onSubmit: function () {
        if (this.checkType() && this.date) {
          this.label = this.date.join('、');
        } else {
          this.label = this.date;
        }

        this.$emit('changeForm', {key: this.keyName, val: this.date});
        this.dateFlg = !this.dateFlg;
      },
      onCancel: function () {
        this.date = this.preDate;
        this.dateFlg = !this.dateFlg;
      },
      onForm: function () {
        this.preDate = this.date;
        this.dateFlg = !this.dateFlg;
      },
    },
    created() {

    },
    mounted: async function() {
      await this.$nextTick(() => {
        this.removeClassElement('v-text-field__details')
      })
    }
  }
</script>

<style lang='scss' scoped>
  .base-date {
    position: relative;
    /*z-index: 7;*/

    max-height: 43px;
    min-height: 43px;
    ::v-deep .v-text-field--solo, .v-text-field--outlined {
      border-radius: 0;
      height: 1vh;
    }

    ::v-deep .theme--light.v-text-field--outlined fieldset {
      border-color: white;
    }

    ::v-deep .v-text-field--outlined > .v-input__control > .v-input__slot {
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

    ::v-deep .v-text-field > .v-input__control > .v-input__slot > .v-text-field__slot {
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
      flex: 1 1 auto;
      position: relative;
      padding: 8px 0;
    }
    ::v-deep .v-text-field__details{
      padding: 0;
    }

    .slide-fade-enter-active {
      transition: all .3s ease;
    }

    .slide-fade-leave-active {
      transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }

    .slide-fade-enter, .slide-fade-leave-to
      /* .slide-fade-leave-active below version 2.1.8 */
    {
      transform: translateX(10px);
      opacity: 0;
    }
  }
</style>
