const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
console.log("load vue config pro");
process.env.NODE_ENV = "production";
console.log(process.env.NODE_ENV);
console.log(process.env.VUE_APP_API_URL);
console.log(process.env.VUE_APP_API_VERSION);
console.log(process.env.VUE_APP_DEBUG);
module.exports = {
  lintOnSave: false,
  runtimeCompiler: true,
  productionSourceMap: false,
  transpileDependencies: ['my-module'],
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules\/(?!(dom7|swiper)\/).*/,
          use: [
            {
              loader: "babel-loader",
              options: {
                presets: [["@babel/preset-env", { modules: false }]]
              }
            }
          ]
        }
      ]
    },
    optimization: {
      minimizer: [
        new UglifyJsPlugin({
          uglifyOptions: {
            compress: {
              drop_console: true
            },
          }
        })
      ]
    }
  }
};