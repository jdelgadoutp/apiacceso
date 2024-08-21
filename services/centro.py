from models.centro import Centro as CentroModel
from shemas.centro import Centro as CentroShema

class CentroService():

    def __init__(self, db) -> None:
        self.db = db

    def get_centros(self):
        result = self.db.query(CentroModel).all()
        return result

    def get_centro(self, id):
        result = self.db.query(CentroModel).filter(CentroModel.id == id).first()
        return result

    def get_by_nombre(self, nombre):
        result = self.db.query(CentroModel).filter(CentroModel.nombre == nombre).all()
        return result

    def create_centro(sefl, centro : CentroShema):
        new_centro = CentroModel(**centro.dict())
        sefl.db.add(new_centro)
        sefl.db.commit()
        return

    def update_centro(self, id, data : CentroShema):
        centro = self.db.query(CentroModel).filter(CentroModel.id == id).first()
        centro.nit = data.nit
        centro.dv = data.dv
        centro.nombre = data.nombre
        centro.direccion = data.direccion
        centro.telefono = data.telefono
        centro.email = data.email
        self.db.commit()
        return    

    def delete_centro(self, id):
        self.db.query(CentroModel).filter(CentroModel.id == id).delete()
        self.db.commit()
        return    