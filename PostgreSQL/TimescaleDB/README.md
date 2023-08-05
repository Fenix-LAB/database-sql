# /home/postgres/pgdata/data
## Documentacion de la imagen de TimescaleDB:
https://docs.timescale.com/self-hosted/latest/install/installation-docker/#install-self-hosted-timescaledb-from-a-pre-built-container

https://hub.docker.com/r/timescale/timescaledb

## Para ejecutar de forma local una imagen de timescaledb
Correr en modo deamon 
```bash
docker run -d --name timescaledb -p 5432:5432 \
-v "$(pwd)":/home/postgres/pgdata/data \
-e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg13
```

## Run Container

```bash
[SDC host]$ docker run -it --name sdc_database -p 5432:5432 \
--network sdc_network_scrap
-v /postgres/pgdata/data:/postgres/pgdata/data \
-e POSTGRES_PASSWORD=password \
--entrypoint /bin/bash \
sdc_database
```

```bash
# levantamos el contenedor de forma local de la base de datos
# se tiene que cambiar la ruta del volumen
[SDC host]$ docker run -d --name sdc_database -p 5432:5432 -v /postgres/pgdata/data:/home/postgres/pgdata/data -e POSTGRES_PASSWORD=password --network sdc_network_scrap timescale/timescaledb:latest-pg13

# ejecutamos solo la terminal
[SDC host]$ docker exec -it <id_container> /bin/sh

# entramos a la tarminal para ejecutar querys
[SDC host]$ psql -U postgres

#comando unico que ejecuta los dos pasos anterirores
[SDC host]$ docker exec -it sdc_database psql -u postgres

# comandos para lanzar una base de datos local
[SDC host]$ create database sdc_scrap_detector;

# mostar las bases de datos
\l

# cambiar a la base de datos a usar
\c {name}
```
Informacion sobre como correr comandos de timescaledb:

```
https://hub.docker.com/_/postgres
```

## DOCKER CONTAINER FOR TIMESCALEDB WITH CONFIG FILE
### This Should initiate the db with the database name

El archivo es guardado de manera local en: 
```
/postgres/pgdata/data
```
## Para construir imagen a partir del Dockerfile:
```
docker build -f backend/timescaledb/Dockerfile -t sdc_timescaledb .

docker run -d --name sdc_timescaledb-$(date '+%Y-%m-%d-%H.%M.%S') --network sdc_network_scrap --hostname tcpuia.sdc_timescaledb.com -p 5432:5432 -e POSTGRES_PASSWORD=password -e PGDATA=/var/lib/postgresql/data/pgdata -v /postgres/pgdata/data:/var/lib/postgresql/data sdc_timescaledb

docker run -it --rm --name sdc_timescaledb-$(date '+%Y-%m-%d-%H.%M.%S') --network sdc_network_scrap --hostname tcpuia.sdc_timescaledb.com -p 5432:5432 -e POSTGRES_PASSWORD=password -e PGDATA=/var/lib/postgresql/data/pgdata -v /postgres/pgdata/data:/var/lib/postgresql/data sdc_timescaledb
```