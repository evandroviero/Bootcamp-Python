import pandas as pd

class ETLProcess:
    def __init__(self, fonte_dados) -> None:
        self.font_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError('Método extrair_dados deve ser implentado nas classes filhas')
    
class ETLCSV(ETLProcess):
    def __init__(self, fonte_dados) -> None:
        super().__init__(fonte_dados)
   
    def extrair_dados(self):
        return pd.read_csv(self.font_dados)


if __name__ == '__main__':
    