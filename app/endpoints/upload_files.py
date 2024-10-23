
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.config.logging import get_logger
from app.crud import crud_file
from app.database.db import get_db
from app.schemas import FileModelBase
from app.utils.constants import fields
from app.utils.custom_datetime_type import CustomDateTimeType

router = APIRouter()
logger = get_logger()

@router.post("/", response_model=None)
async def process_file(file: UploadFile, db: Session = Depends(get_db)):
    """Upload, validate process and store a csv or txt file in db."""
    file_read = await file.read()
    file_content = file_read.decode("utf-8").strip().splitlines()

    schema_list = []
    current_record = {}
    record_lines = len(fields)

    try:
        for i, line in enumerate(file_content):
            if not line.strip():
                continue

            key, value = line.split(",", 1)
            value = value.strip().strip('"')

            if key not in fields:
                logger.warning(f"Field dont permitted: {key}. ignoring this record.")
                continue

            current_record[key] = value

            if len(current_record) == record_lines:
                if all(field in current_record for field in fields):
                    schema_list.append(FileModelBase(
                        record_id=current_record.get("ID"),
                        name=current_record.get("Nombre"),
                        bird_date=CustomDateTimeType().convert_str_to_datetime(current_record.get("Fecha Nacimiento")),
                        email=current_record.get("Email"),
                        amount=float(current_record.get("Monto") or 0)
                    ))
                else:
                    logger.warning(f"Full record ignored: {current_record}")

                current_record = {}
    except Exception as exc:
        logger.warning(f"Error processing file: {exc}")

    try:
        if not schema_list:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": f"There are not valid record to store in database: {file_content}"})

        return crud_file.create_bulk(db=db, obj_in=schema_list)
    except Exception as exc:
        logger.warning(f"Error trying to store records in database: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error trying to store records in database.") from exc

@router.get("/record/{id_record}", response_model=FileModelBase)
def get_record_by_id(id_record: int, db: Session = Depends(get_db)):
    """Get a record by his id given."""
    if record := crud_file.get_record_by_recordid(record_id=id_record, db=db):
        return record

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Record id {id_record} not founded."
        )

file_router = router
