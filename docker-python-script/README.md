# docker-python-script

Simple Python script running inside a Docker container.

## Description

This project demonstrates how to:

* Build a custom Python Docker image
* Run a Python script inside a container
* Use Docker bind mounts
* Understand container runtime execution

## Technologies

* Docker
* Python

## Project Structure

```text
.
├── Dockerfile
├── script.py
├── requirements.txt
└── README.md
```

## Dockerfile

Example Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "script.py"]
```

## Build the Image

```bash
docker build -t python-script .
```

## Run the Container

```bash
docker run python-script
```

Expected output:

```text
Hello from Python inside Docker
```

## Bind Mount Example

Run the container with a bind mount:

```bash
docker run -v $(pwd)/data:/app/data python-script
```

This maps:

```text
HOST:      ./data
CONTAINER: /app/data
```

## Why Use Bind Mounts?

Bind mounts allow:

* data persistence
* file sharing between host and container
* live development
* logs and generated files storage

## Concepts Covered

* Docker images
* Docker containers
* Python containers
* Dockerfile basics
* WORKDIR
* COPY
* CMD
* Bind mounts
* Runtime configuration

## Difference Between Image and Runtime

Dockerfile:

* builds the image
* defines application structure

docker run:

* launches the container
* configures runtime options such as volumes and ports

## Stop Containers

```bash
docker ps
docker stop <container_id>
```
