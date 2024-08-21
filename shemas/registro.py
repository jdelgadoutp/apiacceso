from pydantic import BaseModel, Field
from typing import Optional

class Registro(BaseModel):
    id: Optional[int] = None
    fecha: Optional[str] = None
    empleado_id: int = Field(ge=0, le=2000, examples=["1"])
    ingreso: Optional[str] = None
    salida: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "fecha": "2024-02-17",
                "empleado_id": 1,
                "ingreso": "00:00:00",
                "salida": "00:00:00"
            }
        }