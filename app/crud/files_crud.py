from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBuilder
from app.models import FileModel


class CRUDFile(CRUDBuilder):
    """
    CRUD class object with default methods to Create and Read for FileModel
    """

    def create_bulk(self, db: Session, obj_in: list | dict):
        """Clean and insert data on bulky."""
        if data_existant := db.query(self.model.record_id).filter(
            self.model.record_id.in_(
                [record.record_id for record in obj_in]
                )).all():
            ids_existant = [record[0] for record in data_existant]
            obj_in = [schema for schema in obj_in if schema.record_id not in ids_existant]

        if not obj_in and data_existant:
            return HTTPException(status_code=402,
                                 detail=f"Records with id {ids_existant} already are stored.")
        try:
            if data_existant:
                super().create_bulk(db=db, obj_in=obj_in)
                return JSONResponse(status_code=200,
                                    content=f"Records with id {ids_existant} werent stored because of already exists.")

            super().create_bulk(db=db, obj_in=obj_in)
            return JSONResponse(status_code=200,
                                content="Records inserted properly.")
        except Exception as exc:
            return exc

    def get_record_by_recordid(self, record_id: int, db: Session) -> FileModel:
        """Get a record by his record id given."""
        return db.query(self.model).filter(self.model.record_id == record_id).first()


crud_file = CRUDFile(FileModel)
