from pydantic import BaseModel

# TODO: insertar el modelo de datos
class Person(BaseModel):
    id: int
    name: str
    age: int
    profesion: str