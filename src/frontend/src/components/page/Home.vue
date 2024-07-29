<template>
 <v-container fluid
              :class=" checkTerminal ? 'page-home' : 'page-home-mobile' "
              :style="{ 'background-image': 'url(' + backImage + ')' }"
 >
   <v-row
     class="main-row"
     >

     <v-col v-if="checkTerminal" xs='12' md="6" class="right-form mx-auto" >
       <v-row align="center" justify="center">

       </v-row>
     </v-col>
     <v-col xs='12' md="6" class="left-form mx-auto">
       <v-row align="center">
         <v-col cols="10" class="mx-auto">
           現在テスト運用中です。<br />
           ご自由に使用してください。<br />
         </v-col>
       </v-row>
       <v-row align="center">
         <v-col cols="10" class="mx-auto">
           <v-row>
             <horizontal-form
               :form-data="options"
               @changeForm="changeForm"
             >
               <template slot="button-area">
                 <v-col cols="12" style="padding: 0;">
                   <v-btn block tile color="indigo" dark
                          style="position: relative; z-index: 1;"
                          @click="onSearch"
                   >チームを探す</v-btn>
                 </v-col>
               </template>
             </horizontal-form>
           </v-row>
         </v-col>
       </v-row>
     </v-col>
   </v-row>
 </v-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import rivalHeader from '../common/Header.vue'
import formatMixin from "../common/formatMixin";
import ActionMixin from "../common/ActionMixin";
import HorizontalForm from "../form/HorizontalForm";
import auth from "../../vuex/module/auth";
export default {
  name: 'top',
  mixins: [formatMixin,ActionMixin],
  components: {
    HorizontalForm, rivalHeader
  },
  props: {
    checkTerminal: {
      type: Boolean,
      default: function () {
        return true
      }
    }
  },
  data() {
    return {
      backImage: require('../common/images/back.jpg'),
      leftImage: require('../common/images/our_image_jpeg.jpg'),
      formType: {line: 'ver', xs: 11, md: 10 },
      options: {
        prefecture: {
          baseType: '',
          base: 'select',
          hints: '都道府県',
          param: '',
          api: null,
          option: {}
        },
        city: {
          baseType: '',
          base: 'select',
          hints: '地域',
          param: '',
          api: null,
          option: {}
        },
        station: {
          baseType: '',
          base: 'select',
          hints: '最寄駅',
          param: '',
          api: null,
          option: {}
        },
        purpose: {
          base: 'multiple',
          hints: '目的',
          param: [],
          api: null,
          option: {}
        },
        date: {
          base: 'date',
          hints: '活動日',
          param: [],
          api: null,
          option: {multiple: true}
        }
      }
    }
  },
  watch: {
    authFlg: {
      handler: function (to, from) {
        this.setSelectOption();
      },
      deep: true
    },
  },
  computed:{
    ...mapState('auth',['authFlg', 'userList', 'joinTeamList']),
    ...mapState('area', [
      'prefecture', 'city', 'station'
    ]),
    ...mapState('common', [
      'purpose'
    ]),
  },
  methods: {
    ...mapActions('area', [
      'getPrefecture', 'setAriaApiParam',
      'getCity', 'getStation'
    ]),
    ...mapActions('common', [
      'getConData'
    ]),
    ...mapActions('team', ['getDetailTeamList', 'setSearchDetailParam']),
    setSelectOption: async function () {
      await this.sendCreatApi();
      this.makeOptionData('options');
    },
    sendCreatApi: async function () {
      await this.getPrefecture();
    },
    onSearch: async function () {
      let res = await this.makeApiData(this.options);
      await this.setSearchDetailParam(res);
      if (Object.keys(this.userList).length > 0) {
        await this.setSearchDetailParam(
          {
            user: {
              key: 'user',
              val: this.userList.user_id
            },
            team: {
              key: 'team',
              val: this.joinTeamList.select
            }
          });
      }
      await this.getDetailTeamList();
      this.movePage('/search');
    }
  },
  created () {
    this.setSelectOption();
  }
}
</script>

<style lang="scss" scoped>
.page-home {
  min-height: 80vh;
  position: relative;
  z-index: 2;
  height: auto;
  padding: 0;
  margin: 0;
  background-attachment: fixed;
  .main-row {
    background: no-repeat center;
    height: 80vh;
    margin: 0;
  }
  .right-form {
    .right-form-image {
      border-radius: 320px / 200px;
      border: 2px solid #1892f6;
    }

  }
  .left-form {

  }
}
.page-home-mobile {
  min-height: 150vh;
  height: auto;
  width: 100vw;
  padding: 0;
  margin: 0;
  background-attachment: fixed;
  .main-row {
    background: no-repeat center;
    height: 80vh;
    width: 100vw;
    margin: 0;
  }
  .right-form {
    .right-form-image {
      border-radius: 320px / 200px;
      border: 2px solid #1892f6;
    }

  }
  .left-form {

  }
}
</style>
