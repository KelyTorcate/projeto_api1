# 📘 Projeto: API IBGE - Dados Populacionais

## 📝 Descrição

Este projeto consiste em uma **API desenvolvida com FastAPI** que fornece dados populacionais do IBGE, permitindo consultas por **ano**.  
Os dados são extraídos das APIs públicas do IBGE, tratados com **Pandas** e armazenados em um banco **PostgreSQL**.

O projeto serve como exemplo de **pipeline completo de dados**:  
**Extração → Transformação → Armazenamento → Disponibilização via API**

---

## ⚙️ Funcionalidades

- Consulta de população por ano para:
  - Sexo e domicílio
  - Cor/Raça
- Limpeza e tratamento de dados antes de salvar no banco.
- Conexão segura com PostgreSQL usando variáveis de ambiente (`.env`).

---

## 🛠 Tecnologias Utilizadas

- **Python**  
- **FastAPI** → criação da API  
- **Pandas** → manipulação e limpeza de dados  
- **SQLAlchemy** → conexão com PostgreSQL  
- **PostgreSQL** → banco de dados relacional  
- **python-dotenv** → gerenciamento de credenciais de forma segura  

---

## 📂 Estrutura do Projeto

**Projeto_API_1:**

**etl_ibge.py**         # Script de coleta, tratamento e upload dos dados no PostgreSQL
**api_ibge.py**         # Script que roda a API com FastAPI
**README.md**           # Descrição do projeto
**requirements.txt**    # Bibliotecas usadas no projeto
**.env**                # Credenciais do PostgreSQL (NÃO subir no GitHub)


**Instalação e Execução:**

Pré-requisitos:
Python 3.10 ou superior
PostgreSQL instalado e em execução

## Como rodar localmente

1. Clonar repositório
2. Criar e ativar ambiente virtual
3. Instalar dependências: `pip install -r requirements.txt`
4. Configurar arquivo `.env` com credenciais do PostgreSQL
5. Rodar ETL: `python ETL_IBGE.py`
6. Rodar API: `uvicorn API_IBGE:app --reload`

   
**Endpoints Disponíveis:**

**Raiz**

GET /
Retorna mensagem indicando que a API está no ar.


**Sexo/Domicílio**

GET /sexo?ano=<ano>
Filtra dados por ano.
Exemplo: /sexo?ano=2010


**Cor/Raça**

GET /raca?ano=<ano>
Filtra dados por ano.
Exemplo: /raca?ano=2010

