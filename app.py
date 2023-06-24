import plotly.express as px
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib as plt
import alice
# autor Pedro Cruz
# email: pedrofcrux@gmail.com


def tira(x):
    index = x.index("-")
    x = " ".join(x.split())
    return x[index+1:]

def get_frequencias(ativos_passaram):
    """
    autor: Iury
    """
    words_array = ativos_passaram['materias_dificuldade'].values

    materias_dificeis_passaram = []

    for words_str in words_array:
        words = words_str.split(', ')
        for word in words:        
            materias_dificeis_passaram.append(word)
    
    frequencia = {}
    for materia in materias_dificeis_passaram:
        if materia in frequencia:
            frequencia[materia] += 1
        else:
            frequencia[materia] = 1

    df = pd.DataFrame({'Disciplina': list(frequencia.keys()), 'Quantidade': list(frequencia.values())})
    return df
    

st.title("aprovações 2023 dos alunos de 2022")
df = pd.read_excel("conciso_aprovados.xlsx")
df["curso"] = df["curso"].apply(tira)
lista = pd.read_excel("conciso_aprovados.xlsx", "Planilha2")
lista["curso"] = lista["curso"].apply(tira)
lista = lista.drop_duplicates()
lista = lista.sort_values(by=["alunos aprovados"], ascending=False)
df = df.drop(columns=["curso"])
print(lista.head(10))
st.plotly_chart(px.parallel_categories(df).update_layout(
autosize=True))
st.title("lista de aprovados")
st.write(lista)

ativos_passaram = alice.main()
dif = get_frequencias(ativos_passaram)
dif_f = px.bar(dif, x="Disciplina", y="Quantidade")
st.title("dificuldade das matérias dos aprovados")
st.plotly_chart(dif_f)



ativos_passaram = ativos_passaram[ativos_passaram.idade !=0]
fig = px.histogram(ativos_passaram, x="idade")

st.title("idade dos alunos")
st.plotly_chart(fig)

