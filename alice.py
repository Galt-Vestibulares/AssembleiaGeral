# %%
import pandas as pd
import seaborn as sns 
import matplotlib as plt
from datetime import datetime 
from datetime import date

# autor: Alice, Iury
# modificações: Pedro Cruz

# %% [markdown]
# ### Alunos ativos

# %%
def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 10000)
    ativos_geral = pd.read_csv(r'ativo_geral.csv')

    # %%
    excluidos_geral = pd.read_csv(r'excluidos_geral.csv')

    # %%
    ativos_geral.info()

    # %%
    # colunas pra mantes
    columns = [1, 3, 5, 6, 9, 14, 17, 19, 20, 21, 22, 31, 32, 33, 34, 35]

    ativos_geral = ativos_geral.iloc[:, columns]
    ativos_passaram = ativos_geral[ativos_geral['curso'].notna()]
    ativos_passaram.head()

    # %%
    ativos_geral.shape

    # %%
    ativos_passaram.shape

    # %% [markdown]
    # 33% dos alunos ativos foram aprovados em ao menos um vestibular

    # %%
    pct_aprovados = round((len(ativos_passaram)/len(ativos_geral))*100,2)
    pct_aprovados

    # %%
    ativos_passaram.info()

    # %%
    ativos_passaram.rename({'Matrícula':'matricula', 'Turma':'turma', 'Nome_completo':'nome', 'Status':'status',
                            'Data de Nascimento':'dt_nascimento', 'Língua Estrangeira': 'l_estrangeira', 
                            'Cidade residente':'cidade', 'Unnamed: 19':'ano_final_em', 
                            'Curso que pretende ingressar na Universidade':'curso_pretendido',
                            'Universidade que pretende ingressar como primeira opção': 'uni_pretendida',
                            'Matérias  que possui maior dificuldade':'materias_dificuldade', 
                            'enem 1° sem':'enem_1', 'PAS 1° sem':'pas_1', 'enem 2° sem':'enem_2', 'PAS 2° sem': 'pas_2',
                            'curso':'curso_passou'}, axis=1, inplace=True)

    # %%
    ativos_passaram

    # %%
    ativos_passaram.query("matricula == 22160")

    # %%
    ativos_passaram.loc[ativos_passaram["matricula"] == 22160, "dt_nascimento"] = '2000-04-22 00:00:00'

    # %%
    ativos_passaram['dt_nascimento'] = pd.to_datetime(ativos_passaram['dt_nascimento'], format='%Y-%m-%d %H:%M:%S', errors='ignore')

    # %%
    # %%
    idades = []
    for i, row in ativos_passaram.iterrows():
        born = row['dt_nascimento'].date()
        today = date.today()
        idades.append(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

    # %%
    ativos_passaram['idade'] = idades

    # %%
    ativos_passaram.info()

    # %%
    ativos_passaram.info()

    # %%
    ativos_passaram['idade'] = ativos_passaram['idade'].fillna(0)

    # %%
    ativos_passaram['idade'] = ativos_passaram['idade'].astype(int)
    return ativos_passaram


