# Ubuntu with basic tools and nginx installation
# 
# Build this image :
# docker build -t u14 .
#
# After the build, run docker images command to see the image with tag u14.
#
# Recommeded start command
#
# docker run -name u14 -ti <image> /bin/bash
#
# Advanced usage . To map a folder from localsystem and open port 80
# docker run -name u14 -ti -P 80:80 -v /git/site:/var/www <image> /bin/bash
#

FROM ubuntu:14.04
MAINTAINER ksraju007@gmail.com

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update ;\
    apt-get -y install vim build-essential screen curl wget \
        software-properties-common tar zip openssh-client git \
        ftp telnet screen nginx-full;
EXPOSE 80
CMD "/bin/bash"
