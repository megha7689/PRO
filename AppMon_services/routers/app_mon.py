from fastapi import APIRouter, Depends, status, HTTPException, Response,Path, Query
from typing import List, Union

from  sqlalchemy.orm import Session
from ..repository import app_mon
from .. import schemas,database,models
from sqlalchemy import DateTime
from datetime import datetime
from datetime import date
from typing import Optional, Union
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate,Page, Params
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter(prefix='/app_mon',
    tags=['appmon_services'])



@router.get('/')
def show(from_date:Union[str,None]=None,to_date:Union[str,None]=None,query:Union[str,None]=None,offset: int = 0, limit: int = Query(default=100, lte=100),db: Session = Depends(database.get_db)):
    
    return app_mon.show(db,from_date,to_date,query,offset,limit)
add_pagination(router)




@router.get('/{id}', status_code = 200, response_model=schemas.ShowApp)
def showapp(id:int,response: Response,db: Session = Depends(database.get_db)):
    return app_mon.showapp(id,db)



@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.App_mon, db: Session = Depends(database.get_db)):
    
     return app_mon.create(request, db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.App_mon, db: Session = Depends(database.get_db)):
     
     return app_mon.update(id, request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(database.get_db)):
    return app_mon.delete(id, db)


# @router.get('/',response_model=LimitOffsetPage)
# def show(from_date:Union[str,None]=None,to_date:Union[str,None]=None,query:Union[str,None]=None,db: Session = Depends(database.get_db)):
   
#     return app_mon.show(db,from_date,to_date,query)
    
    
# add_pagination(router)