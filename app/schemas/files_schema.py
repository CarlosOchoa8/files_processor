from datetime import datetime

from pydantic import BaseModel, EmailStr


class CsvModelBase(BaseModel):
    """Model for validate entry data of .csv files."""
    record_id: int
    name: str
    bird_date: datetime
    amount: float
    email: EmailStr


class CsvCreateModel(CsvModelBase):
    """Create class model"""


class CsvUpdateModel(CsvModelBase):
    """Create class model"""


class TxtModelBase(BaseModel):
    """Model for validate entry data of .txt files."""
    record_id = int
    name: str
    bird_date: datetime
    amount: float
    email: EmailStr
