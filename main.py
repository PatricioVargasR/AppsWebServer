"""
    Actividades (TODO):
        read contactos.csv
        JSON enconde contactos.csv
        save in response
"""
#from fastapi import FastAPI
from fastapi import FastAPI, status # Importa la variable de estados
import csv

app = FastAPI()

# @app.get("/") # Asignación predeterminada
# @app.get("/", status_code=202) # Asignación sin librería, solo poniendo el número
# @app.get("/", status_code=status.HTTP_200_OK) # Asignación a través de la libreria, permitiendo desplegar opciones de código
# Agrega una descripción y resumen en la documentación
"""
@app.get(
        "/",
        status_code=status.HTTP_200_OK,
        description="Endpoint raíz de la API Contactos",
        summary="Endpoint raíz"
         )
"""
@app.get("/", status_code=status.HTTP_200_OK, summary="Endpoint raíz")
def read_root():
# async def root(): # Convierte la función en asincrona
# Agregamos documentación  
    """
    # Endpoint raíz
    
    ## 1- Status codes:
    * 200 - Código de confirmación
    * 289 - Código de muestra
    * 334 - Otro código de muestra
    """
    return {"Hello":"World"}

@app.get("/v1/contactos")
# async def get_contactos()
def get_contactos():
    datos = []
    with open('contactos.csv', 'r') as file:
        # fildnames = ('nombre', 'email')
        # lector = csv.DictReader(file, fildnames)
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos
