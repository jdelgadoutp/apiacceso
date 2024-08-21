from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from config.database import Session
from typing import List
from fastapi.encoders import jsonable_encoder
from services.empleado import EmpleadoService
from shemas.empleado import Empleado
from utils.jwt_manager import create_token
from middelware.jwt_bearer import JWTBearer

empleado_router = APIRouter()

@empleado_router.get('/empleados', tags=['empleado'], response_model=List[Empleado], status_code=200, dependencies=[Depends(JWTBearer())])
def get_empleado() -> List[Empleado]:
    db = Session()
    result = EmpleadoService(db).get_empleados()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@empleado_router.post('/empleados', tags=['empleado'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_empleado(empleado: Empleado) -> dict:
    db = Session()
    EmpleadoService(db).create_empleado(empleado)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el empleado"})

@empleado_router.get('/empleados/{id}', tags=['empleado'], response_model=Empleado, dependencies=[Depends(JWTBearer())])
def get_empleado(id: int = Path(ge=1, le=99999999999)) -> Empleado:
    db = Session()
    result = EmpleadoService(db).get_empleado(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@empleado_router.get('/empleados/', tags=['empleado'], response_model=List[Empleado], dependencies=[Depends(JWTBearer())])
def get_empleado_by_cedula(cedula: str = Query(min_length=1, max_length=30)) -> List[Empleado]:
    db = Session()
    result = EmpleadoService(db).get_by_cedula(cedula)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@empleado_router.put('/empleados/{id}', tags=['empleado'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_empleado(id: int, empleado: Empleado)-> dict:
    db = Session()
    result = EmpleadoService(db).get_empleado(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    
    EmpleadoService(db).update_empleado(id, empleado)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el empleado"})

@empleado_router.delete('/empleados/{id}', tags=['empleado'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_empleado(id: int)-> dict:
    db = Session()
    result = EmpleadoService(db).get_empleado(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    EmpleadoService(db).delete_empleado(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el empleado"})