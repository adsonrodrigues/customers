FROM ubuntu:18.04

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y curl

RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs -y
RUN npm install -g create-react-app

RUN rm nodesource_setup.sh