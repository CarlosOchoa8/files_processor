from datetime import datetime

from pydantic import BaseModel, EmailStr


class FileModelBase(BaseModel):
    """Model for validate entry data of files."""
    record_id: int
    name: str
    bird_date: datetime
    amount: float
    email: EmailStr

