from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user/')
async def get_user(db: Session = Depends(get_db)):
    return await service.get_user(db)

@router.get('/user/id')
async def get_user_id( id: int , db: Session = Depends(get_db)):
    return await service.get_user_id(db , id)

@router.post('/user/')
async def post_user( id: int, address: str, fullname: str, age: str, email: str , db: Session = Depends(get_db)):
    return await service.post_user(db , id, address, fullname, age, email)

@router.put('/user/id/')
async def put_user_id( id: str, address: str, fullname: str, age: str, email: str , db: Session = Depends(get_db)):
    return await service.put_user_id(db , id, address, fullname, age, email)

@router.delete('/user/id')
async def delete_user_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_user_id(db , id)

