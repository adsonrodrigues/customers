FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV LIBEV_FLAGS=4

RUN apt update -y
RUN apt upgrade -y

RUN apt-get update --fix-missing

RUN apt-get install -y python3 python3-pip python3-dev python3-virtualenv python3-setuptools libpq-dev gdal-bin

RUN pip3 install --upgrade pip

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV TERM screen
