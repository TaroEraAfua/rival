<template>
  <v-container fluid class="base-select">
    <base-pagination
      :count="formatData.count"
      :page="pageNumber"
      @changePage="changePage"
    />
    <template v-for=" rowData in dataList.prof">
      <v-row>
        <v-col class="col-span">
          <base-list-card
            :formatData="formatData"
            :rowData="rowData"
            @onCardBtn="onCardBtn"
            @onCardDetail="onCardDetail"
          />
        </v-col>
      </v-row>
    </template>
    <base-pagination
      :count="formatData.count"
      :page="pageNumber"
      @changePage="changePage"
    />
  </v-container>
</template>

<script>
import BaseListCard from "../part/BaseListCard";
import BasePagination from "../part/BasePagination";
export default {
  name: 'SearchList',
  components: {
    BasePagination, BaseListCard
  },
  props: {
    formatData: {
      type: Object,
      default: function () {
        return {}
      }
    },
    dataList: {
      type: Object,
      default: function () {
        return {
          count: 1,
          prof: []
        }
      }
    },
  },
  data: function() {
    return {
      pageNumber: 1
   }
  },
  computed: {

  },
  watch: {
    pageNumber: function (val) {
      this.onPage(val);
    }
  },
  methods: {
    changePage: function (data) {
      if (this.pageNumber !== data.val) {
        this.pageNumber = data.val;
        this.$emit('changePage', data);
      }
    },
    onCardBtn: function (data) {
      this.$emit('onCardBtn', data);
    },
    onCardDetail: function (data) {
      this.$emit('onCardDetail', data);
    }

  },
  created () {
  }
}
</script>

<style  lang="scss" scoped>


</style>
