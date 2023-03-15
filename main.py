# Crear una Api rest
from fastapi import FastAPI, HTTPexception
from models import User 
tags_metadata=[
    {
        "name": "TEST",
        "description": "Bienvenida",
    },
    {
        "name": "Users",
        "description": "Muestra los gestión de los usuarios",
    },
]

app = FastAPI(title="DataScience Course",
              openapi_tags=tags_metadata,
              contact={"name": "Isabel Maniega",
                       "url": "https://es.linkedin.com/in/isabel-maniega-cuadrado-40a8356b",
                       "email": "isabelmaniega@hotmail.com",
                },
              openapi_url="/api/v0.1/openapi.json")



# Crear un listado:
database = [{"id": 1, "name": "Juan Perez", "age": 25, "profesion": "Ingeniero"},
            {"id": 2, "name": "Susana Ruiz", "age": 45, "profesion": "Profesora"}]

# TODO: Mostrar el listado: GET
@app.get()
async def show():
    pass

# TODO: Mostrar un dato en concreto: GET
@app.get()
async def show_one():
    pass

# TODO:Insertar un dato en es listado: POST
@app.post("/insertData/")
async def insert(item:User):

    nuevo_usuario = item.dict()
    nuevo_usuario["id"] = len(database) + 1
    database.append(nuevo_usuario)
    return nuevo_usuario
    
    pass

# TODO:Actualizaréis un dato del listado: PUT
@app.put()
async def update():
    pass

# TODO:Eliminareis un dato: DELETE
@app.delete()
async def delete_one():
    pass

# TODO: Eliminar todos los datos: DELETE
@app.delete("/")
async def delete_all():
    if not database:
        raise HTTPexception(status_code=404, detail="No hay usuarios")
    
    database.clear()
    return "Todos los usuarios fueron eliminados"

