from sqlalchemy import column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comuna(Base):
    __tablename__ = 'comuna'
    id_comuna = column(Integer,primary_key=True)
    cod_comuna = column(String(5))
    nombre_comuna = column(String(50))

    def __repr__(self):
        return f"Id = {self.id_comuna}, Codigo Comuna = {self.cod_comuna}, Nombre Comuna = {self.nombre_comuna}"