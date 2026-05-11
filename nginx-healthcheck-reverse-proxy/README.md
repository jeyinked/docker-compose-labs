# nginx-healthcheck-reverse-proxy

Docker Compose lab using Nginx as a reverse proxy in front of a Python API with Docker healthchecks and restart policies.

## Description

This project demonstrates how to:

* Configure an Nginx reverse proxy
* Use Docker healthchecks
* Monitor container health status
* Configure automatic container restart policies
* Connect multiple services through a Docker network
* Use bind mounts for configuration injection

## Architecture

```text
Browser
   ↓
Nginx Reverse Proxy
   ↓
Python API
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

```bash
docker compose up -d
```

## Access

Open in browser:

```text
http://localhost:8084
```

Expected response:

```text
API HEALTHY
```

## Healthcheck

The API container uses a Docker healthcheck:

```yaml
healthcheck:
  test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000')"]
  interval: 30s
  timeout: 10s
  retries: 3
```

Docker periodically checks if the API is responding correctly on port `5000`.

## Restart Policy

The API service uses:

```yaml
restart: unless-stopped
```

This allows Docker to automatically restart the container if it crashes.

## Reverse Proxy

Nginx forwards incoming HTTP requests to the Python API using:

```nginx
proxy_pass http://api:5000;
```

Where `api` is resolved automatically through Docker Compose DNS.

## Verify Container Health

```bash
docker ps
```

Expected status:

```text
healthy
```

## Concepts Covered

* Reverse proxy
* Docker healthchecks
* Restart policies
* Multi-service Compose stack
* Docker networking
* Bind mounts
* Service discovery
* Container supervision
