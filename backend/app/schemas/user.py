from pydantic import BaseModel, EmailStr
from ..models.user import UserProfile  

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None
    password: str
    tipo_perfil: UserProfile

class UserOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    tipo_perfil: UserProfile

    class Config:
        from_attributes = True