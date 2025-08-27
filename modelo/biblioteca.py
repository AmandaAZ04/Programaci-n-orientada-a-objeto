from modelo.direccion import Direccion

class Biblioteca(Direccion):
    def __init__(self,id_biblioteca=0,nombre_biblio='',id_direccion=0,habilitado=True):
        super().__init__(id_direccion) #type: ignore
        self.id_biblioteca = id_biblioteca
        self.nombre_biblio = nombre_biblio
        self.habilitado = habilitado