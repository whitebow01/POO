from Departamento import Departamento
from Casa import Casa



dir1=input('Ingrese dirección=')
sup1=float(input('Ingrese superficie='))
piso=int(input('Ingrese piso='))
depto1=Departamento(dir1,sup1,piso)
print(depto1)

casa1=Casa('Maipú 2349 Concepción',98.3,14.6)
print(casa1)
