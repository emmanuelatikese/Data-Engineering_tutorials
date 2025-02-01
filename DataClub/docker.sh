docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root"\
    -e POSTGRES_DB="taxi_ny" \
    -v docker_db:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
    