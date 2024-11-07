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
        
        input('Pulse Enter para continuar...')
        system('cls')