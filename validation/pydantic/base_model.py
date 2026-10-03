from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

user1_dict = {
    'id' : 178,
    'name': "Rex"
}

user1 = User(**user1_dict)
print(user1.name)
print(user1.model_dump()) # para dicionário
print(user1.model_dump_json()) # para json
