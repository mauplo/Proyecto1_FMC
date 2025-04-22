# Clasificador de Declaraciones de Kotlin

## Descripción

Este programa es un reconocedor y analizador de declaraciones de variables en Kotlin. Está diseñado para:

- **Identificar variables:** Detecta declaraciones realizadas con `val` (constantes) y `var` (variables).
- **Clasificar por tipo:** Agrupa las variables según su tipo (por ejemplo, `Int`, `Float`, `Double`, `String`, `Char` y distintos arreglos como `IntArray`, `FloatArray`, etc.).
- **Diferenciar inicializaciones:** Determina si las variables están inicializadas o no, y cuenta las declaraciones inicializadas.
- **Reconocer arreglos:** Identifica y clasifica arreglos y colecciones, distinguiendo entre los distintos tipos (incluyendo `arrayOf<...>`).
- **Generar estadísticas:** Al finalizar el análisis, se muestra un resumen con el número total de variables, tipos utilizados, variables inicializadas, arreglos, constantes y una clasificación de nombres por tipo.

El objetivo es automatizar el reconocimiento de estructuras válidas en Kotlin, facilitando una visión clara sobre las variables utilizadas en un archivo de código.

## Características Principales

- **Detección de constantes y variables:** Diferencia entre `val` y `var` para identificar constantes y variables.
- **Clasificación detallada:** Separa las variables por tipo (básicos y arreglos).
- **Análisis de inicialización:** Verifica y cuenta las variables que se inicializan en la declaración.
- **Interfaz amigable:** Usa una ventana emergente (Tkinter) para seleccionar el archivo de entrada.
- **Manejo de errores:** Incorpora control de excepciones durante la lectura del archivo.

## Requisitos

- **Python 3.9:** SSe necesita python 3.9 o superior por la función `def parseWhiles(tokens: list) -> tuple[int, list]:`
- **Tkinter:** Este módulo, utilizado para la interfaz gráfica, viene generalmente incluido en la instalación estándar de Python.
- **Librerías estándar:** `re` y `collections` (no se requiere instalación adicional).

## Instalación

1. **Verifica Python:** Asegúrate de tener Python 3 instalado.
2. **Comprueba Tkinter:** Ejecuta el siguiente comando para confirmar que Tkinter está disponible:
    ```bash
    python -m tkinter
    ```
    Si se abre una ventana de prueba, Tkinter está correctamente instalado.
3. **Descarga el código:** Clona o descarga el repositorio que contiene el programa.

## Cómo Ejecutarlo

1. **Abre la terminal:** Navega hasta el directorio donde se encuentra el archivo del programa (por ejemplo, `clasificador.py`).
2. **Ejecuta el programa:** Ingresa el siguiente comando en la terminal:
    ```bash
    python clasificador.py
    ```
3. **Selecciona el archivo:** Al iniciarse, se abrirá una ventana emergente solicitando seleccionar un archivo de texto (`.txt`) que contenga declaraciones de variables en Kotlin.
4. **Observa el resultado:** Una vez analizado el archivo, el programa mostrará en la terminal un resumen con:
    - Número total de variables declaradas.
    - Número total de tipos utilizados.
    - Cantidad de variables por cada tipo.
    - Número de variables inicializadas.
    - Número de variables de tipo arreglo.
    - Número total de declaraciones constantes (`val`).
    - Listado de nombres de variables agrupados por tipo.

## Ejemplos de Ejecución

### Ejemplo 1

**Entrada Kotlin:**

```kotlin
val x: Int = 10
val cadena: String = "Hola mundo"
var contador: Int
var area: Float = 10.0f
var volumen: Float
val cadena2: String = "Para el proyecto"
val arrConst: IntArray = IntArray(3)
var floatArr: FloatArray = FloatArray(10) {1.1f}
var sArr = arrayOf<String>("Hola", "es", "arreglo")
```

**Salida:**
```
Número total de variables declaradas: 9
Número total de tipos utilizados en las declaraciones encontradas: 6
Número total de variables declaradas de cada tipo:
  Int: 2
  String: 2
  Float: 2
  IntArray: 1
  FloatArray: 1
  arrayOfString: 1
Número total de variables inicializadas: 7
Número total de variables de tipo arreglo: 3
Número total de declaraciones constantes: 4

Clasificación de todos los nombres de variables por tipo declarado:
  Int: x, contador
  String: cadena, cadena2
  Float: area, volumen
  IntArray: arrConst
  FloatArray: floatArr
  arrayOfString: sArr
```

