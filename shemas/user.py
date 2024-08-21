from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    email: str = Field(lmin_length=5, max_length=150, examples=["email@midominio.com"])
    password: str = Field(lmin_length=5, max_length=15, examples=["********"])