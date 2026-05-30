def ordenar_por_nombre(lista_paises, ascendente=True):

    lista_paises.sort(key=lambda p: p["nombre"], reverse=not ascendente)
    return lista_paises

def ordenar_por_poblacion(lista_paises, ascendente=True):
    # Usamos la misma lógica, pero ahora el 'key' apunta a "poblacion".
    lista_paises.sort(key=lambda p: p["poblacion"], reverse=not ascendente)
    return lista_paises