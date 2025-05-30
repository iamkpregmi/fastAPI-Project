from .crud import *
from fastapi import APIRouter, Depends
from .schema import Document
from fastapi import APIRouter, UploadFile, File, Form
from database import SessionLocal, engine
from models import Base


router = APIRouter()

#Create Table into Database
Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/file-share', summary="Upload file & Share to anyone", description="Upload a file and save metadata to the database.")
def online_file_share(
    doc_name: str = Form(),
    doc_details: str = Form(),
    doc_created_by: str = Form(),
    file: UploadFile = File(),
    db : Session = Depends(get_db)
):
    return share(doc_name, doc_details, doc_created_by, file, db)


@router.post('/receive-file/{id}')
def receive_file(id, db : Session = Depends(get_db)):
    return receive_file_data(id, db)


@router.post('/download-file/{id}')
def receive_file(id, db : Session = Depends(get_db)):
    return download_file_data(id, db)