# class to instance varify type
'''
To avoid confusion between the SQLAlchemy models and the Pydantic models, 
we will have the file models.py with the SQLAlchemy models, 
and the file schemas.py with the Pydantic models.

These Pydantic models define more or less a "schema" (a valid data shape).
So this will help us avoiding confusion while using both.
'''

from typing import List
from pydantic import BaseModel

class PeopleBase(BaseModel):
    name: str
    height: float
    weight: float
    habbit: str

class PeopleUpdate(PeopleBase):
    id: int

    class Config:
        orm_mode = True

class PeopleType(BaseModel):
    skip: int
    limit: int
    data: List[PeopleUpdate]
