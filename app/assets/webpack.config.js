const HtmlWebPackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const CleanWebpackPlugin = require('clean-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const fs = require("fs");
const path = require('path');


module.exports = {
    entry: [
        "./src/js/index.js", "./src/scss/styles.scss" 
    ],
    output : {
        filename : '[name].[hash].js',
        path : path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
        {
            test: /\.(png|jpg)$/,
            loader: 'file-loader',
            options: {
              outputPath: '/'
          }
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
      new CleanWebpackPlugin(['dist']),
        new MiniCssExtractPlugin({
      filename: "./[name].[hash].css"
    }),
    new BundleTracker({filename: './dist/webpack-stats.json'}),
    new CopyWebpackPlugin([
      {
        from: "./src/fonts",
        to: "./fonts"
      },
    ]),
    new CopyWebpackPlugin([
      {
        from: "./src/img",
        to: "./"
      },
    ]),
        new HtmlWebPackPlugin({
            template: "./src/report1.html",
        filename: "./index.html"
        })
    ]
};
