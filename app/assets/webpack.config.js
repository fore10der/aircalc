const HtmlWebPackPlugin = require("html-webpack-plugin");
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const fs = require("fs");
const path = require('path')

module.exports = {
    entry: [
        "./src/js/index.js", "./src/scss/styles.scss" 
    ],
    output : {
        filename : 'bundle.js',
        path : path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
        {
            test: /\.(png|jpg)$/,
            loader: 'file-loader'
        },
        {
            test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
            use: [{
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]',
                    outputPath: 'fonts/'
                }
            }]
        },
      {
        test: /\.(sass|scss)$/,
        include: path.resolve(__dirname, "src/scss"),
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {}
          },
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
              url: false
            }
          },
          {
            loader: "postcss-loader",
            options: {
              ident: "postcss",
              sourceMap: true,
              plugins: () => [
                require("cssnano")({
                  preset: [
                    "default",
                    {
                      discardComments: {
                        removeAll: true
                      }
                    }
                  ]
                })
              ]
            }
          },
          {
            loader: "sass-loader",
            options: {
              sourceMap: true
            }
          }
        ]
      },
        {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
            loader: "babel-loader"
            }
        },
        {
            test: /\.html$/,
            use: [
            {
                loader: "html-loader"
            }
            ]
        }
        ]
    },
    devServer: {
        historyApiFallback: true,
        // host: '0.0.0.0',//your ip address
        // port: 8080,
    },
    resolve: {
        extensions: ['.js', '.jsx'],
    },
    plugins: [
        new MiniCssExtractPlugin({
      filename: "./styles.bundle.css"
    }),
    new CopyWebpackPlugin([
      {
        from: "./src/fonts",
        to: "./fonts"
      },
    ]),
        new HtmlWebPackPlugin({
        template: "./src/upload.html",
        filename: "./index.html"
        })
    ]
};
