import pandas as pd

class MyDataQuality:
    def __init__(self, data):
        self.data = data  

    def get_value(self, key):
        """Retorna o valor associado à chave, se existir."""
        return self.data.get(key, None)

    def get_nulos(self, base):
        
    def get_unicos(self, base):

    def get_valores_categoricas(self, base):

    def get_descricao(self, base):

    def get_graf_categoricas(self, base):

    def get_graf_numericas(self, base):    