<template>
  <v-container fluid class="base-file-input">
    <v-row>
      <v-col cols="12" class="base-file-input_area">
        <v-file-input
          background-color="white"
          chips
          clearable
          outlined
          accept="image/*"
          label="画像を選択してください"
          @change="onFileChange"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-img
          :src="checkImage"
          max-height="200"
          min-height="200"
          max-width="200"
          min-width="200"
        />
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  name: 'BaseInputFile',
  props: {
    keyName: {
      type: String
    },
    param: {
      type: [String, Object, Boolean],
      default: function () {
        return ''
      }
    },
    hints: {
      type: String
    },
    option: {
      type: Object,
      default: function () {
        return {
          icon: null,
          formType: 'text'
        }
      }
    }
  },
  data: function() {
    return {
      noImage: require('../common/images/no-image.jpg'),
      resultImageData: '',
      resultImageName: ''
    }
  },
  watch: {
    resultImageData: function (to) {
      this.$emit('changeForm', {
        key: this.keyName,
        val: {
          image_name: this.resultImageName,
          image_data: to
        }
      });
      console.log(to);
    }
  },
  computed: {
    checkImage: function () {
      return this.resultImageData ? this.resultImageData : this.noImage
    },
    imageData: {
      get() {
        return this.resultImageData
      },
      set(val) {
        this.$set(this, 'resultImageData', val);
      }
    }
  },
  methods: {
    onFileChange: async function (e) {
      if (e) {
        await this.createImage(e);

      } else {
        this.$set(this, 'resultImageData', '');
        this.$set(this, 'resultImageName', '');
        this.$emit('changeForm', {
          key: this.keyName,
          val: {
            image_name: '',
            image_data: ''
          }
        });
      }


    },
    createImage: function (file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = async function(e) {
        await vm.formatImage(e.target.result);
      };
      reader.readAsDataURL(file);
      this.resultImageName = file.name;

    },
    formatImage: function (file) {
      let Jimp = require("jimp");
      let tmp = this;
      Jimp.read(file, function (err, image) {
        const width = 200;
        const height = 200;
        image
          .cover(width, height)
          .getBase64(image['_originalMime'], function (err, src) {
            tmp.imageData = src;
          });
      });
    }
  },
  created () {

  }
}
</script>

<style  lang="scss" scoped>
  .base-file-input {
    padding: 0;
    .base-file-input_area{
      min-height: 8vh;
      height: auto;
      position: relative;
      z-index: 3;
      ::v-deep .v-text-field--solo, .v-text-field--outlined {
        border-radius: 0;
        height: 1vh;
      }
      ::v-deep .theme--light.v-text-field--outlined fieldset {
        border-color: white;
      }
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

      ::v-deep .v-text-field>.v-input__control>.v-input__slot>.v-text-field__slot {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-flex: 1;
        -ms-flex: 1 1 auto;
        flex: 1 1 auto;
        position: relative;
        padding: 8px 0;
      }
      ::v-deep .v-text-field.v-text-field--enclosed .v-input__append-inner {
        margin-top: 10px;
      }
    }
  }

</style>
