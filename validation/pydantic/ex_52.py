from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nome: str
    email: str
    idade: int = Field(ge=0)

if __name__ == "__main__":

    user1_dict = {
        'nome': "Lucas",
        'email': "lucas@google.com",
        'idade': 68
    }

    user2_dict = {
            'nome': 'Terry',
            'email': "terry@google.com",
            'idade': -1
    }

    try:
        user_1 = Usuario(**user1_dict)
        print(user_1)
        user_2 = Usuario(**user2_dict)
        print(user_2)
    except Exception as e:
        print(e)