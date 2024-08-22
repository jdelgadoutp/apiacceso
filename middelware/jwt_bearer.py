from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token
from shemas.user import User
from services.user import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        db = Session()
        result: User = UserService(db).get_by_email(data["email"])
        if data['email'] != result.email:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")