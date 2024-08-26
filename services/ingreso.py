from shemas.empleado import Empleado as EmpleadoShema
from shemas.registro import Registro as RegistroShema
from shemas.centro import Centro as CentroShema
from services.registro import RegistroService
from services.empleado import EmpleadoService
from services.centro import CentroService
from datetime import datetime

class IngresoService():

    def __init__(self, db) -> None:
        self.db = db

    def ingreso(sefl, cedula):
        db = sefl.db
        result : EmpleadoShema = EmpleadoService(db).get_by_cedula(cedula)
        if not result:
            return mensaje(result, "Advertencia empleado no registrado!")
        registro: RegistroShema = RegistroService(db).get_by_empleado_id_fecha(result.id, fecha())
        if not registro:
            new_registro =  RegistroShema(empleado_id = result.id)
            RegistroService(db).create_registro(new_registro)
            return mensaje(result, "Bienvenido registrado su ingreso")
        else:
            if not registro.salida:
                update_salida = RegistroShema(salida = hora(), empleado_id = result.id)
                RegistroService(db).update_registro(registro.id, update_salida)
                return mensaje(result, "Hasta pronto registrada su salida")
            else: return mensaje(result, "Advertencia salida ya fue procesada!")

    def get_by_centro(self, id, fecha):
        db = self.db
        registros = []
        centro: CentroShema = CentroService(db).get_centro(id)
        if not centro:
            return registros
        result: EmpleadoShema = EmpleadoService(db).get_by_centro(id)
        if not result:
            return registros
        for key in result:
            ingreso = ""
            salida = ""
            data: RegistroShema = RegistroService(db).get_by_empleado_id_fecha(key.id, fecha)
            if data:
                ingreso = data.ingreso
                salida = data.salida 
            registros.append({
                "centro_id": id,
                "nit": f"{centro.nit}-{centro.dv}",
                "nombre_centro": centro.nombre,
                "empleado_id": key.id,
                "cedula": key.cedula,
                "nombre_empleado": f"{key.apellido1} {key.apellido2} {key.nombre1} {key.nombre2}",
                "fecha": fecha,
                "ingreso": ingreso,
                "salida": salida,
                "hora": hora()
            })

        return registros
                
def mensaje(empleado: EmpleadoShema, mensaje: str):
    
    if mensaje != "Advertencia empleado no registrado!":
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
