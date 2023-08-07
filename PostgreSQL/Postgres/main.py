from config.database import Base, engine, Session
from models.test_table import table_test
from schemas.schema_test import ModelTest

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

def post_data():
    ModelTest.c_int = 7
    ModelTest.c_float = 5.2
    ModelTest.c_str = "Hola mundo"

    print(ModelTest.model_dump())

    db = Session()
    new_data = table_test(**ModelTest.model_dump())
    db.add(new_data)
    db.commit()


if __name__ == "__main__":
    # En este momento se puede consultar la base de datos en postgres y verificar que se creó la tabla
    Base.metadata.create_all(bind=engine) # Crear la base de datos
    post_data()