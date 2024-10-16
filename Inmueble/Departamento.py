from Inmueble import Inmueble


class Departamento(Inmueble):
    def __init__(self, dir, supConstr, numpiso):
        super().__init__(dir,supConstr)
        self.piso=numpiso
        
    def __str__(self):
        return 'Depto: Direccion='+self.direccion+\
            ',Superficie Construida='+str(self.superficieConstr)+\
            ',Piso='+str(self.piso)         