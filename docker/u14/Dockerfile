# Ubuntu with basic tools and nginx installation

FROM ubuntu:14.04
MAINTAINER ksraju007@gmail.com

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update ;\
    apt-get -y install vim build-essential screen curl wget \
        software-properties-common tar zip openssh-client git \
        ftp telnet screen nginx-full;
EXPOSE 80
CMD "/bin/bash"
