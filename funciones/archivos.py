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

import csv

# guarda la lista actual de países en el csv
def guardar_paises(ruta, lista_paises):

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pais in lista_paises:
            escritor.writerow(pais)