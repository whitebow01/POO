# Contiene la definición de clase para conectarse a la base de datos empresa

import mysql.connector #Para interactuar con la base de datos

#Creación de la clase Database
class Database(): 
    #Constructor
    def __init__(self):  
        #Conexión a la base de datos:
        self.conexion = mysql.connector.connect( 
            host = 'localhost',
            user = 'root',
            password = 'carlos123',
            database = 'empresa'
        )
        #Creación del cursor
        self.cursor = self.conexion.cursor()    
        # El cursor es un objeto que permitirá ejecutar sentencias SQL 
        # (consultas, inserciones, actualizaciones, etc.) en la base de datos.
    

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()
    
    #Seleccionar y mostrar todos los registros de la tabla repuestos en la base de datos:
    def listRepuestos(self): 
        #Consulta SQL:
        sql = 'select * from repuestos'
        try:
            #Se ejecuta la consulta:
            self.cursor.execute(sql)
            #Se utiliza fetchall() para obtener todos los resultados, que se almacenan en repu:
            repu = self.cursor.fetchall() #devuelve una tupla con los registros de Repuestos
            #Los numero al lado de codigo etc, Nos dice cuantos espacios ocuparan al mostrarse. 
            #Asi se muestran los datos alineados en la terminal
            print((
            f"{'Codigo':10}"
            f"{'Nombre repuesto ':20}"
            f"{'Fecha fabricacion ':12}"
            f"{'Precio proveedor ':12}"
            f"{'Precio venta ':12}"
            f"{'Peso ':12}"
            ))
            #Iteración y formato de cada registro:
            for rep in repu:
                print(f"{rep[0]:10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}{rep[3]:<12}{rep[4]:<12}{rep[5]:<12}")
        #Si hay un error, aparecerá en pantalla:       
        except Exception as err:
            print(err)
    def createRepuesto(self):
        codR = input('Codigo = \n')
        sql1 = 'select codrep from repuestos where codrep ='+repr(codR)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                nomR = input('Nombre =\n')
                fechaF = input('Fecha de fabricacion (dd/mm/aaaa) = \n')
                precioProv = int(input('Precio de proveedor = \n'))
                precioVent = int(input('Precio de venta = \n'))
                peso = float(input('Peso(kg) = \n'))
                sql2 = "insert into repuestos values("+repr(codR)+","+repr(nomR)+\
                    ",str_to_date("+repr(fechaF)+",'%d/%j/%Y'),"+repr(precioProv)+\
                    ","+repr(precioVent)+","+repr(peso)+")"
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()    
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print('Ya existe este codigo')
        except Exception as err:
            print(err)        
    
    def readRepuesto(self):    
        codAbuscar = input('Ingrese código a buscar = \n')
    
        sql = 'select * from repuestos where codrep = '+repr(codAbuscar) 
        #repr agrega cremillas al cod
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep is not None:
                print((
                f"{'Codigo':10}"
                f"{'Nombre repuesto ':20}"
                f"{'Fecha fabricacion ':12}"
                f"{'Precio proveedor ':12}"
                f"{'Precio venta ':12}"
                f"{'Peso ':12}"
                ))
                
                print(f"{rep[0]:10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}{rep[3]:<12}{rep[4]:<12}{rep[5]:<12}")
            else:
                print('Codigo no existe en la base de datos')
        except Exception as err:
            print("Error al realizar la consulta", err)     

    def updateRepuestos(self):
        codAbuscar = input('Ingrese código a Actualizar = \n')
        sql1 = 'select * from repuestos where codrep='+repr(codAbuscar)
        try:
            self.cursor.execute(sql1)
            rep=self.cursor.fetchone()
            if rep!= None:
                print((
                    f"{'Codigo':10}"
                    f"{'Nombre repuesto ':20}"
                    f"{'Fecha fabricacion ':12}"
                    f"{'Precio proveedor ':12}"
                    f"{'Precio venta ':12}"
                    f"{'Peso ':12}"
                    ))
                print(f"{rep[0]:10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}{rep[3]:<12}{rep[4]:<12}{rep[5]:<12}")
                ##Da la opcion de elegir que desea modificar
                elige=input('\n Que desea modificar?\n Nombre(n)\n Fecha de fabricacion(f)\n Precio proveedor(p)\n Precio venta(v)\n peso(k)\n=').lower()
                if elige=='f':
                    nueva=input('Ingrese nueva fecha(dd/mm/aaaa)=')
                    sql2 = "update repuestos set fechafabr=\
                        str_to_date("+repr(nueva)+",'%d/%m/%Y') where codrep="+repr(codAbuscar)
                else:
                    if elige=='n':
                        campo='nomrep'
                        nuevo=input('Ingrese nuevo nombre=')
                    if elige=='p':
                        campo='precioproveedor'
                        nuevo=int(input('Ingrese nuevo precio de proveedor='))
                    if elige=='v':
                        campo='precioventa'
                        nuevo=int(input('Ingrese nuevo precio de venta='))
                    if elige=='k':
                        campo='peso'
                        nuevo=float(input('Ingrese nuevo peso='))
                    sql2 = 'update repuestos set '+campo+'='+repr(nuevo)+' where codrep='+repr(codAbuscar)
                    try:
                        self.cursor.execute(sql2)
                        self.conexion.commit()
                    except Exception as err:
                        self.conexion.rollback()
                        print(err)
            else:
                print('No existe ese código')
        except Exception as err: 
            print(err)         
            
    def deleteRepuesto(self):
        codAbuscar = input('Ingrese código a Eliminar = \n')
        sql1 = 'select * from repuestos where codrep='+repr(codAbuscar)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                sql2 = 'select * from ventas where codrepuesto ='+repr(codAbuscar)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchone()!= None:
                        print('No se puede eliminar, porque esta en la tabla Ventas')
                    else:
                        sql3 = 'delete from repuestos where codrep='+repr(codAbuscar)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print('No existe este codigo')
        except Exception as err:
            print(err)
    
    