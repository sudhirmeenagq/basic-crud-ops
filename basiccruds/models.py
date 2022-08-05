from sqlalchemy import TIMESTAMP, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# Create your models here.

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(100))
    mobile = Column(String(10))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


