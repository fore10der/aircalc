FROM node:carbon-jessie



COPY ./app/assets/ /usr/src/app/assets
WORKDIR /usr/src/app/assets

COPY ./docker/webpack/entrypoint.sh /usr/src/app/entrypoint.sh

RUN ["npm", "install"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
RUN ["npm", "run", "build"]