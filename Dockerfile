FROM alpine

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir fastapi==0.79.0 uvicorn==0.18.2

EXPOSE 8000

COPY ./src /app

CMD uvicorn app.api:app --host 0.0.0.0