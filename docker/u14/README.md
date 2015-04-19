# Ubuntu 14 Dockerfile
This Dockerfile will help to build a pretty basic ubuntu 14 docker image
that contains basic tools as listed in the Dockerfile RUN section.
Idea is to have a image that is capable of doing basic developement tasks
and host a web service if needed for demo/testing purposes.

## Docker Installation

In your machine, install docker first. Read here: https://docs.docker.com/installation/#installation

## Download this repo

git clone https://github.com/ksraju007/zone.git 

## Build the docker image
cd zone/docker/u14 ;
docker build -t u14 .

This will take a few minutes depending on your internet connection, it downloads approximately 400 MB.

See the image exists by running 'docker images' command .

## First run

docker run -name u14 -ti u14 /bin/bash

As you can see, it gives you a clean container which is ready to go. When you exit from the bash shell, the container terminates.

## Advanced options

If you want to serve content from the container , you need to tell docker to do that when you start container ( -p 80:80 ).
It also supports mapping a local filesystem folder as a mounted volume inside. ( -v /local/folder:/container/folder )

docker run -name u14 -ti -P 80:80 -v zone/site:/var/www u14 /bin/bash
Then inside the container , start nginx by running 'service nginx start'

The content should be available at http://localhost/ .

## Cleaning up

Cleanup old containers using 'docker rm' command. Run 'docker ps -a' to find out containers. Then use the image IDs to delete.

docker stop <image ID>
docker rm <image ID> 

If you have a lot of containers , You could also do something like :

for i in `docker ps -a -q` ; do docker stop $i ; docker rm $i ; done

## Other notes

