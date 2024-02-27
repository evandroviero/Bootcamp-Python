import pandas as pd

df = pd.read_csv('vendas.csv')

def soma_valores(df, columns, agrupador):
    func = {}
    for i in columns:
        func[i] = 'sum'

    return df.groupby(agrupador).agg(func).reset_index()

columns = ['Venda','Quantidade']
agrupador = 'Categoria'
somatorio = soma_valores(df, columns, agrupador)
print(somatorio)