from config.database import Base
from sqlalchemy import Column, String, Date, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

class Empleado(Base):

    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True)
    cedula = Column(String(30), nullable=False)
    apellido1 = Column(String(60), nullable=False)
    apellido2 = Column(String(60))
    nombre1 = Column(String(60), nullable=False)
    nombre2 = Column(String(60))
    genero = Column(String(1))
    nacimiento = Column(Date)
    sanguineo = Column(String(5))
    contacto = Column(String(150))
    telefono_contacto = Column(String(30))
    contacto1 = Column(String(150))
    telefono_contacto1 = Column(String(30))
    arl = Column(String(150))
    eps = Column(String(150))
    centro_id = Column(Integer, ForeignKey('centro.id'))
    activo = Column(Boolean, nullable=False, default=True)

    centro = relationship('Centro', back_populates='empleado')
    registro = relationship('Registro', back_populates='empleado')
