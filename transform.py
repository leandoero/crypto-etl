import pandas as pd
from extract import get_info

raw_data = get_info()

df = pd.DataFrame(raw_data)
columns_to_keep = [
    'id', 'symbol', 'name', 'current_price',
    'market_cap', 'price_change_percentage_24h',
    'last_updated'
]
df = df[columns_to_keep]
df['last_updated'] = pd.to_datetime(df['last_updated'])

df.to_csv('data.csv')