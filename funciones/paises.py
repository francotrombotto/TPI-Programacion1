# muestra todos los países cargados
def mostrar_paises(lista_paises):

    # verifica que haya datos para mostrar
    if len(lista_paises) == 0:
        print("\nNo hay países cargados")
        return

    # recorre la lista completa
    for pais in lista_paises:

        print("\n------------------------")
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# permite agregar un nuevo país a la lista
def agregar_pais(lista_paises):

    nombre = input("Ingrese el nombre del país: ").strip()

    #valida duplicados
    for pais in lista_paises:

        if pais["nombre"].lower() == nombre.lower():

            print("\nEse país ya existe")

            return

    # evita que el nombre quede vacío
    if nombre == "":
        print("\nEl nombre no puede estar vacío")
        return

    try:

        poblacion = int(input("Ingrese la población: "))
        superficie = int(input("Ingrese la superficie: "))

    except ValueError:

        print("\nDebe ingresar números válidos")
        return

    continente = input("Ingrese el continente: ").strip()

    if continente == "":
        print("\nEl continente no puede estar vacío")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)

    print("\nPaís agregado correctamente")


# busca países por nombre
def buscar_pais(lista_paises):

    texto = input("Ingrese el nombre a buscar: ").strip().lower()
    
    #Valida que no se pueda hacer una búsqueda vacía
    if texto == "":

        print("\nDebe ingresar un nombre")

        return

    encontrados = []

    # busca coincidencias parciales
    for pais in lista_paises:

        if texto in pais["nombre"].lower():

            encontrados.append(pais)

    if len(encontrados) == 0:

        print("\nNo se encontraron resultados")

        return

    print("\nResultados encontrados:")

    for pais in encontrados:

        print("\n------------------------")
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# actualiza población y superficie de un país
def actualizar_pais(lista_paises):

    nombre = input("Ingrese el país a modificar: ").strip().lower()

    for pais in lista_paises:

        if pais["nombre"].lower() == nombre:

            try:

                nueva_poblacion = int(
                    input("Nueva población: ")
                )

                nueva_superficie = int(
                    input("Nueva superficie: ")
                )

            except ValueError:

                print("\nDebe ingresar números válidos")
                return

            # evita valores negativos o cero
            if nueva_poblacion <= 0:

                print("\nLa población debe ser mayor a cero")
                return

            if nueva_superficie <= 0:

                print("\nLa superficie debe ser mayor a cero")
                return

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("\nDatos actualizados correctamente")

            return

    print("\nNo se encontró el país indicado")