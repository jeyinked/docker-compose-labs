# docker-compose-scaling-lab

Docker Compose lab demonstrating API scaling and simple load balancing with Nginx.

## Description

This project demonstrates how to:

* Scale Docker Compose services
* Run multiple API replicas
* Configure Nginx as a reverse proxy
* Use Docker service discovery
* Understand horizontal scaling concepts
* Distribute traffic across multiple containers

## Architecture

```text
Client
   ↓
Nginx Reverse Proxy
   ↓
Multiple Python API Containers
```

## Project Structure

```text
.
├── compose.yaml
├── nginx.conf
├── README.md
└── api/
    └── app.py
```

## Technologies

* Docker
* Docker Compose
* Nginx
* Python

## Run the Stack

Start the stack with 5 API replicas:

```bash
docker compose up -d --scale api=5
```

## Verify Containers

```bash
docker ps
```

Expected result:

```text
proxy_container
scaling-api-1
scaling-api-2
scaling-api-3
scaling-api-4
scaling-api-5
```

## Access

Open in browser:

```text
http://localhost:8085
```

Refresh the page multiple times.

You should see different API container hostnames.

Example:

```text
Hello from API container: scaling-api-3
```

## Nginx Reverse Proxy

Nginx forwards requests to the API service using:

```nginx
proxy_pass http://api:5000;
```

Docker Compose DNS automatically resolves `api` to multiple containers.

## Scaling

The following command creates multiple replicas of the API service:

```bash
docker compose up -d --scale api=5
```

This demonstrates horizontal scaling with Docker Compose.

## Concepts Covered

* Horizontal scaling
* Reverse proxy
* Docker service discovery
* Multi-container architecture
* Docker networking
* Load distribution
* API replicas
* Container orchestration basics

## Important Note

The `api` service intentionally does not use `container_name`.

This allows Docker Compose to automatically generate unique container names when scaling replicas.

## Stop the Stack

```bash
docker compose down
```

