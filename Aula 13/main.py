from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI(debug=True)
fake = Faker()

file_name = 'data/products.csv'
df = pd.read_csv(file_name)
df['indice'] = range(1, len(df) + 1)
df.set_index('indice', inplace=True)

loja = 11

@app.get('/')
async def hello_world():
    return 'Hello World'

@app.get('/gerar_compra')
async def gerar_compra():
    index = random.randint(1, len(df) - 1)
    tuple = df.iloc[index]
    return 