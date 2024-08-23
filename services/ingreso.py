from models.empleado import Empleado as EmpleadoModel
from shemas.empleado import Empleado as EmpleadoShema
from models.registro import Registro as RegistroModel
from shemas.registro import Registro as RegistroShema
from services.registro import RegistroService
from services.empleado import EmpleadoService
from datetime import datetime

class IngresoService():

    def __init__(self, db) -> None:
        self.db = db

    def ingreso(sefl, cedula):
        db = sefl.db
        result : EmpleadoShema = EmpleadoService(db).get_by_cedula(cedula)
        if not result:
            return mensaje(result, "Empleado no registrado")
        registro: RegistroShema = RegistroService(db).get_by_empleado_id_fecha(result.id, fecha())
        if not registro:
            new_registro =  RegistroShema(empleado_id = result.id)
            RegistroService(db).create_registro(new_registro)
            return mensaje(result, "Ingreso")
        else:
            if not registro.salida:
                update_salida = RegistroShema(salida = hora(), empleado_id = result.id)
                RegistroService(db).update_registro(registro.id, update_salida)
                return mensaje(result, "Salida")
            else: return mensaje(result, "Salida ya fue procesada!")


def mensaje(empleado: EmpleadoShema, mensaje: str):
    
    if mensaje != "Empleado no registrado":
        response = {
            "message": f"{mensaje}", 
            "cedula": f"{empleado.cedula}", 
            "Apellido1": f"{empleado.apellido1}", 
            "Apellidos": f"{empleado.apellido2}", 
            "Nombre1": f"{empleado.nombre1}", 
            "Nombres": f"{empleado.nombre2}", 
            "Hora": f"{hora()}", 
            "Fecha": f"{fecha()}"
        }
    else:
        response = {
            "message": f"{mensaje}", 
            "cedula": "", 
            "Apellido1": "", 
            "Apellidos": "", 
            "Nombre1": "", 
            "Nombres": "", 
            "Hora": f"{hora()}", 
            "Fecha": f"{fecha()}"
        }       

    return response

def fecha():
    fecha_actual = datetime.now()
    return fecha_actual.date().strftime("%Y-%m-%d")

def hora():
    hora_actual = datetime.now()
    return hora_actual.time().strftime("%H:%M:%S")    
