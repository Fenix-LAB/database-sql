from config.database import Base, engine, Session
from models.test_table import table_test
from schemas.schema_test import ModelTest

def post_data():
    ModelTest.c_int = 7
    ModelTest.c_float = 5.2
    ModelTest.c_str = "Hola mundo"
