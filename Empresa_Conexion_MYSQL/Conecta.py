# Contiene la creación de un objeto de conexión a la base de datos
# y ejecución de los métodos de la clase

from Database import *
from os import system

db = Database()


while True:
    elige = input('\n Elije una opcion: \n\
        \t Mostrar todos los repuestos(l)\n\
        \t Insertar repuesto(i)\n\
        \t Mostrar un repuesto(b)\n\
        \t Eliminar un repuesto (e))\n\
        \t Fin(f)\n\
        \t ==> \n ').lower()
    if elige == 'b':
        codAbuscar = input('Ingrese código a buscar = \n')
        db.buscarRepuesto(codAbuscar)
    elif elige == 'l':
        db.listaRepuestos()
    elif elige == 'i':
        db.insertarRepuesto()
    elif elige == 'e':
        db.deleteRepuesto()
    elif elige == 'f':
        print('Fin')
        db.cerrarBD()
        break
    else:
        print('Error de opción')
        
    input('Pulse Enter para continuar...')
    system('cls')