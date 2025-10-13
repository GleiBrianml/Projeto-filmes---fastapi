from fastapi import FastAPI
import funcao
# python -m uvicorn api:app --reload
#Testar api Fastapi
# /docs > Documentação Swagger 
# /redoc > Documentação
#inciar o fastapi
app = FastAPI(title="Gerenciador de Filmes")


@app.get("/")
def home():
    return {"mensagem": "Quero café prof"}

@app.post("/filmes")
def criar_filmes(titulo:str, genero:str , ano:int , avaliacao:float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adcionado com sucesso!"}