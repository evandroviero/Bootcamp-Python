from abc import ABC, abstractclassmethod

class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def start(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractclassmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractclassmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")