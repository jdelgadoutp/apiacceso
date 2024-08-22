from models.empleado import Empleado as EmpleadoModel
from shemas.empleado import Empleado as EmpleadoShema

class EmpleadoService():

    def __init__(self, db) -> None:
        self.db = db

    def get_empleados(self):
        result = self.db.query(EmpleadoModel).all()
        return result

    def get_empleado(self, id):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
        return result

    def get_by_cedula(self, cedula):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.cedula == cedula).first()
        return result

    def create_empleado(sefl, empleado : EmpleadoShema):
        new_empleado = EmpleadoModel(**empleado.dict())
        sefl.db.add(new_empleado)
        sefl.db.commit()
        return

    def update_empleado(self, id, data : EmpleadoShema):
        empleado = self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
        empleado.cedula = data.cedula
        empleado.apellido1 = data.apellido1
        empleado.apellido2 = data.apellido2
        empleado.nombre1 = data.nombre1
        empleado.nombre2 = data.nombre2
        empleado.genero = data.genero
        empleado.nacimiento = data.nacimiento
        empleado.sanguineo = data.sanguineo
        empleado.contacto = data.contacto
        empleado.telefono_contacto = data.telefono_contacto
        empleado.contacto1 = data.contacto1
        empleado.telefono_contacto1 = data.telefono_contacto1
        empleado.arl = data.arl
        empleado.eps = data.eps
        empleado.centro_id = data.centro_id
        empleado.activo = data.activo
        
        self.db.commit()
        return    

    def delete_empleado(self, id):
        self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).delete()
        self.db.commit()
        return    