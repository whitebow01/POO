# Contiene la creación de un objeto de conexión a la base de datos
# y ejecución de los métodos de la clase

from Database import *
from os import system

db = Database()


while True:
    elige = input('\n Elije una opcion: \n\
        \t Mostrar todos los repuestos(l)\n\
        \t Mostrar un repuesto(b)\n\
        \t Insertar repuesto(c)\n\
        \t Eliminar un repuesto (d)\n\
        \t Modificar(m)\n\
        \t Fin(f)\n\
        \t ==> \n ').lower()
    if elige == 'b':
        codAbuscar = input('Ingrese código a buscar = \n')
        db.readRepuesto(codAbuscar)
    elif elige == 'l':
        db.listRepuestos()
    elif elige == 'c':
        db.createRepuesto()
    elif elige == 'd':
        db.deleteRepuesto()
    elif elige=='m':
        db.updateRepuestos()

    elif elige == 'f':
        print('Fin')
        db.cerrarBD()
        break
    else:
        print('Error de opción')
        
    input('Pulse Enter para continuar...')
    system('cls')