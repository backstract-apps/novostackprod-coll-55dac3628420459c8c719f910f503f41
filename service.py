from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_user(db: Session):

    user_all = db.query(models.User).all()
    res = {
        'user_all': user_all,
    }
    return res

async def get_user_id(db: Session, id: int):

    user_one = db.query(models.User).filter(models.User.id == id).first()
    res = {
        'user_one': user_one,
    }
    return res

async def post_user(db: Session, id: int, address: str, fullname: str, age: str, email: str):

    record_to_be_added = {'id': id, 'address': address, 'fullname': id, 'age': id, 'email': email}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_inserted_record = new_user

    user = db.query(models.User).filter(models.User.id == id).first()

    users = db.query(models.User).filter(models.User.id == id).first()
    res = {
        'user_inserted_record': user_inserted_record,
    }
    return res

async def put_user_id(db: Session, id: str, address: str, fullname: str, age: str, email: str):

    user_edited_record = db.query(models.User).filter(models.User.id == id).first()
    for key, value in {'id': id, 'address': address, 'fullname': fullname, 'age': age, 'email': email}.items():
          setattr(user_edited_record, key, value)
    db.commit()
    db.refresh(user_edited_record)
    user_edited_record = user_edited_record

    res = {
        'user_edited_record': user_edited_record,
    }
    return res

async def delete_user_id(db: Session, id: int):

    user_deleted = None
    record_to_delete = db.query(models.User).filter(models.User.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          user_deleted = record_to_delete
    res = {
        'user_deleted': user_deleted,
    }
    return res

