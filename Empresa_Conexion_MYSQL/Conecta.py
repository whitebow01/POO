# Contiene la creación de un objeto de conexión a la base de datos
# y ejecución de los métodos de la clase

from Database import *

db = Database()
db.select_todos()
db.cerrarBD()