from sqlalchemy import create_engine, MetaData
import mysql.connector
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
SQLALCHAMY_DATABASE_URL = 'mysql+mysqlconnector://root@localhost/appmon_services'

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='appmon_services'

)
engine = create_engine(SQLALCHAMY_DATABASE_URL)
meta= MetaData()
conn = engine.connect()





#engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()