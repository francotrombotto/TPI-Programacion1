def ordenar_por_nombre(lista_paises, ascendente=True):

    lista_paises.sort(key=lambda p: p["nombre"], reverse=not ascendente)
    return lista_paises