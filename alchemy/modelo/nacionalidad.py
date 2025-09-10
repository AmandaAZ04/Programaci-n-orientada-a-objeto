from sqlalchemy import column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Nacionalidad(Base):
    __tablename__ = 'nacionalidad'
    id_nacionalidad = column(Integer,primary_key=True)
    pais = column(String(50))
    nacionalidad = column(String(50))