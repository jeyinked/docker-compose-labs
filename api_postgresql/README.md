# python-postgres-compose

Docker Compose lab running a Python service with a PostgreSQL database.

## Description

This project demonstrates how to:

* Run a PostgreSQL database in Docker
* Use Docker Compose for a multi-service backend stack
* Inject environment variables into containers
* Persist database data with a Docker volume
* Connect services through a shared Docker network
* Use `depends_on` to control startup order

## Architecture

```text
Python API
   ↓
PostgreSQL Database
```

## Project Structure

```text
.
├── compose.yaml
├── README.md
└── api/
    └── app.py
```

## Technologies

* Docker
* Docker Compose
* Python
* PostgreSQL

## Run the Stack

```bash
docker compose up -d
```

## View Logs

```bash
docker compose logs api
docker compose logs db
```

## Concepts Covered

* Multi-service Docker Compose stack
* PostgreSQL container
* Docker volumes
* Environment variables
* Docker networking
* Service discovery
* depends_on

## PostgreSQL Configuration

The PostgreSQL container is configured with:

```yaml
environment:
  - POSTGRES_DB=myapp
  - POSTGRES_USER=admin
  - POSTGRES_PASSWORD=secret
```

## API Configuration

The Python service receives database connection information through environment variables:

```yaml
environment:
  - DB_HOST=db
  - DB_NAME=myapp
  - DB_USER=admin
  - DB_PASSWORD=secret
```

## Persistent Data

PostgreSQL data is stored in a Docker volume:

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

This allows the database data to survive container deletion.

## Stop the Stack

```bash
docker compose down
```

To also remove the volume:

```bash
docker compose down -v
```
