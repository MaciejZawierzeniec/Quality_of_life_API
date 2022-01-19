import pandas as pd
from sqlalchemy import create_engine

with open('./quality_of_life_extended.csv', 'r') as file:
    df = pd.read_csv(file)

df.columns = [c.lower() for c in df.columns]
engine = create_engine("postgresql://postgres:postgres@db:5432/postgres")
df.to_sql('cities', con=engine, index=False, if_exists='replace')
