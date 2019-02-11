FROM node:carbon-jessie

COPY ./app/assets/ /usr/src/app/assets
WORKDIR /usr/src/app/assets

RUN ["npm", "install"]
RUN ["npm", "run", "build"]