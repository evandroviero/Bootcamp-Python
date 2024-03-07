import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    def filtrar_valor(self, valor):
        return self.df.loc[self.df['valor'] >= valor]
    
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

arquivo_csv = 'data/exemplo.csv'
df = CsvProcessor(arquivo_csv)

df_ = df.carregar_csv()
print(df_)

df_ = df.filtrar_valor(5)
print(df_)

