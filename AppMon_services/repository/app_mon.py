from sqlalchemy.orm import Session
from .. import models, schemas,database
from fastapi import HTTPException, status, Query
from sqlalchemy import DateTime,values,select
import datetime
from datetime import datetime

from sqlalchemy import or_, func
from typing import Optional, Union
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from ..database import SessionLocal, engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi_pagination import  paginate
import json

def show(db: Session,from_date:Union[str,None]=None,to_date:Union[str,None]=None,query:Union[str,None]=None,offset: int = 0, limit: int = Query(default=100, lte=100)):
      
      Q = models.App_master
      apps = db.query(Q)
      
      dt_str=dt_str1=None
      try:
        if from_date:
            dt_obj = datetime.strptime(from_date,'%Y-%m-%d %H:%M:%S')
            dt_str = datetime.strftime(dt_obj,'%Y-%m-%d %H:%M:%S')
        if to_date:
            dt_obj1 = datetime.strptime(to_date,'%Y-%m-%d %H:%M:%S')
            dt_str1 = datetime.strftime(dt_obj1,'%Y-%m-%d %H:%M:%S')
      except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Date should be in format %Y-%m-%d %H:%M:%S')
      if query:
            apps=apps.filter(or_(Q.app_name.contains(query),(Q.app_key.contains(query))))
      
     
      
      if dt_str and dt_str1:
            apps = apps.filter(Q.date.between(dt_str,dt_str1))
      rows = apps.count()
      if dt_str:
            apps = apps.filter(Q.date.between(dt_str,datetime.now()))
      rows = apps.count()
      if dt_str1:
            apps = apps.filter(Q.date <= dt_str1)
      rows = apps.count()
      
      rows = apps.filter(Q.status == "y").count()
     
      apps=apps.filter(Q.status =="y").limit(limit).offset(offset).all()
      
      apps1 =jsonable_encoder((apps))
      
      return JSONResponse({'status':'success','error_code': 0,'total records':rows, 'data':apps1,'from_date':dt_str,'to_date':dt_str1,'limit':limit,'offset':offset})
      



def showapp(id: int,db:Session):
    app = db.query(models.App_master).filter(models.App_master.app_id == id).first()
    if not app:
         return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=f'App with id {id} not available',
        )
    return app

def create(request: schemas.App_mon, db: Session):
   
    
    new_app = models.App_master(app_name=request.app_name,app_key=request.app_key)
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    
    return JSONResponse(status_code=201, content={"message": "Application details stored successfully"})

def update(id:int,request: schemas.App_mon,db: Session):
    app = db.query(models.App_master).filter(models.App_master.app_id == id)
    
    if not app.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'app with id {id} not found')
    app.update(request.dict())
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Application details updated successfully"})

   

def delete(id:int, db: Session):
    app = db.query(models.App_master).filter(models.App_master.app_id ==id)
    

    if not app.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'App with id {id} not found')
    app.update({models.App_master.status:"n"})
    db.commit()
    return 'done'







