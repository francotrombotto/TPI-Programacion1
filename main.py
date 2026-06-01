
from funciones.archivos import (cargar_paises,guardar_paises)
from funciones.paises import (mostrar_paises,agregar_pais,buscar_pais,actualizar_pais)

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
        mostrar_paises(paises)
    elif opcion == "2":
        agregar_pais(paises)
        guardar_paises("datos/paises.csv",paises)
    elif opcion == "3":
        buscar_pais(paises)
    elif opcion == "4":
        submenu_filtros(paises)  
    elif opcion == "5":
        submenu_ordenamientos(paises)  
    elif opcion == "6":
        submenu_estadisticas(paises) 
    elif opcion == "7":
        actualizar_pais(paises)
        guardar_paises("datos/paises.csv",paises) 
    elif opcion == "0":
        print("\nCerrando programa...")
        break
    else:
        print("\n⚠️ Opción inválida.")
