FROM golang:1.22.3-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -ldflags '-extldflags "-static"' -o build/fizzbuzz

FROM gcr.io/distroless/static-debian11

COPY --from=builder /app/build/fizzbuzz .

COPY --from=builder /app/templates ./templates

CMD ["./fizzbuzz", "serve"]
