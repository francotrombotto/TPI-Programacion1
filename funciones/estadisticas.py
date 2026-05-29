def obtener_pais_max_poblacion(lista_paises):
    # Validación: Si la lista está vacía, no se puede buscar. Retornamos None para evitar errores.
    if not lista_paises: return None
    
    # Inicialización: Suponemos que el primer país es el que tiene más población.
    # Usamos esta variable como punto de referencia para comparar con el resto.
    pais_max = lista_paises[0]
    
    # Recorrido: Iteramos por cada país de la lista.
    for pais in lista_paises:
        # Comparación: Si el país actual supera en población al que teníamos guardado,
        # actualizamos nuestra referencia (pais_max) con el nuevo país.
        if pais["poblacion"] > pais_max["poblacion"]:
            pais_max = pais
    return pais_max

def obtener_pais_min_poblacion(lista_paises):
    # Lógica idéntica al máximo, pero invertimos la condición de comparación (<).
    if not lista_paises: return None
    pais_min = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] < pais_min["poblacion"]:
            pais_min = pais
    return pais_min

def calcular_promedio_poblacion(lista_paises):
    # Validación: Evitamos la división por cero si la lista está vacía.
    if not lista_paises: return 0
    
    # Acumulación: Usamos una 'comprensión de generador' para sumar las poblaciones
    # de todos los países. Es más eficiente y legible que un bucle tradicional.
    total = sum(p["poblacion"] for p in lista_paises)
    
    # Cálculo: Dividimos la suma total por la cantidad de elementos (len).
    return total / len(lista_paises)

def calcular_promedio_superficie(lista_paises):
    # Misma lógica que el promedio de población, aplicada a la superficie.
    if not lista_paises: return 0
    total = sum(p["superficie"] for p in lista_paises)
    return total / len(lista_paises)