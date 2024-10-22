import logging


logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
   "| \n[%(asctime)s]|  [%(levelname)s]    |  [%(module)s]:%(funcName)s:%(lineno)d: MSG > %(message)s"
   )

handler.setFormatter(formatter)
logger.addHandler(handler)


def get_logger() -> logging:
    """Return custom logger."""
    return logging.getLogger("logger")
