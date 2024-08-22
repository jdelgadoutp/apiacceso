from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middelware.error_handler import ErrorHandler
from routers.centro import centro_router
from routers.user import user_router
from routers.empleado import empleado_router
from routers.registro import registro_router
from routers.ingreso import ingreso_router

app = FastAPI()
app.title = "Acceso Asservi S.A.S."
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

app.add_middleware(ErrorHandler)

app.include_router(centro_router)
app.include_router(user_router)
app.include_router(empleado_router)
app.include_router(registro_router)
app.include_router(ingreso_router)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Api Control de acceso Asservi SAS</h1>')