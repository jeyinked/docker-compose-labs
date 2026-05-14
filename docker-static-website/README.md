# docker-static-website

Simple static website hosted with Nginx inside a Docker container.

## Description

This project demonstrates how to:

* Build a custom Docker image
* Serve a static HTML website with Nginx
* Use a custom Nginx configuration
* Expose a containerized web application

## Technologies

* Docker
* Nginx
* HTML/CSS

## Project Structure

```text id="v5k6lp"
.
├── Dockerfile
├── nginx.conf
├── index.html
└── README.md
```

## Dockerfile

The project uses a custom Docker image based on Nginx.

Main concepts:

* Base image
* File copy
* Custom configuration
* Static web hosting

## Build the Image

```bash id="m7xvra"
docker build -t static-website .
```

## Run the Container

```bash id="n3h9wu"
docker run -d -p 8087:80 static-website
```

## Access the Website

Open in browser:

```text id="r8zkds"
http://localhost:8087
```

or:

```text id="k9mbwe"
http://SERVER_IP:8087
```

## Nginx Configuration

The custom Nginx configuration serves the static website on port 80.

Example:

```nginx id="j5hftn"
server {
  listen 80;

  location / {
    root /usr/share/nginx/html;
    index index.html;
  }
}
```

## Concepts Covered

* Docker images
* Docker containers
* Nginx web server
* Static website hosting
* Docker networking
* Port mapping
* Custom container configuration

## Stop the Container

```bash id="t2qvnp"
docker ps
docker stop <container_id>
```

