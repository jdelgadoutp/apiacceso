from config.database import Base
from sqlalchemy import Column, Integer, Date, func, Time, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

def formato_fecha_hora():
    # Devuelve la fecha/hora formateada
    return datetime.now().strftime("%H:%M:%S")

class Registro(Base):

    __tablename__ = "registro"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, server_default=func.current_date())
    empleado_id = Column(Integer, ForeignKey("empleado.id"))
    ingreso = Column(Time, default=formato_fecha_hora())
    salida = Column(Time)

    empleado = relationship('Empleado', back_populates='registro')