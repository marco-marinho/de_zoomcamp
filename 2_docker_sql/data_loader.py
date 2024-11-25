import pandas as pd
import typer
from sqlalchemy import create_engine

app = typer.Typer()


@app.command()
def load_data(
    user: str,
    passwd: str,
    host: str,
    port: int,
    db: str,
    parquet_file: str,
    csv_file: str,
):
    # Create a connection to the database
    engine = create_engine(f"postgresql://{user}:{passwd}@{host}:{port}/{db}")

    # Load the data from the parquet file
    df = pd.read_parquet(parquet_file)

    # Write the data to the database
    df.to_sql("yellow_taxi_data", con=engine, if_exists="replace")

    # Load the zone lookup data
    df = pd.read_csv(csv_file)

    # Write the data to the database
    df.to_sql("taxi_zone_lookup", con=engine, if_exists="replace")


if __name__ == "__main__":
    app()
