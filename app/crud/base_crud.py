from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session
from app.config.logging import get_logger
from fastapi import HTTPException

logger = get_logger()

class CRUDBuilder:
    def __init__(self, model):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Args:

        `model`: A SQLAlchemy model class
        `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def create(self, db: Session, obj_in: dict | dict[str, Any]):
        """Create a ModelType object"""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_bulk(self, db: Session, obj_in: list | dict):
        """Create a ModelType object"""
        logger.info("CREATE BULK1===============================")
        try:
            if not isinstance(obj_in[0], dict):
                obj_in = [schema.dict() for schema in obj_in]

            bulk_insert = insert(self.model).values(obj_in)
            bulk_insert_on_ignore = bulk_insert.on_conflict_do_nothing()
            db.execute(bulk_insert_on_ignore)
            db.commit()
            return True
        except Exception as exc:
            db.rollback()
            logger.error(f"Error insertando en la base de datos: {exc}")
            raise HTTPException(
                status_code=400,
                detail=f"Error insertando en la base de datos: {exc}"
            ) from exc

    def get(self, id: int, db: Session):
        return db.query(self.model).filter(self.model.id == id).first()
