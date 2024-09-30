import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype, is_categorical_dtype
from ydata_profiling import ProfileReport

class MyDataQuality:
    def __init__(self, data):
        self.data = data  

    def get_value(self, key):
        """Retorna o valor associado à chave, se existir."""
        return self.data.get(key, None)

    def get_nulos(self, df):
        nulos = df.isnull().sum()
        return nulos
        
    def get_unicos(self, df):
        unicos = df.nunique()
        self.data['Unicos'] = unicos
        return unicos

    def get_descricoes(self, df):
        df_aux_num = pd.DataFrame()  
        df_aux_cat = pd.DataFrame()
        for coluna in df.columns:
            if is_numeric_dtype(df[coluna]):
                df_aux_num[coluna] = df[coluna].describe()
            elif is_categorical_dtype(df[coluna]) or df[coluna].dtype == object:
                df_aux_cat[coluna] = df[coluna].describe()
        self.data['Descrição de Colunas Numéricas'] = df_aux_num
        self.data['Quantidade de Valores em Colunas Categóricas'] = df_aux_cat
        return df_aux_num, df_aux_cat

    def get_graf_categoricas(self, df):
        """Gera gráficos de barras para colunas categóricas."""
        for coluna in df.columns:
            if is_categorical_dtype(df[coluna]) or df[coluna].dtype == object:
                plt.figure(figsize=(8, 6))
                sns.countplot(data=df, y=coluna, palette='viridis')
                plt.title(f'Contagem de valores na coluna {coluna}')
                plt.show()

    def get_graf_numericas(self, df):
        """Gera histogramas para colunas numéricas."""
        for coluna in df.columns:
            if is_numeric_dtype(df[coluna]):
                plt.figure(figsize=(8, 6))
                sns.histplot(df[coluna], kde=True, color='blue')
                plt.title(f'Distribuição da coluna {coluna}')
                plt.show()
    
    def get_graf_nulos(self, df):
        """Gera um gráfico de barras mostrando a quantidade de valores nulos por coluna."""
        nulos = df.isnull().sum()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=nulos.index, y=nulos.values, palette='rocket')
        plt.title('Quantidade de Valores Nulos por Coluna')
        plt.xticks(rotation=90)
        plt.show()

    def generate_ydata_profile(self, df):
        """Gera um relatório completo de qualidade de dados usando ydata-profiling."""
        profile = ProfileReport(df, title="Relatório de Qualidade de Dados", explorative=True)
        profile.to_notebook_iframe()  
        profile.to_file("data_quality_report.html")  
    