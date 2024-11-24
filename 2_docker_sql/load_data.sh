docker build -t data_ingest:0.1.0 .
docker run -it \
    --network pg-network \
    data_ingest:0.1.0
echo "Data loaded into the database"