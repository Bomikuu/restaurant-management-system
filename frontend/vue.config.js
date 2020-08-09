module.exports = {
  runtimeCompiler: true,
  devServer: {
    compress: true,
    disableHostCheck: true,
  },
  transpileDependencies: ["vuetify"],
  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false,
    },
  }
};
