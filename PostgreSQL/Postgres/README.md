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
-v ${PWD}:/home/postgres/pgdata/data \
timescale/timescaledb:latest-pg13
```

### Entrar en el contenedor 

Modo interactivo 

```bash
docker exec -it <id_container> bash
```

Modo interactivo y comandos SQL

```bash
docker exec -it <id_container> psql -u postgres
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

Listar tablas de una base de datos

```bash
\dt
```

Para obtener informacion de la tabla usamos:

```bash
\d+ "<name>";
```

Mostrar contenido de una tabla:

```bash
SELECT * <"FROM table_name">;
```

Para borrar una tabla se usa:

```bash
DROP TABLE <"table_name">;
```