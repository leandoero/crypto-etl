import psycopg2
import pandas as pd
from sqlalchemy import create_engine

pf = pd.read_csv("data.csv")
engine = create_engine("postgresql+psycopg2://postgres:7535@localhost:5432/postgres")
conn = psycopg2.connect(dbname="postgres", user="postgres", password="7535", host="localhost", port="5432")

cursor = conn.cursor()
conn.autocommit = True

cursor.execute("""
    CREATE TABLE IF NOT EXISTS coins (
    id TEXT PRIMARY KEY,
    symbol TEXT,
    name TEXT,
    current_price FLOAT,
    market_cap BIGINT,
    price_change_percentage_24h FLOAT,
    last_updated TIMESTAMP
);   
""")

pf.to_sql('coins', engine, if_exists='replace', index=False)

cursor.close()

conn.close()