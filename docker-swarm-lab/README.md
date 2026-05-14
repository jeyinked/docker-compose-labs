# docker-swarm-lab

Introduction to Docker Swarm orchestration with replicated services and scaling.

## Description

This project demonstrates:

* Docker Swarm initialization
* Service orchestration
* Replicated containers
* Horizontal scaling
* Docker services management
* Basic container orchestration concepts

## Technologies

* Docker
* Docker Swarm
* Python

## Project Structure

```text
.
├── Dockerfile
├── app.py
└── README.md
```

## Python Application

The application is a simple Python HTTP server returning the container hostname.

Example response:

```text
Hello from Swarm container: hostname
```

## Dockerfile

The project uses a custom Docker image based on Python.

Build the image:

```bash
docker build -t swarm-lab .
```

## Initialize Docker Swarm

Initialize the Swarm manager node:

```bash
docker swarm init --advertise-addr 192.168.1.3
```

## Create a Swarm Service

Create a service with 3 replicas:

```bash
docker service create \
  --name swarm-api \
  --replicas 3 \
  -p 8086:5000 \
  swarm-lab
```

## Verify Services

List Swarm services:

```bash
docker service ls
```

View service replicas/tasks:

```bash
docker service ps swarm-api
```

List running containers:

```bash
docker ps
```

## Scaling the Service

Increase replicas dynamically:

```bash
docker service scale swarm-api=5
```

Docker Swarm automatically creates additional replicas without stopping existing containers.

## Access

Open in browser:

```text
http://localhost:8086
```

Refresh multiple times to see different container hostnames.

## Concepts Covered

* Container orchestration
* Docker Swarm
* Replicated services
* Horizontal scaling
* Service management
* Desired state
* Load distribution
* Multi-container architecture

## Difference Between Compose and Swarm

Docker Compose:

* Multi-container local environments
* Development-oriented
* Basic scaling

Docker Swarm:

* Real orchestration
* Desired state management
* Automatic replica management
* Scaling and service orchestration
* Multi-node capable

## Remove the Service

```bash
docker service rm swarm-api
```

## Leave Swarm

```bash
docker swarm leave --force
```
