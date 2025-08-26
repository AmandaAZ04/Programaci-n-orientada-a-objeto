from modelo.direccion import Direccion

class Biblioteca(Direccion):
    def __init__(self,id_biblioteca,nombre_biblio,id_direccion):
        super().__init__(id_direccion) #type: ignore
        self.id_biblioteca = id_biblioteca
        self.nombre_biblio = nombre_biblio