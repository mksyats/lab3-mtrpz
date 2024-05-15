FROM alpine

WORKDIR /app

RUN apk add --no-cache nodejs npm

RUN apk add dumb-init

COPY package*.json ./

RUN npm install

COPY app.js ./

ENTRYPOINT ["dumb-init", "--", "npm", "start"]
