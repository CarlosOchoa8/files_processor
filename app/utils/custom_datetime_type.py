from datetime import datetime

from app.config.logging import get_logger

logger = get_logger()


class CustomDateTimeType:
    _date_formats = [
        "%Y/%m/%d",
        "%d-%m-%Y",
    ]

    @classmethod
    def convert_str_to_datetime(cls, bird_date: str) -> datetime:
        """Convert a given string datetime into object datetime on allowed formats."""
        for fmt in cls._date_formats:
            try:
                date_object = datetime.strptime(bird_date, fmt)
                logger.info(f"Cadfena de fecha {bird_date} convertida a objeto datetime: {date_object}")
                return date_object
            except ValueError as ve:
                logger.error(f"No se puede convertir la fecha {bird_date} al formato deseado: {ve}")
                continue
        
        logger.error(f"No se pudo convertir la fecha: {bird_date}")
        return None
