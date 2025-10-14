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
    return {"mensagem": "Bem-vindos ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filmes(titulo:str, genero:str , ano:int , avaliacao:float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adcionado com sucesso!"}


@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({
                "id": linha[0],
                "titulo": linha[1],
                "genero": linha[2],
                "ano": linha[3],
                "avaliacao": linha[4]
            })
    return {"filmes":lista}

@app.put("/filmes/{id_filme}")
def update_filmes(id_filme: int, nova_avaliacao: float):
    filme = funcao.buscar_filme(id_filme)
    if filme:
        funcao.atualizar_filme(id_filme, nova_avaliacao)
        return {"mensagem": "Filme atualizado com sucesso!"}
    else:
        return { "erro":"Filme não encontrado"}
