FROM postgres:14.1

ENV POSTGRES_DB="megapay_db"
ENV POSTGRES_USER="api_user"
ENV POSTGRES_PASSWORD="wstdyufvgbhjipnh8yr7o8pi"
ENV PGDATA="/var/lib/postgresql/data/pgdata"

COPY ./init.sql /docker-entrypoint-initdb.d/