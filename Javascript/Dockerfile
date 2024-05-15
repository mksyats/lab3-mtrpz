FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY app.js ./

FROM gcr.io/distroless/nodejs22-debian12

WORKDIR /app

COPY --from=builder /app .

CMD ["app.js"]
