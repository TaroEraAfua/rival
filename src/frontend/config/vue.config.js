const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
console.log("load vue config");
module.exports = {
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
    const plugins = [];
    plugins.push(
        new UglifyJsPlugin({
          uglifyOptions: {
            compress: {
              drop_console: true,
              drop_debugger: true,
              pure_funcs: ['console.log']
            }
          },
          sourceMap: false,
          parallel: true
        })
      );
      config.plugins = [
        ...config.plugins,
        ...plugins
      ];
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
  productionSourceMap: false,
  transpileDependencies: ['vuetify'],
};
