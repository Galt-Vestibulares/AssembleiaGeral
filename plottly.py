import plotly.express as px
import pandas as pd
import streamlit as st


def tira(x):
    index = x.index("-")
    x = " ".join(x.split())
    return x[index+1:]


st.title("aprovações 2023 dos alunos de 2022")
df = pd.read_excel("conciso_aprovados.xlsx")
df["curso"] = df["curso"].apply(tira)
lista = pd.read_excel("conciso_aprovados.xlsx", "Planilha2")
lista["curso"] = lista["curso"].apply(tira)
lista = lista.drop_duplicates()
lista = lista.sort_values(by=["alunos aprovados"], ascending=False)
df = df.drop(columns=["curso"])
print(lista.head(10))
st.plotly_chart(px.parallel_categories(df))
st.title("lista de aprovados")
st.write(lista)

