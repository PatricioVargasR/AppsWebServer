from fastapi import FastAPI # Importamos el módulo FastAPI
from pydantic import BaseModel # Importamos el módulo BaseModel

# Creamos una plantilla
class Item(BaseModel):
    name: str # Variable de tipo str
    description: str | None = None # Variable que puede aceptar str o ser none
    price: float # Variable del tipo flotante
    tax: float | None = None # Variable del tipo flotante o none

# Variable que usará para iniciar el código
app = FastAPI()

# Declaramos ruta con URI
@app.post("/items/")
# Función asincrona que recibirá la plantilla de la clase
async def create_item(item: Item):
    # Asignamos los items de forma diccionario
    item_dict = item.dict()
    # En caso de que el tax exista
    if item.tax:
        # Se declara un nuevo precio con la suma del tax
        price_with_tax = item.price + item.tax
        # Actualiza el item de precio  con la variable anterior
        item_dict.update({"price_with_tax": price_with_tax})
    # Regresa los item de diccionario   
    return item_dict
