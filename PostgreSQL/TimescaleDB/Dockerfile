FROM timescale/timescaledb:latest-pg13

ENV POSTGRES_USER postgres
ENV POSTGRES_DB db_scrap_detector

COPY backend/timescaledb/init_db.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

EXPOSE 5432
