from sqlalchemy import Column, Integer, MetaData
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
base=declarative_base()
metadata=MetaData()

class day2(base):
    __tablename__ ="day2"
    Id = Column(Integer,primary_key=True,index=True)
    frist_name=Column("Name",NullType)
    last_name=Column("Address",NullType)
    dob=Column("DOB",NullType)

