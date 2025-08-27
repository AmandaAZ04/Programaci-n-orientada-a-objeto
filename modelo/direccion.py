from modelo.comuna import Comuna

class Direccion(Comuna):
    def __init__(self,id_direccion=0,id_comuna=0,calle=0,numero_d=0,departamento=0):
        super().__init__(id_comuna) #type: ignore
        self.id_direccion = id_direccion
        self.calle = calle
        self.numero_d = numero_d
        self.departamento = departamento