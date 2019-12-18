## Using Docker


#### 1. Run an image with `$ docker run <image-name>`
* The image creates a container from the image and assigns a random name.
* if a container from an image exists previously, use `docker start --attach <container-name>` to restart the container.<br>
  * The `--attach` tells Docker to connect to the container output so we can see the results.

* to create container with an assigned name, use `docker run --name <the-name>

#### 2. Viewing
* To list running containers: `docker ps`
* To view all containers: `docker ps -a`
* To view images on the system: `docker image ls`

#### 3. Stop Containers: `docker stop <container name>`
*  Remove containers: `docker rm <container name>`

#### 4. Create a Docker image
* Write dockerfile and then use: `docker build -t <tag name> .`
  * `-t <tag name>` gives Docker a tag for the image 
  * The dot (or ".") told Docker to look for the Docker file in the current working directory. 


#### Run a custom image
`$ docker run --name foo -d -p 8080:80 mynginx`<br>

From the above,<br>
– `--name foo` gives the container a name, rather than one of the randomly assigned names we’ve seen so far.<br>
- `-d` detaches from the container, running it in the background, as we did in our previous run of Nginx.<br>
- `-p` 8080:80 maps network ports, as we did with the first example.
Finally, the image name is always last.


The below will allow you to run a web-server and override the server name<br>

`
docker run --name webapp -p 8080:4000 -e NAME="Dude"  mypyweb
`

