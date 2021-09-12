# FROM golang:alpine

# # Required because go requires gcc to build
# RUN apk add build-base

# RUN apk add inotify-tools

# COPY . /debug_env

# WORKDIR /debug_env

# RUN go mod download

# RUN go get github.com/go-delve/delve/cmd/dlv

# CMD sh /debug_env/run.sh

FROM golang:1.17-bullseye


RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y inotify-tools 

RUN pip3 install lark-parser --upgrade 


COPY . /debug_env

WORKDIR /debug_env

RUN go mod download

RUN go get -d github.com/go-delve/delve/cmd/dlv
RUN go install github.com/go-delve/delve/cmd/dlv

CMD sh /debug_env/run.sh