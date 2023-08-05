from pydantic import BaseModel
from typing import List


class ModelTest(BaseModel):
    c_str: str
    c_int: int
    c_float: float
