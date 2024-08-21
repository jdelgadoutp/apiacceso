from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from config.database import Session
from typing import List
from models.centro import Centro
from fastapi.encoders import jsonable_encoder
from middelware.jwt_bearer import JWTBearer
from services.centro import CentroService
from shemas.centro import Centro

centro_router = APIRouter()

@centro_router.get('/centros', tags=['centro'], response_model=List[Centro], status_code=200, dependencies=[Depends(JWTBearer())])
def get_centros() -> List[Centro]:
    db = Session()
    result = CentroService(db).get_centros()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@centro_router.post('/centros', tags=['centro'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_centro(centro: Centro) -> dict:
    db = Session()
    CentroService(db).create_centro(centro)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el centro"})

@centro_router.get('/centros/{id}', tags=['centro'], response_model=Centro, dependencies=[Depends(JWTBearer())])
def get_centro(id: int = Path(ge=1, le=2000)) -> Centro:
    db = Session()
    result = CentroService(db).get_centro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@centro_router.get('/centros/', tags=['centro'], response_model=List[Centro], dependencies=[Depends(JWTBearer())])
def get_centro_by_nombre(nombre: str = Query(min_length=1, max_length=200)) -> List[Centro]:
    db = Session()
    result = CentroService(db).get_by_nombre(nombre)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@centro_router.put('/centros/{id}', tags=['centro'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_centro(id: int, centro: Centro)-> dict:
    db = Session()
    result = CentroService(db).get_centro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    
    CentroService(db).update_centro(id, centro)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el centro"})

@centro_router.delete('/centros/{id}', tags=['centro'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_centro(id: int)-> dict:
    db = Session()
    result = CentroService(db).get_centro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    CentroService(db).delete_centro(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el centro"})
