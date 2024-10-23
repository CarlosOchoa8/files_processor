from datetime import datetime

from app.config.logging import get_logger

logger = get_logger()


class CustomDateTimeType:
    _date_formats = [
        "%Y/%m/%d",
        "%d-%m-%Y",
    ]

    @classmethod
    def convert_str_to_datetime(cls, bird_date: str) -> datetime | None:
        """Convert a given string datetime into the standard format YYYY-MM-DD."""
        for fmt in cls._date_formats:
            try:
                date_object = datetime.strptime(bird_date, fmt)
                standard_date = date_object.strftime("%Y-%m-%d")  # Convert to desired format
                logger.info(f"Date string {bird_date} converted to datetime object: {standard_date}")
                return standard_date
            except ValueError as ve:
                logger.error(f"Cannot convert date {bird_date} to the desired format: {ve}")
                continue

        logger.error(f"Failed to convert date: {bird_date}")
        return None
