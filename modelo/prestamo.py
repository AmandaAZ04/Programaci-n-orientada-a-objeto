from modelo.libro import Libro
from modelo.lector import Lector

class Prestamo(Libro,Lector): #type: ignore
    def __init__(self,id_prestamo,id_libro,id_lector,fecha_prestamo,plazo_devolucion,fecha_entrega):
        super().__init__(id_libro) #type: ignore
        super().__init__(id_lector) #type: ignore
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.plazo_devolucion = plazo_devolucion
        self.fecha_entrega = fecha_entrega