
from funciones.archivos import cargar_paises

from funciones.submenus import (
    mostrar_menu, 
    submenu_filtros, 
    submenu_ordenamientos, 
    submenu_estadisticas
)

# cargamos los datos del csv al iniciar el programa
paises = cargar_paises("datos/paises.csv")

while True:
    mostrar_menu()
    opcion = input("\nElegí una opción: ").strip()

    if opcion == "1":
        print("\n-> Módulo en construcción: Mostrar países")
    elif opcion == "2":
        print("\n-> Módulo en construcción: Agregar país")
    elif opcion == "3":
        print("\n-> Módulo en construcción: Actualizar país")
    elif opcion == "4":
        submenu_filtros(paises)  
    elif opcion == "5":
        submenu_ordenamientos(paises)  
    elif opcion == "6":
        submenu_estadisticas(paises)  
    elif opcion == "0":
        print("\nCerrando programa...")
        break
    else:
        print("\n⚠️ Opción inválida.")
