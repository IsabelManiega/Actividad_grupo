from pydantic import BaseModel

# TODO: insertar el modelo de datos
class User(BaseModel):
    "id": float  # no estoy segura si se pone o se obtiene automaticamente
    "name": str
    "age": float
    "profesion": str