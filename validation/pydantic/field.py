from pydantic import BaseModel, Field

"""
A função Field permite adicionar metadados, regras de validação adicionais e valores padrão dinâmicos.
"""

class Produto(BaseModel):
    name: str = Field(min_lenght=2,max_length=50, description = "Nome comercial do produto",
        examples=["Notebook Gamer", "Mouse sem fio"])
    price: float = Field(gt=0, description="Preço deve ser positivo")
    tags: list[str] = Field(default_factory=list)