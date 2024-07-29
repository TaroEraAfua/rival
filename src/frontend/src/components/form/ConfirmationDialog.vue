<template>
  <v-row justify="center">
    <v-dialog v-model="dialogFlg" persistent :max-width="options.width">
      <v-card>
        <v-card-title class="headline">{{ checkTitle }}</v-card-title>
        <v-divider />
        <v-card-text>
          {{ checkContent }}
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
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
  export default {
    name: 'ConfirmationDialog',
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
      options: {
        type: Object,
        default: function () {
          return {
            width: '290'
          }
        }
      }
    },
    computed: {
      ...mapState('constant', ['dialogContent']),
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
        this.$emit('onBtn', { dialog:this.dialogKey , btn: key} );
      }
    }
  }

</script>
