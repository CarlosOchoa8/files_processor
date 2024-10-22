from typing import Generator

from app.database.base_class import SessionLocal

def get_db() -> Generator:
    """Get a DB session

    Yields:
        Generator: A sessionmaker instance
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
