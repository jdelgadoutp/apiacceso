from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from config.database import Session
from typing import List
from fastapi.encoders import jsonable_encoder
from services.user import UserService
from shemas.user import User
from utils.jwt_manager import create_token
from middelware.jwt_bearer import JWTBearer

user_router = APIRouter()

@user_router.get('/users', tags=['usuario'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
def get_user() -> List[User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.post('/users', tags=['usuario'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})

@user_router.get('/users/{id}', tags=['usuario'], response_model=User, dependencies=[Depends(JWTBearer())])
def get_user(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/', tags=['usuario'], response_model=List[User], dependencies=[Depends(JWTBearer())])
def get_user_by_email(email: str = Query(min_length=1, max_length=100)) -> List[User]:
    db = Session()
    result = UserService(db).get_by_email(email)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.put('/users/{id}', tags=['usuario'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_user(id: int, user: User)-> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})

@user_router.delete('/users/{id}', tags=['usuario'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_user(id: int)-> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})

@user_router.post('/login', tags=['auth'])
def login(user: User):
    db = Session()
    valida: User = UserService(db).get_by_email(user.email)
    if not valida:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})  
    if user.email == valida.email and user.password == valida.password:
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    else: return JSONResponse(status_code=403, content={"message": "Usuario ó password invalidos"})  