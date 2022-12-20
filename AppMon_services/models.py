from .database import Base
from pydantic import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Enum,Date, TIMESTAMP, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

class Status(enum.Enum):
    y = "y"
    n = "n"
    

    

class App_master(Base):
    __tablename__='app_master'
    
    app_id = Column(Integer,primary_key = True)
    app_name = Column(String(255))
    app_key = Column(String(255))
    status = Column(Enum(Status),default=Status.y)
    date_modified = Column(DateTime(timezone=True),server_default=func.now(),onupdate = func.now())
    date = Column(DateTime(timezone=True), server_default=func.now())

    



 

