# Base de datos de PostgreSQL

### Documentacion de la imagen de TimescaleDB:

https://hub.docker.com/_/postgres

### Docker run

Correr en modo deamon

```bash
docker run -d \
--name my_base_timescaledb \
-p 5432:5432 \
-e POSTGRES_PASSWORD=password \
timescale/timescaledb:latest-pg13
```

### Entrar en el contenedor 

Modo interactivo 

```bash
docker exec -it <id_container> bash
```

Modo interactivo y comandos SQL

```bash
docker exec -it <id_container> bash
```

### Comandos SQL

Para comenzar a ejecutar querys usamos:

```bash
psql -U postgres
```

Crear bases de datos:

```bash
create database <name>;
```

Mostrar bases de datos:

```bash
\l
```

Cambier base de datos:

```bash
\c <name>
```
