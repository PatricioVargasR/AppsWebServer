from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/")
def read_root():
# async def root(): # Convierte la función en asincrona
    return {"Hello":"World"}

@app.get("/v1/contactos")
def get_contactos():
    datos = []
    with open('contactos.csv', 'r') as file:
        # fildnames = ('nombre', 'email')
        # lector = csv.DictReader(file, fildnames)
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos

    # TODO read contactos.csv
    # TODO JSON enconde contactos.csv
    # TODO save in response