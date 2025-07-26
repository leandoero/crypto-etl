import pandas as pd
from sqlalchemy import create_engine, Table, Column, Text, Float, BigInteger, DateTime, MetaData

# Чтение данных
try:
    pf = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Файл data.csv не найден!")
    exit(1)

# Создание подключения через SQLAlchemy
engine = create_engine("postgresql+psycopg2://postgres:7535@localhost:5432/postgres")

# Определение структуры таблицы
metadata = MetaData()
coins = Table('coins', metadata,
              Column('id', Text, primary_key=True),
              Column('symbol', Text),
              Column('name', Text),
              Column('current_price', Float),
              Column('market_cap', BigInteger),
              Column('price_change_percentage_24h', Float),
              Column('last_updated', DateTime))

# Создание таблицы
metadata.create_all(engine)

# Запись данных в таблицу
pf.to_sql('coins', engine, if_exists='replace', index=False)

# Освобождение ресурсов
engine.dispose()