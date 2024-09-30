import streamlit as st
import pandas as pd
from data_quality import MyDataQuality
def app():

        st.title('Análise de Qualidade de Dados')
        df = pd.read_csv('exercise_angles.csv')

        # Crie uma instância de MyDataQuality
        dq = MyDataQuality({})

        # Mostrar os dados
        st.subheader('Dados Carregados')
        st.write(df.head())

        # Obtenha informações sobre valores nulos
        st.subheader('Valores Nulos por Coluna')
        nulos = dq.get_nulos(df)
        st.bar_chart(nulos)

        # Obtenha informações sobre valores únicos
        st.subheader('Valores Únicos por Coluna')
        unicos = dq.get_unicos(df)
        st.bar_chart(unicos)

        # Obtenha descrições das colunas
        st.subheader('Descrição das Colunas Numéricas')
        desc_num, desc_cat = dq.get_descricoes(df)
        st.write(desc_num)

        st.subheader('Descrição das Colunas Categóricas')
        st.write(desc_cat)

        # Gráficos para colunas categóricas
        st.subheader('Distribuição de Colunas Categóricas')
        dq.get_graf_categoricas(df)

        # Gráficos para colunas numéricas
        st.subheader('Distribuição de Colunas Numéricas')
        dq.get_graf_numericas(df)

        # Gráfico de valores nulos
        st.subheader('Mapa de Calor de Valores Nulos')
        dq.get_graf_nulos(df)

        # Gerar relatório ydata-profiling
        if st.button('Gerar Relatório ydata-profiling'):
            dq.generate_ydata_profile(df)