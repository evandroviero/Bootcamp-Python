import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv) -> None:
        self.arquivo = arquivo_csv
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.arquivo)

    def remover_celulas_vazias(self):
        self.df = self.df.dropna()

    def filtrar_por_estado(self, estado):
        self.df = self.df[self.df['estado'] == estado]

    def processar(self, estado):
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)
        return self.df

arquivo_csv = 'exemplo.csv'
df_filtrado = ProcessadorCSV(arquivo_csv).processar('SP')
print(df_filtrado)