from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Photos(Base):
    __tablename__= 'Photos'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    op=Column(String)
    image=Column(String)
    description=Column(String)
    timeuploaded=Column(DateTime)
    location=Column(String)
    imagesizeratio=Column(Float)

    def __repr__(self):
        return "Name: {} \n Original Poster: {} \n Image: {} \n Description: {} \n Time of upload: {} \n Ratio:{} \n".format(self.name,self.op,self.image,self.description,self.timeuploaded, self.location, self.imagesizeratio)

