from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="A$$ervi.$@$.##", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="A$$ervi.$@$.##", algorithms=['HS256'])
    return data