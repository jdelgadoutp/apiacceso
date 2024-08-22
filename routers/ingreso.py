from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middelware.jwt_bearer import JWTBearer
from services.ingreso import IngresoService

ingreso_router = APIRouter()

@ingreso_router.post('/ingresos/', tags=['ingreso'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def ingreso(cedula: str):
    db = Session()
    result = IngresoService(db).ingreso(cedula)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))