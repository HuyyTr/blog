FROM python:3.8.10-alpine
RUN pip install --upgrade pip

RUN apk update \
    && apk add --no-cache gcc python3-dev musl-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app

WORKDIR /app