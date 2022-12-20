from pydantic import BaseModel, Field, BaseSettings
from typing import List, Union, Optional
from datetime import datetime
import pydantic
from sqlalchemy import Enum
import enum

class App_mon(BaseModel):
    
    app_name : str = Field(..., max_length=255,regex="^[a-zA-Z][a-zA-Z0-9- _]*$") 
    app_key : str = Field(...,max_length=255,regex='^[A-Z0-9]+(?:_[A-Z0-9]+)*$')
    status : str  = "y"
    
    
    class Config():
        orm_mode=True
        schema_extra = {
            "example": {
               "app_name": "",
               "app_key":"",
                
                
            }
        }

class Status(enum.Enum):
    y = "y"
    n = "n"
    
class ShowApp(BaseModel):
    app_id: int
    app_name : str
    app_key : str
    status: enum.Enum
    date_modified : datetime
    date : datetime
    
    class Config():
        orm_mode=True
        
     

        




  



