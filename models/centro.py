from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Centro(Base):

    __tablename__ = "centro"

    id = Column(Integer, primary_key=True)
    nit = Column(Integer)
    dv = Column(Integer)
    nombre = Column(String(200))
    direccion = Column(String(100))
    telefono = Column(String(30))
    email = Column(String(150))

    empleado = relationship('Empleado', back_populates='centro')