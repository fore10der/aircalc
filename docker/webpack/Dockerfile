FROM node:carbon-jessie

WORKDIR /usr/src/app/assets

COPY ./app/assets/package.json ./
COPY ./app/assets/.babelrc ./
COPY ./app/assets/postcss.config.js ./
COPY ./app/assets/webpack.config.js ./
COPY ./app/assets/src ./src

RUN npm install
RUN npm run build