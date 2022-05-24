#Creating the table

from sqlalchemy import MetaData, Table, Column, String, Text, Boolean, create_engine, Integer
from datetime import datetime

engine = create_engine("mysql+mysqldb://root:animeshroot@123@localhost/internship")

metadata = MetaData()

blog = Table('blog', metadata,
    Column('id', Integer(), primary_key= True),
    Column('post_title', String(200), nullable= False),
    Column('post_slug', String(200), nullable= False),
    Column('content', Text(), default= False),
    Column('published', Boolean(), default= True),
)

print(engine)