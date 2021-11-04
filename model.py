'''
We will use this Base class we created before to create the SQLAlchemy models.
'''

# create model attribute/column
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from sql_app.database import Base
from sqlalchemy.orm import relationship

class PeopleInfo(Base):
    __tablename__ = "humanInfo"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=30))
    height = Column(Float)
    weight = Column(Float)
    habbit = Column(String(length=252))
