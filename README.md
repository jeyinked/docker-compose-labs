# Docker Compose Labs

A collection of hands-on Docker and Docker Compose labs focused on container networking, reverse proxying, custom images, and multi-service architectures.

## Projects

### nginx-custom-image

Custom Nginx image built with Dockerfile and deployed with Docker Compose.

Concepts covered:

* Dockerfile
* Custom image build
* Docker Compose build
* Bind mounts vs COPY
* Custom bridge network

---

### nginx-python-reverse-proxy

Nginx reverse proxy forwarding requests to a Python API running in another container.

Concepts covered:

* Reverse proxy
* Docker DNS
* Multi-service Compose stack
* Shared Docker networks
* Environment variables
* Bind mounts
* depends_on

## Requirements

* Docker
* Docker Compose

## Clone the Repository

```bash id="r83mxa"
git clone https://github.com/jeyinked/docker-compose-labs.git
```

## Run a Project

Example:

```bash id="u72xqp"
cd docker-compose-labs/nginx-python-reverse-proxy
docker compose up -d
```

## Goal

This repository is used as a practical playground to learn:

* Docker
* Docker Compose
* Container networking
* Reverse proxying
* Multi-container applications
* Infrastructure as Code (IaC)
