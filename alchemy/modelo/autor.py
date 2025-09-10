from sqlalchemy import column,Integer,String,Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from modelo.nacionalidad import Nacionalidad

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autor'
    id_autor = column(Integer, primary_key=True)
    nombre_autor = column(String(100))
    pseudonimo = column(String(100))
    habilitado = column(Boolean)
    id_nacionalidad = column(Integer, ForeignKey(Nacionalidad.id_nacionalidad))