## Ejemplo 2 
**Prueba con declaraciones correctas e incorrectas:**
```
### Primero las cadenas correctas  ###
# Pruebas Int
val i1: Int=10
var i2: Int
val i3 = 0

# Pruebas Float
var f1: Float = 10.0f
var f2: Float
var f3 = 1.7f

# Pruebas Double
var d1: Double = 1.23
var d2 : Double 
var d3 =1.23

# Pruebas Char
val c1 : Char = 'M'
val c2 : Char 
val c3 = 'M'

# Pruebas String
val s1: String = "Hola mundo"
val s2: String   
val s3 = "Para el proyecto"

# Pruebas IntArray
val ia1: IntArray = IntArray(3)
val ia2: IntArray 
val ia3= IntArray (2)

# Pruebas FloatArray
var fa1: FloatArray = FloatArray(10) {2.13f}   
var fa2: FloatArray
var fa3  = FloatArray(5)

# Pruebas DoubleArray
var da1: DoubleArray = DoubleArray(10) {2.13}   
var da2: DoubleArray
var da3  = DoubleArray(4)

# Pruebas CharArray
var ca1: CharArray = CharArray(10) 
var ca2:   CharArray
var ca3  = CharArray(4)

# Pruebas arrayOfString
var aos1 = arrayOf<String>()
var aos2 = arrayOf<String>("Hola","?", "es", "arreglo")

# Pruebas arrayOfChar
var aoc1 = arrayOf<Char>( )
var aoc2 = arrayOf<Char>('o', 'w'  , '0')

# Pruebas arrayOfInt
var aoi1 =arrayOf<Int>(    )
var aoi2 =arrayOf<Int>(3,4,5)

# Pruebas arrayOfFloat
var aof1 =arrayOf<Float>(  )
var aof2 =arrayOf<Float>(3.3f,4.4f,5.5f)

# Pruebas arrayOfDouble
var aod1 =arrayOf<Double>(  )
var aod2 =arrayOf<Double>(3.34,4.4,5.51)

### Ahora las incorrectas ###
val str: Stringiri 
val x: 2
val x: In
val if: 2
val 76g = 2
var var : 
var vari able=
```


**Salida:**

```
Número total de variables declaradas: 37
Número total de tipos utilizados en las declaraciones encontradas: 14
Número total de variables declaradas de cada tipo:
Int: 3
Float: 3
Double: 3
Char: 3
String: 3
IntArray: 3
FloatArray: 3
DoubleArray: 3
CharArray: 3
arrayOfString: 2
arrayOfChar: 2
arrayOfInt: 2
arrayOfFloat: 2
arrayOfDouble: 2
Número total de variables inicializadas: 28
Número total de variables de tipo arreglo: 22
Número total de declaraciones constantes: 11

Clasificación de todos los nombres de variables por tipo declarado:
Int: i1, i2, i3
Float: f1, f2, f3
Double: d1, d2, d3
Char: c1, c2, c3
String: s1, s2, s3
IntArray: ia1, ia2, ia3
FloatArray: fa1, fa2, fa3
DoubleArray: da1, da2, da3
CharArray: ca1, ca2, ca3
arrayOfString: aos1, aos2
arrayOfChar: aoc1, aoc2
arrayOfInt: aoi1, aoi2
arrayOfFloat: aof1, aof2
arrayOfDouble: aod1, aod2

```

## Problemas Conocidos
- **Limitación de tipos**: Solo se reconocen los tipos básicos y ciertos arreglos predefinidos. No se analizan estructuras complejas, anidadas o clases completas.
- **Alcance de las declaraciones**: Se analizan únicamente declaraciones directas; por lo tanto, algunas estructuras válidas en contextos más complejos podrían no ser reconocidas.


## Detalles Técnicos y Modularización
- **Expresiones Regulares**:
Se utilizan expresiones regulares complejas para capturar las declaraciones de variables, tanto para asignaciones explícitas como implícitas. Esto permite identificar correctamente el tipo de dato, inicialización y el uso de arreglos.

- **Interfaz Gráfica con Tkinter**:
La función `carga_archivo()` utiliza Tkinter para abrir una ventana emergente que permite seleccionar el archivo de texto a analizar.

- **Manejo de Errores**:
Se han implementado bloques `try/except` para gestionar posibles errores durante la lectura del archivo, asegurando que el programa informe adecuadamente al usuario en caso de problemas.

- **Modularización**:
El código está organizado en funciones específicas:
    -  `carga_archivo()`: Gestiona la selección y lectura del archivo.
    - `analiza_archivo()`: Procesa el contenido, utiliza expresiones regulares para identificar declaraciones y genera estadísticas detalladas.


## Consideraciones Finales
- **Formato del archivo**:
El programa espera archivos de texto (.txt) con declaraciones en formato Kotlin. Asegúrate de que el contenido respete la sintaxis básica para obtener resultados precisos.

- **Ejecución en diferentes entornos**:
Dado que se utiliza Tkinter para la selección de archivos, el programa está optimizado para entornos de escritorio.

- **Ampliación del análisis**:
Actualmente, el programa se enfoca en declaraciones simples. Para proyectos más complejos, se podrían implementar mejoras para reconocer estructuras anidadas o adicionales.

# Autores 
- Axel Castro Lara – 204092
- Mauricia Peña López Ostolaza – 205688
- Emilio González Acosta – 207911
- Luis Fernando Rodríguez Retama – 208047
- Rafael Harry Gomar Dawson – 208999
