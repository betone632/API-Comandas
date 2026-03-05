#Roberto Antunes Souza
from fastapi import APIRouter
from domain.entities.Produto import Produto

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"], status_code=200)
def get_produto():
    return {"msg": "produto get todos executado"}

@router.get("/produto/{id}", tags=["Produto"], status_code=200)
def get_produto_por_id(id: int):
    return {"msg": "produto get um executado", "id": id}

@router.post("/produto/", tags=["Produto"], status_code=200)
def post_produto(corpo: Produto):
    return {"msg": "produto post executado", "nome": corpo.nome, "preco": corpo.valor_unitario, "descricao": corpo.descricao}

@router.put("/produto/{id}", tags=["Produto"], status_code=200)
def put_produto(id: int):
    return {"msg": "produto put executado", "id": id}

@router.delete("/produto/{id}", tags=["Produto"], status_code=200)
def delete_produto(id: int):
    return {"msg": "produto delete executado", "id": id}