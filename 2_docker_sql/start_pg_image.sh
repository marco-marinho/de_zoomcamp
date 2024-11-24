docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network pg-network \
    --name pg-server \
    postgres:13.1-alpine