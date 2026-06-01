from funciones.filtros import (filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie)
from funciones.estadisticas import (obtener_pais_max_poblacion,obtener_pais_min_poblacion,calcular_promedio_poblacion,calcular_promedio_superficie,contar_paises_por_continente)
from funciones.ordenamiento import (ordenar_por_nombre,ordenar_por_poblacion,ordenar_por_superficie)

def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Mostrar países")
    print("2 - Agregar país")
    print("3 - Buscar país")
    print("4 - Filtros")
    print("5 - Ordenamientos")
    print("6 - Estadísticas")
    print("7 - Actualizar país")
    print("0 - Salir")


def submenu_filtros(lista_paises):
    while True:
        print("\n--- FILTROS ---")
        print("1 - Por continente")
        print("2 - Por rango de población")
        print("3 - Por rango de superficie")
        print("0 - Volver")

        opcion_str = input("\nIngrese una opción del submenú: ").strip()
        
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            
            if opcion == 1:
                # Pedimos el dato
                continente_input = input("\nIngrese el nombre del continente: ").strip()
                
                #Llamamos a la función
                resultados = filtrar_por_continente(lista_paises, continente_input)
                
                #Mostramos los resultados
                if len(resultados) > 0:
                    print(f"\nSe encontraron {len(resultados)} países en {continente_input.capitalize()}:")
                    for p in resultados:
                        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km2")
                else:
                    print(f"\nNo se encontraron países para el continente '{continente_input}'.")
            elif opcion == 2:
                # Pedimos los rangos y validamos que sean números
                min_str = input("\nIngrese la población mínima: ").strip()
                max_str = input("Ingrese la población máxima: ").strip()
                
                if min_str.isdigit() and max_str.isdigit():
                    minimo = int(min_str)
                    maximo = int(max_str)
                    
                    # Llamamos a la función
                    resultados = filtrar_por_poblacion(lista_paises, minimo, maximo)
                    
                    # Mostramos los resultados
                    if len(resultados) > 0:
                        print(f"\nPaíses con población entre {minimo} y {maximo}:")
                        for p in resultados:
                            print(f"- {p['nombre']} | Población: {p['poblacion']}")
                    else:
                        print("\nNo se encontraron países en ese rango de población.")
                else:
                    print("\nError: Los rangos deben ser números enteros válidos.")
            elif opcion == 3:
                #Pedimos los rangos y validamos
                min_str = input("\nIngrese la superficie mínima (km2): ").strip()
                max_str = input("Ingrese la superficie máxima (km2): ").strip()
                
                if min_str.isdigit() and max_str.isdigit():
                    minimo = int(min_str)
                    maximo = int(max_str)
                    
                    #Llamamos a la función
                    resultados = filtrar_por_superficie(lista_paises, minimo, maximo)
                    
                    #Mostramos los resultados
                    if len(resultados) > 0:
                        print(f"\nPaíses con superficie entre {minimo} y {maximo} km2:")
                        for p in resultados:
                            print(f"- {p['nombre']} | Superficie: {p['superficie']} km2")
                    else:
                        print("\nNo se encontraron países en ese rango de superficie.")
                else:
                    print("\nError: Los rangos deben ser números enteros válidos.")
            elif opcion == 0:
                print("\nVolviendo al menú principal...")
                break 
            else:
                print("\nError: Por favor, ingrese un número del 0 al 3.")
        else:
            print("\nError: Entrada inválida. Ingrese solo números enteros.")

def submenu_ordenamientos(lista_paises):
    while True:
        print("\n--- SUBMENÚ: ORDENAMIENTOS ---")
        print("1 - Ordenar por nombre")
        print("2 - Ordenar por población")
        print("3 - Ordenar por superficie")
        print("0 - Volver")
        
        opcion_str = input("\nIngrese una opción: ").strip()
        
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            
            if opcion in [1, 2, 3]:
                # Preguntamos el sentido del orden
                sentido = input("¿Orden ascendente? (s/n): ").lower()
                es_ascendente = (sentido == 's')
                
                # Ejecutamos la función
                if opcion == 1:
                    ordenar_por_nombre(lista_paises, es_ascendente)
                elif opcion == 2:
                    ordenar_por_poblacion(lista_paises, es_ascendente)
                elif opcion == 3:
                    ordenar_por_superficie(lista_paises, es_ascendente)
                
                # Mostramos la lista ordenada
                print("\nLista ordenada:")
                for p in lista_paises:
                    print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km2")
                    
            elif opcion == 0:
                break
            else:
                print("\nError: Ingrese una opción válida.")
        else:
            print("\nError: Ingrese solo números.")


def submenu_estadisticas(lista_paises):
    while True:
        print("\n--- SUBMENÚ: ESTADÍSTICAS ---")
        print("1 - País con mayor población")
        print("2 - País con menor población")
        print("3 - Promedio de población")
        print("4 - Promedio de superficie")
        print("5 - Cantidad de países por continente")
        print("0 - Volver al Menú Principal")
        
        opcion_str = input("\nIngrese una opción del submenú: ").strip()
        
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            
            if opcion == 1:
                pais = obtener_pais_max_poblacion(lista_paises)
                print(f"\nEl país con mayor población es: {pais['nombre']} ({pais['poblacion']})")
            elif opcion == 2:
                pais = obtener_pais_min_poblacion(lista_paises)
                print(f"\nEl país con menor población es: {pais['nombre']} ({pais['poblacion']})")
            elif opcion == 3:
                prom = calcular_promedio_poblacion(lista_paises)
                print(f"\nEl promedio de población es: {prom:.2f}")
            elif opcion == 4:
                prom = calcular_promedio_superficie(lista_paises)
                print(f"\nEl promedio de superficie es: {prom:.2f} km2")
            elif opcion == 5:
                conteo = contar_paises_por_continente(lista_paises)
                print("\nCantidad de países por continente:")
                for cont, cant in conteo.items():
                    print(f"- {cont}: {cant}")
            elif opcion == 0:
                print("\nVolviendo al menú principal...")
                break # Rompe el bucle y regresa al menú principal
            else:
                print("\nError: Por favor, ingrese un número del 0 al 5.")
        else:
            print("\nError: Entrada inválida. Ingrese solo números enteros.")