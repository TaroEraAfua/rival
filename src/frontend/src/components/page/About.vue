<template>
    <v-container fluid class="rival-top-1">

      <v-card class='overflow-hidden' no-body>
        <v-row no-gutters>
          <v-col md='12'>
            <v-img :src="image_top_head" class="card-img"/>
          </v-col>
        </v-row>
      </v-card>

      <div class="coming-content-body">
        <div>
          <h4>こんなこと思ったことありませんか？</h4>
          <v-col md='12'>
            <v-img :src="image_checkbox" class="card-img image-checkbox"/>
          </v-col>
          <h5>チームを運営している方へ。</h5>
          <p class="p-indent-ss">
            チームの強化に！たまには、趣向を変えて・・・<br>
            「どこかのチームと練習試合したい！」<br>
            と思った時、対戦相手を見つけるのって意外と大変ですよね。
          </p>
          <p>
            他にも、新しいメンバーを募集しよう！と思った時。<br>
            掲示板に募集要項を書いたり、友達を当たってみたり・・・<br>
            意外とめんどくさいですよね。
          </p>
          <h5>チームを探している方へ。</h5>
          <p>
            ちょっとバスケがしたいなー。 <br>
            と思って、いざ、チームを探そう！！ <br>
            と思った時。<br>
            意外と自分のニーズ（場所、時間、曜日）にあったチームを探すのって大変じゃないですか？
          </p>

          <p>でも、大丈夫！ライバルを使えばそんな不安すぐに解決出来ちゃいます！</p>
        </div>
        <div>
          <h4>私たちのサービス</h4>
          <h5>主なサービス</h5>
          <v-col md='12'>
            <v-img :src="image_our_service" class="card-img image-our-service"/>
          </v-col>
          <h5>最大の特徴！！</h5>
          <p>
            私たちのサービスの最大の特徴。<br>
            それは、なんといっても
          </p>
          <h6>
            自分、自分たちに合ったチームと一発でマッチングできること。
          </h6>

          <p>
            そのために場所、時間、曜日といった基本的な検索機能はもちろん！<br>
            チームの雰囲気やレベル、目的も一発で検索できちゃいます♪
          </p>

          <p class="center-service">
            「毎週、練習しているようなガチなチームと戦いたいなー。」<br>
            「まったりと活動しているチームとゆるーく交流試合したいなー。」<br>
            「バスケやったことないけど、初心者でも練習参加歓迎してくれるチームはないかな？」
          </p>
          <p>
            そんな貴方の思いに一発で応えることができちゃいます！
          </p>

          <p>
            試合申し込みを受け付けるか、メンバーの募集を受け付けるかも、
            ワンクリックで簡単管理♪
          </p>
          <p>
            さらに、メッセージはサイト内で完結！メールアドレスなど個人情報をネットに上げることも、<br>
            相手に知らせる必要もありません。
          </p>

          <p>
            試合日や、練習日が決まったらそれをスケジュール管理することもできちゃいます♪
          </p>
        </div>
        <div>
          <h4>今後はもっと！より素敵なものへ！</h4>
          <h5>「たったこれだけ・・・？」と思ったあなた！</h5>

          <p>全ては、お見せできないですが、今後どんどん！素敵な機能！サービスを展開して行きます！</p>

          <ul>
            <li>チームチャット機能</li>
            <li>出欠管理機能</li>
            <li>スコア管理機能</li>
            <li>No1は誰だ!? WEB天下一武道会!!</li>
          </ul>
        </div>
        <div>
          <h4>私たちの思い</h4>
          <v-col md='12'>
            <v-img :src="image_our_image" class="card-img image_our_image"/>
          </v-col>

          <h5>「バスケを通して多くの人がワクワクするような世界を作る。」</h5>

          <p>
            そんな世の中にしたいと本気で私たちは思い、少人数でこのサービスの開発を進めています。
          </p>

          <p>
            より多くのチーム。より多くの人達が私たちのサービスを通して、バスケを楽しんだり、試合を楽しんでくれれば、皆様の日常の中にちょっとしたワクワクを。ちょっとエキサイティングな日々を提供てきると信じています。
          </p>
        </div>
        <div>
          <h4>ぜひ、登録してみてください！</h4>
          <h5>「なんだこのサービス！？なんだか面白そう！！」</h5>

          <p>
            そう思ってくださったら、ぜひ、事前登録してみてください！
            興味がありそうな、お知り合いがいたらぜひ勧めてみてください！
          </p>
          <p class="p-indent-top-ss">私たちと一緒に日本のスポーツを盛り上げて行きませんか？</p>
          <!--
          <a href="/com_user">
            <b-card-img :src="image_click_here" class="card-img image_click_here"/>
          </a>-->
        </div>
      </div>

    </v-container>
</template>

<script>
  export default {
    name: 'top',
    components: {
    },
    data() {
      return {
        slide: 0,
        sliding: null,
        image_src: require('../common/images/sample.png'),
        image_about: require('../common/images/logo.png'),
        image_search: require('../common/images/search.png'),
        image_sing: require('../common/images/people.png'),
        image_top_head: require('../common/images/header_jpeg.jpg'),
        image_checkbox: require('../common/images/discontent_jpeg.jpg'),
        image_our_service: require('../common/images/our_service_jpeg.jpg'),
        image_our_image: require('../common/images/our_image_jpeg.jpg'),
        image_click_here: require('../common/images/click_here.png'),
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      },
      transPage(page) {
        this.currentPage = page;
      },
      ontab(path) {
        this.$router.push(path);
      },
    }
  }
</script>


<style lang="scss" scoped>
    .rival-top-1 {
      padding: 0;
      height: 70%;
      font-family: YuGothic;
      color: #454546;
      .card-img {
        padding: 0;
      }
    }

    .center {
      text-align: center;
    }

    .coming-content-body {
      background: #ebf1f4;
      padding: 10px 20% 10px 20%;

      h4 {
        border-left: 6px solid #ca2330;
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        background-color: #ebf1f4;
        z-index: 2;
      }

      h5 {
        color: #e83f1a;
      }

      h6 {
        text-decoration: underline;
        color: #ca2330;
        font-size: 20px;
      }

      .center-service {
        text-align: center;
        color: #fd7a68;
      }

      .p-indent-ss {
        margin-bottom: 2%;
      }

      .p-indent-top-ss {
        margin-top: 3%;
      }

      .image-checkbox {
        width: 100%;
        margin: 0 auto;
      }

      .image-our-service {
        width: 100%;
        margin: 0 auto;
      }

      .image_our_image {
        width: 100%;
        margin: 0 auto;
      }

      .image_click_here {
        width: 50%;
        margin: 0 auto;
      }

      .service-in {
        text-decoration: underline;
        display: inline;
        color: #e83f1a;
        font-size: 20px;
      }

      .service-in-mini {
        display: inline;
      }

    }

    @media only screen and (max-width: 979px) {
      .coming-content-body {
        padding: 10px 5% 10px 5%;

        .image-checkbox {
          width: 100%;
        }

        .image-our-service {
          width: 100%;
        }

        .image_our_image {
          width: 100%;
        }

        .image_click_here {
          width: 100%;
        }

      }
    }

</style>
