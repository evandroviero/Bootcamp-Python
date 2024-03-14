import pandas as pd

def carregar_csv_e_filtrar(arquivo_csv, estado):
    df = pd.read_csv(arquivo_csv)

    df = df.dropna()

    df_filtrado = df[df['estado'] == estado]
    return df_filtrado

arquivo_csv = 'exemplo.csv'
estado_filtrado = 'SP'

df_filtrado = carregar_csv_e_filtrar(arquivo_csv, estado_filtrado)
print(df_filtrado)