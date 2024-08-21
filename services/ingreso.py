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
        fecha_actual = datetime.now()
        hora_actual = datetime.now()
        hora = hora_actual.time().strftime("%H:%M:%S")
        fecha_formateada = fecha_actual.date().strftime("%Y-%m-%d")
        if not result:
            return {"message": "empleado no encontrado", "cedula": "", "Apellido1": "", "Apellidos": "", "Nombre1": "", "Nombres": "", "Hora": f"{hora}", "Fecha": f"{fecha_formateada}"}
        registro: RegistroShema = RegistroService(db).get_by_empleado_id_fecha(result.id, fecha_formateada)
        new_registro =  RegistroShema(empleado_id = result.id)
        if not registro:
            RegistroService(db).create_registro(new_registro)
            ingreso = {"message": "Ingreso", "cedula": f"{result.cedula}", "Apellido1": f"{result.apellido1}", "Apellidos": f"{result.apellido2}", "Nombre1": f"{result.nombre1}", "Nombres": f"{result.nombre2}", "Hora": f"{hora}", "Fecha": f"{fecha_formateada}"}  
            return ingreso
        else:
            if not registro.salida:
                update_salida = RegistroShema(salida = hora, empleado_id = result.id)
                RegistroService(db).update_registro(registro.id, update_salida)
                update = {"message": "Salida", "cedula": f"{result.cedula}", "Apellido1": f"{result.apellido1}", "Apellidos": f"{result.apellido2}", "Nombre1": f"{result.nombre1}", "Nombres": f"{result.nombre2}", "Hora": f"{hora}", "Fecha": f"{fecha_formateada}"} 
                return update
            else: return {"message": "Ya existe una salida procesada!", "cedula": f"{result.cedula}", "Apellido1": f"{result.apellido1}", "Apellidos": f"{result.apellido2}", "Nombre1": f"{result.nombre1}", "Nombres": f"{result.nombre2}", "Hora": f"{hora}", "Fecha": f"{fecha_formateada}"}  