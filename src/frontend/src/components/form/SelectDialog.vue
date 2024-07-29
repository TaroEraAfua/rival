<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialogFlg"
      persistent
      :max-width=" checkOption('width') "
      :scrollable="true"
    >
      <v-card>
        <v-card-title class="headline">{{ title }}</v-card-title>
        <v-divider />
        <v-card-text v-if="rowData && Object.keys(rowData).includes('content')">
          <v-container>
            <template v-for="(item, key) in rowData.content">
              <v-row>
                <v-col cols="2">{{ item.title }}</v-col>
                <v-col>{{ item.content }}</v-col>
              </v-row>
            </template>
          </v-container>
        </v-card-text>
        <v-card-text :style=" checkOption('height') ">
          <template
            v-for="(item, key) in btnKeyList"
          >
            <v-card-actions>
              <v-btn block tile :color="checkBtnColor(key)" dark
                     @click="onSubmit(key)">
                {{ item }}
              </v-btn>
            </v-card-actions>
          </template>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    name: 'SelectDialog',
    props: {
      title: {
        type: String,
        default: function () {
          return ''
        }
      },
      dialogFlg: {
        type: Boolean,
        default: function () {
          return false
        }
      },
      rowData: {
        type: Object,
        default: function () {
          return {
            data: {},
            content: {},
          }
        }
      },
      btnKeyList: {
        type: Object,
        default: function () {
          return {
          }
        }
      },
      options: {
        type: Object,
        default: function () {
          return {
            width: '70',
            height: '40'
          }
        }
      }
    },
    computed: {
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
            return result
          }
        }
      }
    },
    methods: {
      checkBtnColor: function (key) {
        switch (key) {
          case 'close':
            return 'gray'
          default:
            return 'indigo'
        }
      },
      onSubmit: function (key) {
        this.$emit('onSubmit', { key: key, data: this.rowData.target } );
      }
    }
  }

</script>
