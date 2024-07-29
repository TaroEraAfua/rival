<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialogFlg"
      persistent
      :max-width=" checkOption('width') "
      :scrollable="true"
    >
      <v-card>
        <v-card-title class="headline">{{ checkTitle }}</v-card-title>
        <v-divider />
        <v-card-text
          :style=" checkOption('height') "
        >
          <common-info
            :formData="infoData"
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <template
            v-for="(item) in btnKeyList"
          >
            <v-btn :color="dialogContent.btn[item].color" text @click="onSubmit(item)">
              {{ dialogContent.btn[item].label }}
            </v-btn>
          </template>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  import {mapActions, mapState} from 'vuex';
  import CommonInfo from "./CommonInfo";
  export default {
    name: 'ViewDialog',
    components: { CommonInfo },
    props: {
      dialogKey: {
        type: String,
        default: function () {
          return ''
        }
      },
      btnKeyList: {
        type: Array,
        default: function () {
          return []
        }
      },
      dialogFlg: {
        type: Boolean,
        default: function () {
          return false
        }
      },
      infoData: {
        type: Object,
        default: function () {
          return {}
        }
      },
      options: {
        type: Object,
        default: function () {
          return {
            width: '40',
            height: '40'
          }
        }
      }
    },
    computed: {
      ...mapState('constant', ['dialogContent']),
      checkOption: function () {
        return function (key) {
          let result = '';
          if (this.options && Object.keys(this.options).includes(key)) {
            switch (key) {
              case 'height':
                result = String(this.options[key]) + 'vh';
                break;
              case 'width':
                result = String(this.options[key]) + 'vw';
                break;
            }
          } else {

          }

          return result
        }
      },
      checkTitle: function () {
        if (this.dialogKey) {
          return this.dialogContent[this.dialogKey].title
        } else {
          return ''
        }
      },
      checkContent: function () {
        if (this.dialogKey) {
          return this.dialogContent[this.dialogKey].content
        } else {
          return ''
        }
      }
    },
    methods: {
      onSubmit: function (key) {
        this.$emit('onSubmit', { dialog:this.dialogKey , btn: key} );
      }
    }
  }

</script>
