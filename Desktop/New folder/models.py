from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, MetaData, column
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

class person(base):
    __tablename__="table_person"
    person_id = Column(Integer,primary_key = True, index = True)
    person_username = Column('username',NullType)
    person_password = Column('password',NullType)
    person_email = Column('email',NullType)
    blog_id = Column('blog_id',NullType)

    
