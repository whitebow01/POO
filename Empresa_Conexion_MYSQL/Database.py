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
    

    