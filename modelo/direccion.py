from modelo.comuna import Comuna

class Direccion(Comuna):
    def __init__(self,id_direccion,id_comuna,calle,numero_d,departamento):
        super().__init__(id_comuna) #type: ignore
        self.id_direccion = id_direccion
        self.calle = calle
        self.numero_d = numero_d
        self.departamento = departamento