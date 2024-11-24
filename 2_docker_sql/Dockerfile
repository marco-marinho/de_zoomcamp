FROM python:3.12-slim
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install wget -y && \
    pip install --upgrade pip 

WORKDIR /app
RUN wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet -O data.parquet
COPY requirements.txt requirements.txt
COPY data_loader.py data_loader.py
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "data_loader.py", "root", "root", "pg-server", "5432", "ny_taxi", "data.parquet" ]