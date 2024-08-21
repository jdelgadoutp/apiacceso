from pydantic import BaseModel, Field
from typing import Optional, List

class Empleado(BaseModel):

    id: Optional[int] = None
    cedula: str =  Field(lmin_length=5, max_length=30, examples=["99999999"])
    apellido1: str = Field(lmin_length=5, max_length=60, examples=["Apellido 1"])
    apellido2: str = Field(lmin_length=5, max_length=60, examples=["Apellidos"])
    nombre1: str = Field(lmin_length=5, max_length=60, examples=["Nombre 1"])
    nombre2: str = Field(lmin_length=5, max_length=60, examples=["Nombres"])
    genero: str = Field(lmin_length=1, max_length=1, examples=["M"])
    nacimiento: str = Field(lmin_length=5, max_length=10, examples=["2024-01-01"])
    sanguineo: str = Field(lmin_length=1, max_length=5, examples=["A+"])
    contacto: str = Field(lmin_length=5, max_length=150, examples=["Nombre contacto en caso de emergencia"])
    telefono_contacto: str = Field(lmin_length=5, max_length=30, examples=["606-5555555"])
    centro_id: int = Field(ge=0, le=2000, examples=["1"])
    activo: bool = Field()