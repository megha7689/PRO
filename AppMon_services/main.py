from fastapi import FastAPI, Request
from .import schemas, models
from .database import engine
from .routers import app_mon
import time

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(app_mon.router)


