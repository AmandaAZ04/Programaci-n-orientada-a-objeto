from modelo.autor import Autor
from modelo.biblioteca import Biblioteca
from modelo.categoria import Categoria

class Libro(Autor,Biblioteca,Categoria):
    def __init__(self,id_libro=0,titulo_libro='',id_autor=0,paginas=0,copias_libro=0,id_biblioteca=0,habilitado_libro=True,id_categoria=0):
        super().__init__(id_autor) #type: ignore
        super().__init__(id_biblioteca) #type: ignore
        super().__init__(id_categoria) #type: ignore
        self.id_libro = id_libro
        self.titulo_libro = titulo_libro
        self.paginas = paginas
        self.copias_libro = copias_libro
        self.habilitado_libro = habilitado_libro