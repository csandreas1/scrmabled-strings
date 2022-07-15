FROM python:3

WORKDIR /app/code

COPY . .

CMD [ "python3"]