from config.database import Base, engine, Session
from models.test_table import table_test

"""
ORM: ORM (Object Relational Mapping o Mapeo Objeto-Relacional en castellano) 
es una herramienta que nos permite mapear, o lo que es lo mismo, 
convertir los objetos de tu aplicación a un formato adecuado 
para ser almacenados en cualquier base de datos.

CRUD: CRUD es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y 
Delete (Borrar). Este concepto se utiliza para describir
las cuatro operaciones básicas que pueden realizarse en la mayoría
de las bases de datos y sistemas de gestión de información.

"""

def post_data(c_str: str, c_int: int, c_float: float):
    """
    Función para insertar datos en la base de datos

    """

    db = Session() # Crear una sesión con la base de datos
    new_data = table_test(column_str=c_str, column_int=c_int, column_float=c_float) # Crear una instancia de la clase modelo
    db.add(new_data) # Añadir la instancia a la sesión
    db.commit() # Confirmar los cambios para que se guarden en la base de datos

def get_all_data():
    """
    Función para consultar todos los datos de la base de datos

    """
    
    db = Session() # Crear una sesión con la base de datos
    data = db.query(table_test).all() # Consultar todos los datos de la tabla
    print(f'Datos obtenidos: {data}') # Imprimir los datos

def get_data_by_id(id: int):
    """
    Función para consultar un dato de la base de datos

    """
    
    db = Session() # Crear una sesión con la base de datos
    data = db.query(table_test).filter(table_test.id == id).first() # Consultar todos los datos de la tabla
    print(f'Dato obtenido: {data}') # Imprimir el dato

def update_data(id: int, c_str: str, c_int: int, c_float: float):
    """
    Función para actualizar un campo de la base de datos

    """

    db = Session() # Crear una sesión con la base de datos
    data = db.query(table_test).filter(table_test.id == id).first() # Consultar el dato de la tabla
    
    if not data: # Si no existe el dato
        print("No existe el dato") # Imprimir un mensaje
    if data:
        pass
        # TODO Actualizar el dato
        # print(f'Dato obtenido: {data}')
        # data.column_str = c_str # Actualizar el dato
        # data.column_int = c_int # Actualizar el dato
        # data.column_float = c_float # Actualizar el dato
        # db.commit() # Confirmar los cambios para que se guarden en la base de datos
        # print(f'Dato actualizado: {data}') # Imprimir el dato

if __name__ == "__main__":
    # En este momento se puede consultar la base de datos en postgres y verificar que se creó la tabla
    Base.metadata.create_all(bind=engine) # Crear la base de datos
    post_data("chris", 9, 9.5) # Insertar datos en la base de datos
    get_all_data() # Consultar todos los datos de la base de datos
    get_data_by_id(1) # Consultar undato de la base de datos
    # update_data(1, "chris", 10, 10.0) # Actualizar un dato de la base de datos