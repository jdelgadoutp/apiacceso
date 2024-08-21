from models.registro import Registro as RegistroModel
from shemas.registro import Registro as RegistroShema

class RegistroService():

    def __init__(self, db) -> None:
        self.db = db

    def get_registros(self):
        result = self.db.query(RegistroModel).all()
        return result

    def get_registro(self, id):
        result = self.db.query(RegistroModel).filter(RegistroModel.id == id).first()
        return result

    def get_by_empleado_id_fecha(self, empleado_id, fecha):
        result = self.db.query(RegistroModel).filter(RegistroModel.empleado_id == empleado_id, RegistroModel.fecha == fecha).first()
        return result

    def create_registro(sefl, registro : RegistroShema):
        new_registro = RegistroModel(**registro.dict())
        sefl.db.add(new_registro)
        sefl.db.commit()
        return

    def update_registro(self, id, data : RegistroShema):
        registro = self.db.query(RegistroModel).filter(RegistroModel.id == id).first()
        registro.salida = data.salida
        self.db.commit()
        return    

    def delete_registro(self, id):
        self.db.query(RegistroModel).filter(RegistroModel.id == id).delete()
        self.db.commit()
        return