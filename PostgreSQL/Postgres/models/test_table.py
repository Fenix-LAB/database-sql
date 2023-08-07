from config.database import Base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Float)

class table_test(Base):
    __tablename__ = "test postgres"

    id = Column(Integer, primary_key=True, autoincrement=True)
    column_str = Column(String)
    column_int = Column(Integer)
    column_float = Column(Float)