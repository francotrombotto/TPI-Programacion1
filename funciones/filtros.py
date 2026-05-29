# devuelve los países que coincidan con el continente ingresado
def filtrar_por_continente(lista_paises, continente):

    filtrados = []

    for pais in lista_paises:

        if pais["continente"].strip().lower() == continente.strip().lower():

            filtrados.append(pais)

    return filtrados