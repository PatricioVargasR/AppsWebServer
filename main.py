"""
    BaseModel: Nos ayudará a crear una plantilla para nuestros parámetros de envio
    datetime: Nos ayudará a obtener la fecha y hora actual en que se ejecuta el método
"""
#from fastapi import FastAPI
from fastapi import FastAPI, status # Importa la variable de estados
from pydantic import BaseModel # Importamos el módulo Base model de pydantic
# from typing import Optional
from datetime import datetime # Importamo el módulo datetime
import csv # Importamos el módulo csv para trabajar con archivos

# Creamos la variable de arranque
app = FastAPI()

# Creamos una clase modelo
class Post(BaseModel):
    nombre: str
    email: str

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

@app.get("/v1/contactos", status_code=status.HTTP_200_OK, summary="Endpoint para listar datos")
def get_contactos():
    """
    # Endpoint para obtener datos de la API

    ## 1.- Status codes:
    * 200 - Código de confirmación
    """
    datos = []
    with open('contactos.csv', 'r') as file:
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos

# Forma 1

# @app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
# def add_contactos(nombre:str, email:str):
    """
    # Endpoint para enviar datos de la API

    ## 1.- Status codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * nombre: str
    * email: str
    """
#    with open('contactos.csv', 'a', newline="") as file:
#        fieldnames = ["nombre", "email"]
#        writer = csv.DictWriter(file, fieldnames=fieldnames)
#        row = {"nombre": nombre, "email": email}  #  Uso de diccionario
#        writer.writerow(row)
#    return row, {"datetime":datetime.now()}  # Mensaje de confirmación


# Forma 2
@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
# 
def add_contactos(post:Post):
    # Agrega la descripición correspondiente
    """
    # Endpoint para enviar datos de la API

    ## 1.- Status codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * nombre: str
    * email: str
    """
    with open('contactos.csv', 'a', newline="") as file:
        fieldnames = ["nombre", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = post.dict() # Uso de diccionario
        writer.writerow(row)
    return row, {"datetime":datetime.now()} # Mensaje de confirmación
