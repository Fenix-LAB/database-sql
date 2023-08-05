# from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

host = "localhost"
port = "5432"
user = "postgres"
password = "password"
db_name = "test_database"

POSTGRES_SQL_CONNECTION = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

try:
    engine = create_engine(POSTGRES_SQL_CONNECTION, echo=True)
    print("Conection succesfully")
except Exception as ex:
    print("Could Not connect to Database %s", ex)

meta = MetaData()

Base = declarative_base()

Session = sessionmaker(bind=engine)

print("Ready to work")