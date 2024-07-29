<template>
  <div class="base-input-text" style="margin-top: 10px">
    <span >{{ param }}</span>
  </div>
</template>

<script>
  export default {
    name: "BaseOutputText",
    props: {
      keyName: {
        type: String
      },
      param: {
        type: [String, Number, Object],
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
            formType: 'text'
          }
        }
      }
    },
  }
</script>

<style scoped>

</style>