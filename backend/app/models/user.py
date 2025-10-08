from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from ..core.database import Base 
import enum

class UserProfile(str, enum.Enum):
    DONO = "dono"
    ATLETA = "atleta"
    ORGANIZADOR = "organizador"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    tipo_perfil = Column(SQLAlchemyEnum(UserProfile), nullable=False)