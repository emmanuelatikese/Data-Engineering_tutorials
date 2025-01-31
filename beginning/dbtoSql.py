import psycopg2 as db
import pandas as pd

conn = db.connect("dbname='users' host='localhost' user='postgres' password='password'")
df = pd.read_sql("select * from userstable", conn)
df.to_json("fromDB.json", orient="records")
df.to_csv("fromDB.csv")



