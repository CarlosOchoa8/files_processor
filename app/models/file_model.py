from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database.base_class import Base


class FileModel(Base):
    """File model to store data from .csv/.txt"""
    __tablename__ = "files_record"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    bird_date = Column(DateTime(), nullable=False)
    email = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
