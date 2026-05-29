def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Mostrar países")
    print("2 - Agregar país")
    print("3 - Buscar país")
    print("4 - Filtros")
    print("5 - Ordenamientos")
    print("6 - Estadísticas")
    print("0 - Salir")


def submenu_filtros(lista_paises):
    while True:
        print("\n--- FILTROS ---")
        print("1 - Por continente")
        print("2 - Por rango de población")
        print("3 - Por rango de superficie")
        print("0 - Volver")

        # Todo este bloque de abajo DEBE tener sangría para pertenecer al while True
        opcion_str = input("\nIngrese una opción del submenú: ").strip()
        
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            
            if opcion == 1:
                print("\n-> Módulo en construcción: Filtrar por continente")
            elif opcion == 2:
                print("\n-> Módulo en construcción: Filtrar por población")
            elif opcion == 3:
                print("\n-> Módulo en construcción: Filtrar por superficie")
            elif opcion == 0:
                print("\nVolviendo al menú principal...")
                break # Ahora Python sí sabe que este break debe romper el while de arriba
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
        print("0 - Volver al Menú Principal")
        
        opcion_str = input("\nIngrese una opción del submenú: ").strip()
        
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            
            if opcion == 1:
                print("\n-> Módulo en construcción: Ordenar por nombre")
            elif opcion == 2:
                print("\n-> Módulo en construcción: Ordenar por población")
            elif opcion == 3:
                print("\n-> Módulo en construcción: Ordenar por superficie")
            elif opcion == 0:
                print("\nVolviendo al menú principal...")
                break # Rompe el bucle y regresa al menú principal
            else:
                print("\nError: Por favor, ingrese un número del 0 al 3.")
        else:
            print("\nError: Entrada inválida. Ingrese solo números enteros.")

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
                print("\n-> Módulo en construcción: País con mayor población")
            elif opcion == 2:
                print("\n-> Módulo en construcción: País con menor población")
            elif opcion == 3:
                print("\n-> Módulo en construcción: Promedio de población")
            elif opcion == 4:
                print("\n-> Módulo en construcción: Promedio de superficie")
            elif opcion == 5:
                print("\n-> Módulo en construcción: Cantidad de países por continente")
            elif opcion == 0:
                print("\nVolviendo al menú principal...")
                break # Rompe el bucle y regresa al menú principal
            else:
                print("\nError: Por favor, ingrese un número del 0 al 5.")
        else:
            print("\nError: Entrada inválida. Ingrese solo números enteros.")