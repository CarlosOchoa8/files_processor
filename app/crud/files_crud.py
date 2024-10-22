from app.crud.base_crud import CRUDBuilder
from app.models import FileModel

class CRUDFile(CRUDBuilder):
    """
    CRUD class object with default methods to Create and Read for FileModel
    """


crud_file = CRUDFile(FileModel)
