FROM alpine

RUN apk add python3

WORKDIR /app

COPY ./Project .

CMD ["python3", "./scripts/server.py"]
