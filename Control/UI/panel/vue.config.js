const { defineConfig } = require('@vue/cli-service')
const NodePolyfillPlugin = require('node-polyfill-webpack-plugin')


module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  publicPath:'./',
  configureWebpack: {
    plugins: [new NodePolyfillPlugin()],
  },
  devServer: {
    // Paths
    proxy: { // 配置跨域
      '/api':{
          target:`http://192.168.1.88:1024/api`, //请求后台接口
          changeOrigin:true, // 允许跨域
          pathRewrite:{
              '^/api' : '' // 重写请求
          }
      }
    }
  }
})
