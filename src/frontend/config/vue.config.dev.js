console.log("load vue config dev");
module.exports = {
  parallel: 3,
  devServer: {
    parallel: false,
    host: '0.0.0.0',
    port: '8080',
    watchOptions: {
      poll: true
    },
    disableHostCheck: false
  },
  chainWebpack: config => {
    config.module.rule('vue').uses.delete('cache-loader');
    config.module.rule('js').uses.delete('cache-loader');
    config.module.rule('scss').uses.delete('cache-loader');
    config.module.rule('vue').uses.delete('babel-loader');
    config.module.rule('js').uses.delete('babel-loader');
    config.module.rule('scss').uses.delete('babel-loader');
    config.module.rule('vue').uses.delete('vuetify-loader');
    config.module.rule('js').uses.delete('vuetify-loader');
    config.module.rule('scss').uses.delete('vuetify-loader');
  },
  configureWebpack: {
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.runtime.esm.js',
      }
    },
    cache: true,
    optimization: {
      splitChunks: {
        minSize: 10000,
        maxSize: 200000,
      }
    },
  },
  productionSourceMap:  true,
  transpileDependencies: ['vuetify'],
};
