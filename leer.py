import csv

datos = []
with open('contactos.csv', 'r') as file:
    fildnames = ('nombre', 'email')
    lector = csv.DictReader(file, fildnames)
    for row in lector:
        datos.append(row)
    print(datos)