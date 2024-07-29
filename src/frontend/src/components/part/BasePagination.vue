<template>
  <div class="text-center">
    <v-pagination
      v-model="pageNumber"
      :length="count"
      total-visible="7"
      circle
    />
  </div>
</template>

<script>
export default {
  name: 'BasePagination',
  props: {
    count: {
      type: [Number, String],
      default: function () {
        return 1
      }
    },
    page: {
      type: [Number, String],
      default: function () {
        return 1
      }
    }
  },
  data: function() {
    return {
      pageNumber: 1
    }
  },
  computed: {
  },
  watch: {
    page: {
      handler: function (to, from) {
        if (to !== this.pageNumber) {
          this.pageNumber = to;
        }
      },
      deep: true
    },
    pageNumber: function (to, from) {
      if (to !== from) {
        this.$emit('changePage', {key: 'page', val: to});
      }
    }
  },
  methods: {

  },
  created () {

  }
}
</script>

<style  lang="scss" scoped>
  .base-card {

  }

</style>
