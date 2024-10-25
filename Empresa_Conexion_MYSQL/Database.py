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
    def select_todos(self):
        #Consulta SQL:
        sql = 'select * from repuestos'
        try:
            #Se ejecuta la consulta:
            self.cursor.execute(sql)
            #Se utiliza fetchall() para obtener todos los resultados, que se almacenan en repu:
            repu = self.cursor.fetchall() #devuelve una tupla con los registros de Repuestos
            print(f"\
                {'Codigo':10 }'\
                {'Nombre repuesto ':20}\
                {'Fecha fabricacion ':12}\
                {'Precio proveedor ':12}\
                {'Precio venta ':12}
                {'Peso ':12}"
                )
            #Iteración y formato de cada registro:
            for rep in repu:
                print(f"\
                    #codigo
                    {rep[0]:10}\ 
                    #nombre
                    {rep[1]:20}\ 
                    #fecha
                    {rep[2].strftime('%d/%m/%Y'):12}\ 
                    #precioproveedor    
                    {rep[3]:<12}\ 
                    #precioventa
                    {rep[4]:<12}\ 
                    #peso
                    {rep[5]:<12}" 
                    )
        #Si hay un error, aparecerá en pantalla:       
        except Exception as err:
            print(err)