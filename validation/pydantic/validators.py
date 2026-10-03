from pydantic import BaseModel, field_validator, model_validator

"""
@field_validator: Valida um campo individual antes ou depois da validação padrão.

@model_validator: Valida múltiplos campos de forma interdependente (validação no nível do objeto).
"""

class SignUp(BaseModel):
    username: str
    password: str
    confirm_password: str

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('O nome de usuário deve ser alfanumérico')
        return v

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError('As senhas não coincidem')
        return self


if __name__ == "__main__":

    user_harry = {
        'username': "@!#",
        "password": "potter",
        "confirm_password": "patter"
    }

    try:
        user1 = SignUp(**user_harry)
    except Exception as e:
        print(e)
