from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import os
import shutil
from models import MasterDocuments
from fastapi import HTTPException, status
import base64
from fastapi.responses import FileResponse


def share(doc_name, doc_details, doc_created_by, file, db):
    os.makedirs("assets", exist_ok=True)
    file_location = f"assets/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_data = MasterDocuments(doc_name = doc_name, doc_details = doc_details, doc_created_by= doc_created_by, doc_path=file.filename)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully!"
    })


def receive_file_data(id, db):

    file_data = db.query(MasterDocuments).filter(MasterDocuments.doc_id == id).first()

    if not file_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Data not found of {id}.')

    file_path = os.path.join("assets", file_data.doc_path)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on disk.")

    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")

    context = {
        "doc_id": file_data.doc_id,
        "doc_name": file_data.doc_name,
        "doc_details": file_data.doc_details,
        "doc_created_by": file_data.doc_created_by,
        "doc_created_at": file_data.doc_created_at,
        "doc_base64": encoded_string
    }

    return context


def download_file_data(id, db):
    file_data = db.query(MasterDocuments).filter(MasterDocuments.doc_id == id).first()

    if not file_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Data not found for ID {id}.')

    file_path = os.path.join("assets", file_data.doc_path)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on disk.")

    return FileResponse(
        path=file_path,
        media_type="application/octet-stream",
        filename=file_data.doc_path,
    )
