# devuelve los países que coincidan con el continente ingresado
def filtrar_por_continente(lista_paises, continente):

    filtrados = []

    for pais in lista_paises:

        if pais["continente"].strip().lower() == continente.strip().lower():

            filtrados.append(pais)

    return filtrados

# devuelve los países cuya población esté dentro del rango indicado
def filtrar_por_poblacion(lista_paises, minimo, maximo):

    filtrados = []

    for pais in lista_paises:

        # verifica que la población esté dentro del rango
        if minimo <= pais["poblacion"] <= maximo:

            filtrados.append(pais)

    return filtrados


# devuelve los países cuya superficie esté dentro del rango indicado
def filtrar_por_superficie(lista_paises, minimo, maximo):

    filtrados = []

    for pais in lista_paises:

        # verifica que la superficie esté dentro del rango
        if minimo <= pais["superficie"] <= maximo:

            filtrados.append(pais)

    return filtrados