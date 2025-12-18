# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, os estudantes irão construir uma pequena API REST usando o framework FastAPI. Eles irão definir endpoints para criar, listar, atualizar e deletar recursos — seguindo boas práticas de design de APIs, validação com Pydantic e documentação automática.

## 📝 Tasks

### 🛠️ Configurar o Projeto

#### Description
Crie um ambiente virtual, instale o FastAPI e um servidor ASGI (uvicorn). Estruture o projeto com um arquivo principal `main.py` e um módulo para modelos e rotas.

#### Requirements
Completed program should:

- Ter um endpoint `GET /items` que retorna a lista de itens.
- Ter um endpoint `POST /items` que cria um novo item com validação.
- Ter endpoints `GET /items/{id}`, `PUT /items/{id}` e `DELETE /items/{id}`.


### 🛠️ Implementar Endpoints e Validação

#### Description
Utilize Pydantic para definir os modelos `ItemCreate` e `Item` e implemente lógica simples em memória (uma lista) para armazenar os itens durante a execução.

#### Requirements
Completed program should:

- Validar entrada no `POST` e `PUT` usando Pydantic.
- Retornar códigos HTTP apropriados (`201` para criação, `404` quando não encontrado, etc.).
- Expor documentação automática (OpenAPI) gerada pelo FastAPI.


### 🛠️ (Opcional) Persistência e Testes

#### Description
Para estudantes avançados: adicionar persistência simples usando SQLite (via SQLModel ou SQLAlchemy) e escrever testes para os endpoints usando `pytest` and `httpx`.

#### Requirements
Completed program should:

- Incluir um `requirements.txt` opcional listando dependências.
- Fornecer instruções de como executar os testes.


## How to run (developer)

1. Criar e ativar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install fastapi uvicorn
```

3. Executar a aplicação:

```bash
uvicorn main:app --reload
```


## Starter Code

Veja `starter-code.py` na mesma pasta para um ponto de partida simples.
