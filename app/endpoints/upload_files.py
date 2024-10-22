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
    file_content = file_read.decode("utf-8")
    file_head_row = file_content.splitlines()[0]

    delimiters = [",", ";", "\t", "|"]
    delimiter_qty = {delimiter: file_head_row.count(delimiter) for delimiter in delimiters}
    delimiter = max(delimiter_qty, key=delimiter_qty.get)
    file_head_length = len(file_head_row.split(delimiter))

    schema_list = []
    for line in file_content.splitlines(delimiter)[1:]:
        line_content = line.split(delimiter)

        if len(line_content) != file_head_length:
            return f"La cantidad de datos en {line_content} no corresponde a la cantidad de columnas {file_head_row}"

        record_id=line_content[0]
        name=line_content[1].strip('"')
        bird_date=line_content[2]
        email = line_content[3].strip('"')
        amount=line_content[4]
        formatted_date = CustomDateTimeType().convert_str_to_datetime(bird_date=bird_date)

        if not formatted_date:
            return f"No se puede convertir la fecha {bird_date} al formato deseado DD-MM-YYYY o YYYY/MM/DD"

        schema_list.append(
            CsvModelBase(
                record_id=record_id,
                name=name,
                bird_date=formatted_date,
                amount=amount,
                email=email,
            )
        )
        logger.info(schema_list)
        try:
            crud_file.create_bulk(db=db, obj_in=schema_list)
            logger.info("==============TRY==============")
        except Exception as exc:
            logger.warning(f"Error intentando serializar datos del archivo: {exc}")

    return "ok"


file_router = router
