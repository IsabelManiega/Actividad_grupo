# Crear una Api rest
from fastapi import FastAPI, Response
import json

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

# TODO: Mostrar el listado: GET
@app.get('/datospersonales/', tags=["Users"])
async def datospersonales(response:Response):
    try:
        database1=database
        return(database1)
    
    except Exception as e:
        print("Error al cargar la informacion" % str(e))
        response.status_code = status.HTTP_404_NOT_FOUND
        return "404 NOT FOUND"   


