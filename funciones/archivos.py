import csv

def cargar_paises(ruta):

    paises = []

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("Error: archivo no encontrado")

    return paises