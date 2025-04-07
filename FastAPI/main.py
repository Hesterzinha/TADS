# pip install fastapi[all] -> Instala todos os pacotes recomendados para o FastAPI, incluindo o Uvicorn, que é um servidor ASGI leve e rápido.
# pip install uvicorn -> Instala o Uvicorn.
# uvicorn main:app --reload -> Executa o servidor FastAPI. O --reload faz com que o servidor reinicie automaticamente quando você faz alterações no código.
# uvicorn (nome_do_arquivo):(nome_da_aplicaçao(app)) --reload

from typing import Union # Union é uma função do módulo typing que permite especificar que um valor pode ser de mais de um tipo.
from fastapi import FastAPI
from pydantic import BaseModel # Pydantic é uma biblioteca de validação de dados e gerenciamento de configurações, que é usada pelo FastAPI para validar os dados de entrada e saída.

app = FastAPI() # cria uma instância do FastAPI, que é o aplicação web que irá lidar com as requisições HTTP.



class Item(BaseModel): #criei uma classe que herda de BaseModel, que é uma classe base do Pydantic para validação de dados.
    name: str # tipo de dado string
    price: float # tipo de dado float
    is_offer: Union[bool, None] = None # tipo de dado booleano ou None, com valor padrão None
    # Union é usado para indicar que o valor pode ser de um tipo ou outro (neste caso, bool ou None).
    # none é um valor especial que representa a ausência de valor ou um valor nulo.


@app.get("/") # decorator que indica que essa função deve ser chamada quando uma requisição GET for feita para a raiz do aplicativo.
def read_root(): # função que retorna um dicionário com uma mensagem simples.
    return {"Hello": "World"} # retorna um dicionário com a chave "Hello" e o valor "World".


@app.get("/items/{item_id}") # decorator que indica que essa função deve ser chamada quando uma requisição GET for feita para o endpoint /items/{item_id}
def read_item(item_id: int, q: Union[str, None] = None): # função que recebe um parâmetro item_id do tipo inteiro e um parâmetro opcional q do tipo string ou None.
    return {"item_id": item_id, "q": q} # retorna um dicionário com o item_id e o valor de q (se fornecido).


@app.put("/items/{item_id}") # decorator que indica que essa função deve ser chamada quando uma requisição PUT for feita para o endpoint /items/{item_id}
def update_item(item_id: int, item: Item): # função que recebe um parâmetro item_id do tipo inteiro e um objeto item do tipo Item (definido anteriormente).
    return {"item_name": item.name, "item_id": item_id} # retorna um dicionário com o nome do item e o item_id.
