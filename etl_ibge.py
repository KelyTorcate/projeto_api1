import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_dataframe(url, colunas, novos_nomes):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data[1:])  # ignora cabeçalho
        df = df[colunas]
        df.columns = novos_nomes

        # Tratar valores inválidos
        df['populacao'] = df['populacao'].replace('-', pd.NA)
        df['populacao'] = pd.to_numeric(df['populacao'], errors='coerce', downcast='integer')
        df['ano'] = pd.to_numeric(df['ano'], errors='coerce', downcast='integer')

        # Remover linhas com população nula
        df = df.dropna(subset=['populacao'])

        return df
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

# ----------------- URLS -----------------
url_sexo = "https://apisidra.ibge.gov.br/values/t/200/p/2000-2010/v/93/c2/4,5/c1/1,2/n3/all"
url_raca = "https://apisidra.ibge.gov.br/values/t/136/p/2000-2010/v/93/c86/2776,2777,2778,2779,2780,2781/n3/all"

# ----------------- DATAFRAMES -----------------
df_sexo = get_dataframe(
    url_sexo,
    ['D5C', 'D5N', 'D1N', 'D3N', 'D4N', 'V'],
    ['codigo_uf', 'uf', 'ano', 'sexo', 'domicilio', 'populacao']
)

df_raca = get_dataframe(
    url_raca,
    ['D4C', 'D4N','D3C', 'D3N', 'D1N', 'V'],
    ['codigo_uf', 'uf', 'codigo_raca', 'raca', 'ano', 'populacao']
)

# ----------------- CONEXÃO COM BANCO -----------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    connect_args={"options": "-c client_encoding=utf8"}
)

# ----------------- CARGA NO BANCO -----------------
df_sexo.to_sql("tabela_sexo", engine, if_exists="replace", index=False)
df_raca.to_sql("tabela_raca", engine, if_exists="replace", index=False)

print("Dados carregados no PostgreSQL com sucesso!")

