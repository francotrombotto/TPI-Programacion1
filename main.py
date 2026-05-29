from funciones.archivos import cargar_paises
from funciones.filtros import filtrar_por_continente

# cargamos los datos del csv al iniciar el programa
paises = cargar_paises("datos/paises.csv")


def mostrar_menu():

    print("\n===== MENU PRINCIPAL =====")
    print("1 - Mostrar países")
    print("2 - Agregar país")
    print("3 - Buscar país")
    print("0 - Salir")


# bucle principal del programa
while True:

    mostrar_menu()

    opcion = input("\nElegí una opción: ")

    # muestra todos los países cargados
    if opcion == "1":

        for pais in paises:

            print("\n------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

    elif opcion == "2":

        print("\nAcá después vamos a agregar países")

    elif opcion == "3":

        continente = input("Ingresá continente: ")

        resultado = filtrar_por_continente(paises, continente)

        print(resultado)
        
    elif opcion == "0":

        print("\nCerrando programa...")
        break

    else:

        print("\nOpción inválida")

