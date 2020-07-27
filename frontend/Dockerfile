from node:10
RUN mkdir -p /code

# global install & update
RUN npm i -g npm && npm install yarn
RUN yarn cache clean

WORKDIR /code
EXPOSE 3000
CMD ./command.sh


