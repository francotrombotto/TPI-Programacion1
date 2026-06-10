# TPI Programación 1 - Gestión de Datos de Países

## Integrantes

* Franco Trombotto
* Sofía Odello

## Materia

Programación 1

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación de consola en Python para la gestión de información de países.

El sistema permite cargar datos desde un archivo CSV y realizar distintas operaciones sobre ellos, como búsquedas, filtros, ordenamientos y generación de estadísticas.

El objetivo principal es aplicar los conceptos vistos durante la cursada de Programación 1, utilizando listas, diccionarios, funciones, estructuras de control y manejo de archivos.

---

## Estructura del Proyecto

```text
TPI-Programacion1/
│
├── datos/
│   └── paises.csv
│
├── funciones/
│   ├── archivos.py
│   ├── filtros.py
│   ├── ordenamientos.py
│   ├── estadisticas.py
│   ├── paises.py
│   └── submenus.py
│
├── main.py
└── README.md
```

---

## Funcionalidades Implementadas

### Gestión de Países

* Mostrar todos los países cargados.
* Agregar nuevos países.
* Buscar países por nombre.
* Actualizar población y superficie de un país existente.

### Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

### Ordenamientos

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Orden ascendente y descendente.

### Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

### Persistencia de Datos

* Lectura de información desde archivo CSV.
* Guardado automático de cambios realizados.

---

## Tecnologías Utilizadas

* Python 3
* CSV (Comma Separated Values)
* GitHub
* GitHub Desktop
* Visual Studio Code

---

## Requisitos

Tener instalado:

* Python 3.x

Verificar instalación:

```bash
python --version
```

---

## Ejecución del Programa

Ubicarse en la carpeta raíz del proyecto y ejecutar:

```bash
python main.py
```

---

## Dataset

El programa utiliza un archivo CSV llamado:

```text
datos/paises.csv
```

Formato esperado:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Alemania,83149300,357022,Europa
Japon,125800000,377975,Asia
```

---

## Conceptos Aplicados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos vistos en la materia:

* Variables
* Listas
* Diccionarios
* Funciones
* Estructuras condicionales
* Estructuras repetitivas
* Modularización
* Lectura y escritura de archivos CSV
* Validación de datos
* Ordenamiento de registros
* Estadísticas básicas

---

## Repositorio

Repositorio GitHub:

https://github.com/francotrombotto/TPI-Programacion1

---

## Video Demostración

Video del funcionamiento del sistema:

https://youtu.be/gvRFR_gCbm8

---

## Conclusión

Este trabajo permitió poner en práctica los principales conceptos de Programación 1 mediante el desarrollo de una aplicación funcional basada en el manejo de datos de países. Además, se trabajó de forma colaborativa utilizando Git y GitHub para el control de versiones y la integración del código.
