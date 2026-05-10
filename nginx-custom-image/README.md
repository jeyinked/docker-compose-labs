# nginx-custom-image

Custom Nginx image built with Dockerfile and deployed with Docker Compose.

## Description

This project demonstrates how to:

* Build a custom Nginx image
* Use Docker Compose with `build`
* Replace the default Nginx web content
* Deploy a custom containerized web server
* Use a custom bridge network

## Project Structure

```text id="s7kd21"
.
├── compose.yaml
├── Dockerfile
├── index.html
└── README.md
```

## Technologies

* Docker
* Docker Compose
* Nginx

## Build and Run

```bash id="f82mx1"
docker compose up -d
```

## Access

Open in browser:

```text id="k29xpw"
http://localhost:8081
```

## Concepts Covered

* Dockerfile
* Docker image build
* Docker Compose `build`
* Custom container image
* Port mapping
* Bridge networking
* COPY instruction
* Difference between bind mounts and image-based content

## Notes

The website files are copied directly into the image using:

```Dockerfile id="q91zpa"
COPY index.html /usr/share/nginx/html/
```

This means changes to `index.html` require rebuilding the image:

```bash id="t62mvn"
docker compose up -d --build
```

