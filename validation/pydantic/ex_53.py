from pydantic import BaseModel, field_validator

class Item(BaseModel):
    nome: str
    preco: float

    @field_validator('preco')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
            if v < 0:
                raise ValueError('preco deve ser positivo')
            return v

class Pedido(BaseModel):
    id: int = 101
    itens: list[Item]

item1 = {
    'nome': 'blusa',
    'preco': 12.50
}

item2 = {
    'nome': 'brinquedo',
    'preco': 20.10
}

item3 = {
    'nome': 'universo',
    'preco': -1000
}


item_1 = Item.model_validate(item1)
item_2 = Item.model_validate(item2)
item_3 = Item.model_validate(item3)

pedido_dict = {
    'itens': [item_1, item_2] 
}
carrinho = Pedido.model_validate(pedido_dict)

print(carrinho)


