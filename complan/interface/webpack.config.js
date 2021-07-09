var HTMLWebpackPlugin = require('html-webpack-plugin')
var path = require('path')


module.exports = {
  entry: {
    main: './src/link.js',
},
  
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  
  module: {
    rules: [
      {
        test: /\.html$/,
        use: 'html-loader'
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use:  "babel-loader" 
      },
      {
        test: /\.css$/,
        use: [ "style-loader", "css-loader" ]
      },
      {
        test: /\.(jpg|png|svg|jpeg|gif)$/,
        loader: 'url-loader'
      }, 
      {
        test: /\.(eot|ttf|woff|woff2)$/,
        loader: 'url-loader',
        options: {
          limit: 10000
        }
     }
    ]

  },
  plugins: [
     new HTMLWebpackPlugin({
      filename: 'index.html',
      template: './templates/interface/index.html',
      chunks: ['index']
    }),
  ]
};
