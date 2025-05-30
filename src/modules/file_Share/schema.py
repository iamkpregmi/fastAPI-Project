from pydantic import BaseModel


class Document(BaseModel):
    doc_name: str
    doc_details: str
    doc_created_by: str
