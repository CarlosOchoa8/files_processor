from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from app.config.logging import get_logger
from app.database.db import get_db
from app.schemas import CsvModelBase
from app.utils.custom_datetime_type import CustomDateTimeType
from app.crud import crud_file

router = APIRouter()
logger = get_logger()

@router.post("/", response_model=None)
async def process_file(file: UploadFile, db: Session = Depends(get_db)):
    """Upload, validate process and store a csv or txt file in db."""
    file_read = await file.read()
    file_content = file_read.decode("utf-8").strip().splitlines()

    schema_list = []
    current_record = {}
    for line in file_content:
        if not line.strip():
            continue

        key, value = line.split(",", 1)

        value = value.strip().strip('"')

        if key in current_record:
            if len(current_record) == 5:
                schema_list.append(CsvModelBase(
                    record_id=current_record.get("ID"),
                    name=current_record.get("Nombre"),
                    bird_date=CustomDateTimeType().convert_str_to_datetime(current_record.get("Fecha")),
                    email=current_record.get("Email"),
                    amount=float(current_record.get("Monto"))
                ))
                current_record = {}

        current_record[key] = value

    if current_record:
        schema_list.append(CsvModelBase(
            record_id=current_record.get("ID"),
            name=current_record.get("Nombre"),
            bird_date=CustomDateTimeType().convert_str_to_datetime(current_record.get("Fecha")),
            email=current_record.get("Email"),
            amount=float(current_record.get("Monto"))
        ))

    try:
        return crud_file.create_bulk(db=db, obj_in=schema_list)
    except Exception as exc:
        logger.warning(f"Error intentando serializar datos del archivo: {exc}")



file_router = router
