from modelo.direccion import Direccion
from modelo.biblioteca import Biblioteca

class Lector(Direccion,Biblioteca): #type: ignore
    def __init__(self,id_lector,rut_lector,digito_verificador,nombre_lector,id_direccion,id_biblioteca,habilitado_lector,correo_lector,telefono_lector):
        super().__init__(id_direccion) #type: ignore
        super().__init__(id_biblioteca) #type: ignore
        self.id_lector = id_lector
        self.rut_lector = rut_lector
        self.digito_verificador = digito_verificador
        self.nombre_lector = nombre_lector
        self.habilitado_lector = habilitado_lector
        self.correo_lector = correo_lector
        self.telefono_lector = telefono_lector