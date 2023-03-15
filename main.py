# Crear una Api rest
from fastapi import FastAPI

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

# TODO: Mostrar un dato en concreto: GET

# TODO:Insertar un dato en es listado: POST

# TODO:Actualizaréis un dato del listado: PUT

# TODO:Eliminareis un dato: DELETE

# TODO: Eliminar todos los datos: DELETE