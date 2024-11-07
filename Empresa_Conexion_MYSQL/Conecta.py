# Contiene la creación de un objeto de conexión a la base de datos
# y ejecución de los métodos de la clase

from Database import *
from os import system

db = Database()

def default():
    print("Opcion fuera de rango") 
    return

menu = {1:db.listRepuestos, 
        2:db.readRepuesto, 
        3:db.createRepuesto, 
        4:db.deleteRepuesto, 
        5:db.updateRepuestos,
        6:exit
        }

while True:
        print("\n═══ Menú Principal Administrador ═══")
        print("1. Mostrar todos los repuestos")
        print("2. Mostrar un repuesto")
        print("3. Insertar repuesto")
        print("4. Eliminar un repuesto")
        print("5. Modificar")
        print("6. Fin")
        
        
        try: ##validacion solo numeros
            opcion = int(input("ELija una opción \n"))
            menu.get(opcion, default)()
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
        
    # elige = input('\n Elije una opcion: \n\
    #     \t Mostrar todos los repuestos(l)\n\
    #     \t Mostrar un repuesto(b)\n\
    #     \t Insertar repuesto(c)\n\
    #     \t Eliminar un repuesto (d)\n\
    #     \t Modificar(m)\n\
    #     \t Fin(f)\n\
    #     \t ==> \n ').lower()
    # if elige == 'b':
    #     codAbuscar = input('Ingrese código a buscar = \n')
    #     db.readRepuesto(codAbuscar)
    # elif elige == 'l':
    #     db.listRepuestos()
    # elif elige == 'c':
    #     db.createRepuesto()
    # elif elige == 'd':
    #     db.deleteRepuesto()
    # elif elige=='m':
    #     db.updateRepuestos()

    # elif elige == 'f':
    #     print('Fin')
    #     db.cerrarBD()
    #     break
    # else:
    #     print('Error de opción')
        
    # input('Pulse Enter para continuar...')
    # system('cls')