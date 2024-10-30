# Contiene la creación de un objeto de conexión a la base de datos
# y ejecución de los métodos de la clase

from Database import *
from os import system

db = Database()


while True:
    elige = input('\n Elije una opcion: \n\
        \t Mostrar un repuesto(u)\n\
        \t Mostrar todos los repuestos(t)\n\
        \t Fin(f)\n\
        \t ==>').lower()
    if elige == 'u':
        codAbuscar = input('Ingrese código a buscar =')
        db.BuscarRepuesto(codAbuscar)
    elif elige == 't':
        db.ListaRepuestos()
    elif elige == 'f':
        print('Fin')
        db.cerrarBD()
        break
    else:
        print('Error de opción')
        
    input('Pulse Enter para continuar...')
    system('cls')