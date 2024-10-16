from Inmueble import Inmueble


class Casa(Inmueble):
    def __init__(self,dir,supConstr,supPatio):
        super().__init__(dir,supConstr)   
        self.supPatio=supPatio
        
    def __str__(self):
        return 'Casa: Direccion ='+self.direccion+\
            ', Superficie Construida = '+str(self.superficieConstr)+\
            ', Superficie del patio = '+str(self.supPatio)
