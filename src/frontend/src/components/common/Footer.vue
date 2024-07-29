<template>
  <v-card
    class="rival-footer"
  >
    <v-footer
      padless
    >
      <v-card
        flat
        tile
        class="flex rival-footer-body text-center brown lighten-4"
      >
        <v-card-text>
          <v-btn
            href="mailto:rival.matching@gmail.com"
            icon
          >
            <v-img
              :src="mail_icon"
              max-height="20"
              min-height="20"
              max-width="20"
              min-width="20"
            />お問い合わせはこちらまで
          </v-btn>
        </v-card-text>
        <v-card-text>
          <v-btn
            icon
            class="twitter white--text"
            href="https://twitter.com/share?text=バスケのためのサイト「Rival」おすすめ！%0a&url=https://rival-basketball.jp/com_top=バスケットボール,バスケ,"
            onClick="window.open(encodeURI(decodeURI(this.href)), 'tweetwindow', 'width=650, height=470, personalbar=0, toolbar=0, scrollbars=1, sizable=1'); return false;"
            rel="nofollow"
          ><i class="fab fa-twitter"></i>
          </v-btn>
          <v-btn
            icon
            class="facebook white--text"
            href="https://www.facebook.com/sharer/sharer.php?text=バスケのためのサイト「Rival」おすすめ！%0a&url=https://rival-basketball.jp/com_top=バスケットボール,バスケ,"
          >
            <i class="fab fa-facebook-f"></i>
          </v-btn>
          <v-btn
            icon
            href="https://social-plugins.line.me/lineit/share?url=https%3a%2f%2frival%2dbasketball%2ejp%2f"
          >
            <v-img

              :src="line_icon"
              max-height="30"
              min-height="30"
              max-width="30"
              min-width="30"
            />
          </v-btn>
        </v-card-text>
        <v-card-text>
          Copyright 2020 - Rival All Right Reserved
        </v-card-text>
      </v-card>
    </v-footer>
  </v-card>
</template>

<script>
  export default {
    data() {
      return {
        mail_icon: require('./images/mail.png'),
        line_icon: require('./images/LINE_SOCIAL_Circle.png')
      }
    },
    methods: {},
    created() {

    }
  }

</script>

<style lang="scss">
  .rival-footer {
    padding: 0;
    .rival-footer-body {
      width: 100vw;
      .twitter{
        width: 30px;
        height: 30px;
        background: #7dcdf7;
      }
      .facebook {
        width: 30px;
        height: 30px;
        background: #7c9dec;
      }
    }
  }
</style>
