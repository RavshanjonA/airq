FROM python:3.12

WORKDIR /app
COPY . .

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt