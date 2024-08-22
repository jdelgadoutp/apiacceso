from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from config.database import Session
from typing import List
from models.registro import Registro
from fastapi.encoders import jsonable_encoder
from middelware.jwt_bearer import JWTBearer
from services.registro import RegistroService
from shemas.registro import Registro
from services.ingreso import IngresoService

registro_router = APIRouter()

@registro_router.get('/registros', tags=['registro'], response_model=List[Registro], status_code=200, dependencies=[Depends(JWTBearer())])
def get_registros() -> List[Registro]:
    db = Session()
    result = RegistroService(db).get_registros()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@registro_router.post('/registros', tags=['registro'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_registro(registro: Registro) -> dict:
    db = Session()
    RegistroService(db).create_registro(registro)
    return JSONResponse(status_code=201, content={"message": "Se ha creado registro"})

@registro_router.get('/registros/{id}', tags=['registro'], response_model=Registro, dependencies=[Depends(JWTBearer())])
def get_registro(id: int = Path(ge=1, le=2000)) -> Registro:
    db = Session()
    result = RegistroService(db).get_registro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@registro_router.get('/registros/', tags=['registro'], response_model=List[Registro], dependencies=[Depends(JWTBearer())])
def get_registro_by_empleado_id_fecha(empleado_id: str = Query(min_length=1, max_length=200), fecha: str = Query(min_length=1, max_length=10)) -> List[Registro]:
    db = Session()
    result = RegistroService(db).get_by_empleado_id_fecha(empleado_id, fecha)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@registro_router.put('/registros/{id}', tags=['registro'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_registro(id: int, registro: Registro)-> dict:
    db = Session()
    result = RegistroService(db).get_registro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    
    RegistroService(db).update_registro(id, registro)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@registro_router.delete('/registros/{id}', tags=['registro'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_registro(id: int)-> dict:
    db = Session()
    result = RegistroService(db).get_registro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    RegistroService(db).delete_registro(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado registro"})
