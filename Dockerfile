FROM python:3.12.0-bookworm

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python generate_text.py 
