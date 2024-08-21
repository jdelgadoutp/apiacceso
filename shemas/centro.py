from pydantic import BaseModel, Field
from typing import Optional, List

class Centro(BaseModel):
    id: Optional[int] = None
    nit: int = Field(ge=0, le=999999999)
    dv: int = Field(ge=0, le=9)
    nombre: str = Field(lmin_length=5, max_length=200, examples=["Nombre de centro de trabajo"])
    direccion: str = Field(lmin_length=5, max_length=100, examples=["Diredción centro de trabajo"])
    telefono:str = Field(min_length=5, max_length=30, examples=["606555555"])
    email:str = Field(min_length=5, max_length=150, examples=["correo@midominio.com"])