# Crear una Api rest
from fastapi import FastAPI, HTTPException
from models import Person 

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
@app.get('')
async def show():
    pass

# TODO: Mostrar un dato en concreto: GET
@app.get('')
async def show_one():
    pass

@app.post("/insertData/")
async def insert(item:Person):

    nuevo_usuario = item.dict()
    nuevo_usuario["id"] = len(database) + 1
    database.append(nuevo_usuario)
    return nuevo_usuario


# TODO:Actualizaréis un dato del listado: PUT
@app.put("/updateData/")
async def update(item:Person):
    df= pd.database
    df.loc[df.index[-1], "id"] = item.id
    df.loc[df.index[-1], "name"] = item.name
    df.loc[df.index[-1], "age"] = item.age
    df.loc[df.index[-1], "profesion"] = item.profesion
    df.to_csv("updateData", index=False)
    return {**item.dic()}
            

# TODO:Eliminareis un dato: DELETE
@app.delete('')
async def delete_one():
    pass


@app.delete("/")
async def delete_all():
    if not database:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    
    database.clear()
    return "Todos los usuarios fueron eliminados"
