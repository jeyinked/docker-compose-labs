# nginx-python-reverse-proxy

Multi-container application using Nginx as a reverse proxy in front of a Python API with Docker Compose.

## Description

This project demonstrates how to:

* Configure an Nginx reverse proxy
* Connect multiple containers through a shared Docker network
* Use Docker Compose for multi-service orchestration
* Use Docker DNS between containers
* Inject environment variables into containers
* Mount custom configuration files with bind mounts

## Architecture

```text id="n82xpk"
Browser
   ↓
Nginx Reverse Proxy
   ↓
Python API
```

## Project Structure

```text id="t91mva"
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

```bash id="v82mza"
docker compose up -d
```

## Access

Open in browser:

```text id="u62xqp"
http://localhost:8083
```

Expected response:

```text id="l82vmp"
API Python OK - APP_ENV=dev
```

## Concepts Covered

* Reverse proxy
* Docker networking
* Docker DNS
* Multi-service applications
* Bind mounts
* Environment variables
* depends_on
* Container communication

## Reverse Proxy

Nginx forwards incoming requests to the Python API using:

```nginx id="o73mqa"
proxy_pass http://api:5000;
```

Where `api` is the Docker Compose service name automatically resolved by Docker DNS.

## Notes

The Python API receives environment variables from Docker Compose:

```yaml id="r81xpw"
environment:
  - APP_ENV=dev
```

The custom Nginx configuration is mounted using a bind mount:

```yaml id="y73mvn"
volumes:
  - ./nginx.conf:/etc/nginx/conf.d/default.conf
```

