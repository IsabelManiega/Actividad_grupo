# Crear una Api rest
from fastapi import FastAPI, HTTPException, Response, status
from models import Person
import pandas as pd

tags_metadata=[
    {
        "name": "Test",
        "description": "Bienvenida",
        
        
        
    },
    {
        "name": "Users",
        "description": "Muestra la gestión de los usuarios",
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

@app.get('/TEST/', tags=["Test"])
async def TEST():
    return "Bienvenido al ejercicio de Datos personales"


@app.get('/datospersonales/', tags=["Users"])
async def datospersonales(response:Response):
    try:
        return database
    
    except Exception as e:
        print("Error al cargar la informacion" % str(e))
        response.status_code = status.HTTP_404_NOT_FOUND
        return "404 NOT FOUND"   

@app.post("/insertData/")
async def insert(item:Person):

    nuevo_usuario = item.dict()
    nuevo_usuario["id"] = len(database) + 1
    database.append(nuevo_usuario)
    return nuevo_usuario


@app.put("/updateData/{item_id}", tags=["Users"])
async def update(item_id: int, item: Person):
    try:
        for value in database:
            if value['id'] == item_id:
                value['name'] == item.name
                value['age'] == item.age
                value['profesion'] == item.profesion
         return {{item_id}, **item.dic()}
    except:
        return "404 NOT FOUND"


            

# TODO:Eliminareis un dato: DELETE
@app.delete('')
async def delete_one():
    pass


@app.delete("/", tags=["Users]"])
async def delete_all():
    if not database:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    
    database.clear()
    return "Todos los usuarios fueron eliminados"
