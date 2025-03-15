# Proyecto1_FMC
Este proyecto consiste en un reconocedor de declaraciones de variables del lenguaje de programación Kotlin.

## Funcionalidad

El archivo main.py define una función `carga_archivo` que hace lo siguiente:

1. Crea la ventana de una aplicación usando el paquete de python `tkinter`.
2. Abre el archivo mediante una ventana de selección con `filedialog.askopenfilename()`,  permitiendo que el usuario escoja. 
3. Si el archivo es seleccionado:
    * Abre el archivo 
    * Lee los contenidos y lo guarda en una variable
    * Imprime los contenidos en la consola
    * Regresa el contenido como un string.
4. Si el archivo no es seleccionado:
    * Imprime "No file selected." en la consola.
    * Regresa `None`.

## Uso

1. Correr el archivo main.py en una IDE como Visual Code (evitar jupyter o collab)
2. Un dialogo para la selección de un archivo aparecerá.
3. Escoger el archivoque se quiere leer y picar "Open"/"Abrir"
4. The contents of the file will be printed to the console.
5. The file contents are also returned by the `carga_archivo` function, which can be used for further processing in your code.

## Ejemplo
