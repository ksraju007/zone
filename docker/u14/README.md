# Ubuntu 14 Dockerfile
This Dockerfile will help to build a pretty basic ubuntu 14 docker image
that contains basic tools as listed in the Dockerfile RUN section.
Idea is to have a image that is capable of doing basic developement tasks
and host a web service if needed for demo/testing purposes.

## Docker Installation

In your machine, install docker first. Read here: https://docs.docker.com/installation/#installation

## Download this repo

```sh
git clone https://github.com/ksraju007/zone.git 
```
## Build the docker image

```sh
cd zone/docker/u14 ;
docker build -t u14 .
```

This will take a few minutes depending on your internet connection, it downloads approximately 400 MB.

See the image exists by running *docker images* command .

## First run

```sh
docker run -name u14 -ti u14 /bin/bash
````

As you can see, it gives you a clean container which is ready to go. When you exit from the bash shell, the container terminates.

## Advanced options

If you want to serve content from the container , you need to tell docker to do that when you start container ( -p 80:80 ).
It also supports mapping a local filesystem folder as a mounted volume inside. ( -v /local/folder:/container/folder )

```sh
docker run -name u14 -ti -p 80:80 -v /path/to/repo/zone/site:/usr/share/nginx/html u14 /bin/bash
service nginx start
service nginx status
```

Use another -p 81:80 , if you have some other thing listening on port 80 on the host already.

The content should be available at http://localhost/  or http://localhost:81 (whatever you chose above).

Now the changes you make inside files in site folder is immediately visible on the web browser.
Once you are happy with changes you did , you can terminate the container and commit changes into repo. 

## Cleaning up

Cleanup old containers using *docker rm* command. Run *docker ps -a* to find out containers. Then use the image IDs to delete.

```sh
docker stop <image ID>
docker rm <image ID> 
```

If you have a lot of containers , You could also do something like :

```sh
for i in `docker ps -a -q` ; do docker stop $i ; docker rm $i ; done
```

## Other notes

