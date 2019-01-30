from model import *
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_content(name,op,image,description, location, timeuploaded):
    photograph=Photos(name=name,op=op,image=image,description=description, location=location,  timeuploaded=timeuploaded)
    session.add(photograph)
    session.commit()

def delete_content(id):
    session.query(Photos).filter_by(id=id).delete()
    session.commit()

def query_by_photos():
    photos=session.query(Photos).all()
    photos.reverse()
    return photos


def get_content_id(timeuploaded):
    item = session.query(Photos).filter_by(timeuploaded=timeuploaded).first()
    return item.id 


def change_content_image(img_id, img_url, ratio=None):
    item = session.query(Photos).filter_by(id=img_id).first()
    item.image = img_url
    if ratio:
        item.imagesizeratio = ratio
    session.commit()


def touch(filename):
    if not os.path.exists(filename):
        return 
    else:
        try:
            os.utime(filename, None)
        except OSError:
            open(filename, 'a').close()

def query_ratio():
    photos=session.query(Photos).all()
    print(photos)
    photos.sort(key=(lambda x: x.imagesizeratio))
    return photos


