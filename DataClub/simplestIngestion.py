import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("some_data.csv", nrows=10000)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

engine = create_engine("postgresql://postgres:password@localhost:5432/users")
engine.connect()

# this is just used to setup the table schema in sql.
pd.io.sql.get_schema(df, name="taxi_tb", con=engine)

df.to_sql(name="taxi_tb", con=engine, if_exists='replace')


