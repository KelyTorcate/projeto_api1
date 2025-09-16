import pandas as pd
from sqlalchemy import create_engine
from fastapi import FastAPI, Query
from dotenv import load_dotenv
import os

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

# ----------------- FASTAPI -----------------
app = FastAPI(
    title="API IBGE",
    description="API para servir dados populacionais",
    version="1.0"
)

@app.get("/")
def root():
    return {"mensagem": "API IBGE está no ar!"}

@app.get("/sexo")
def get_tabela_sexo(
    ano: int | None = Query(None, description="Filtrar por ano")
):
    query = "SELECT * FROM tabela_sexo WHERE 1=1"
    if ano:
        query += f" AND ano = {ano}"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

@app.get("/raca")
def get_tabela_raca(
    ano: int | None = Query(None, description="Filtrar por ano")
):
    query = "SELECT * FROM tabela_raca WHERE 1=1"
    if ano:
        query += f" AND ano = {ano}"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")
