### main.py ###
# Uso:
# 1. Ejecutar el script.
# 2. Seleccionar un archivo .txt con las declaraciones cuando aparezca la ventana.
# 3. El script mostrará los resultados en la terminal.

# Autores: Axel Castro Lara                 204092
#          Mauricia Peña López Ostolaza     205688
#          Emilio González Acosta           207911
#          Luis Fernando Rodríguez Retama   208047
#          Rafael Harry Gomar Dawson        208999

### IMPORTACIÓN DE PAQUETES ###
import re  # Importar paquete para manejo de expresiones regulares
import tkinter as tk  # Importar y renombrar paquete para la GUI
from tkinter import filedialog  # Importa módulo para la selección de archivos
from collections import defaultdict  # Importa módulo para contar los tipos de variables y evitar KeyErrors

# definimos las palabras reservadas en Kotlin que no queremos que se usen como nombre
reservadas = (
    "var|val|typealias|as|is|in|if|else|when|for|while|do|return|continue|break|"
    "fun|class|interface|object|constructor|this|super|public|private|protected|"
    "internal|final|open|override|abstract|sealed"
)

## Modularización de posibles finales para las cadenas de la ER ##

# caracteres aceptados para un String
esStr = r"[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\w\s]"
# inicializar un Int
inI = r"\s*=\s*\d*"
# inicializar un Float
inF = r"\s*=\s*\d*\.\d+(f)"
# inicializar un Double
inD = r"\s*=\s*\d*(\.)\d+"
# inicializar un Char
inC = r"\s*=\s*'\w(')"
# inicializar un String
inS = rf'\s*=\s*"{esStr}*(")'
# inicializar un IntArray
inIA = r"\s*=\s*(IntArray)\s*\(\s*\d+\s*\)"
# inicializar un FloatArray
inFA = r"\s*=\s*(FloatArray)\s*\(\s*\d+\s*\)(?:\s*\{\s*\d*\.\d+f\s*\})?"
# inicializar un DoubleArray
inDA = r"\s*=\s*(DoubleArray)\s*\(\s*\d+\s*\)(?:\s*\{\s*\d*\.\d+\s*\})?"
# inicializar un CharArray
inCA = r"\s*=\s*(CharArray)\s*\(\s*\d+\s*\)"
# inicializar un arrayOf<String>
inAoS = rf'(String)\s*>\s*\((?:\s*"{esStr}*"(?:\s*,\s*"{esStr}*")*)?\s*\)'
# inicializar un arrayOf<Char>
inAoC = r"(Char)\s*>\s*\((?:\s*'\w'(?:\s*,\s*'\w')*)?\s*\)"
# inicializar un arrayOf<Int>
inAoI = r"(Int)\s*>\s*\((?:\s*\d*(?:\s*,\s*\d*)*)?\s*\)"
# inicializar un arrayOf<Float>
inAoF = r"(Float)\s*>\s*\((?:\s*\d*\.\d+f(?:\s*,\s*\d*\.\d+f)*)?\s*\)"
# inicializar un arrayOf<Double>
inAoD = r"(Double)\s*>\s*\((?:\s*\d*\.\d+(?:\s*,\s*\d*\.\d+)*)?\s*\)"
# inicializar cualquier arrayOf
inAoX = rf"\s*=\s*(arrayOf)\s*<\s*(?:{inAoS}|{inAoC}|{inAoI}|{inAoF}|{inAoD})"
# inicializar directamente algún tipo de dato
inX = rf"(?:{inI}|{inF}|{inD}|{inC}|{inS}|{inIA}|{inFA}|{inDA}|{inCA}|{inAoX})"

# declarar Int
deI = rf"(Int)(?:{inI})?"
# declarar Float
deF = rf"(Float)(?:{inF})?"
# declarar Double
deD = rf"(Double)(?:{inD})?"
# declarar Char
deC = rf"(Char)(?:{inC})?"
# declarar String
deS = rf"(String)(?:{inS})?"
# declarar IntArray
deIA = rf"(IntArray)(?:{inIA})?"
# declarar FloatArray
deFA = rf"(FloatArray)(?:{inFA})?"
# declarar DoubleArray
deDA = rf"(DoubleArray)(?:{inDA})?"
# declarar CharArray
deCA = rf"(CharArray)(?:{inCA})?"
# declarar algún tipo de dato
deX = rf"\s*:\s*(?:{deI}|{deF}|{deD}|{deC}|{deS}|{deIA}|{deFA}|{deDA}|{deCA})"

## Expresión regular para capturar las declaraciones de variables ##
er = rf"^[;\s]*(val|var)\s+((?!\b(?:{reservadas})\b)[a-zA-Z_]\w*)(?:{inX}|{deX})[;\s]*$"
er_compilada = re.compile(er)  # se compila la expresión regular

### DEFINICIÓN DE LA EXPRESIÓN REGULAR ###
#
#    Expresión regular para encontrar declaraciones de variables en Kotlin
#    (^|\n|\s*;\s*)                       # Puede comenzar con ; o salto de línea o espacio, después permite espacios
#    (val|var)\s+                         # Requiere una declaración (val o var), y un espacio después
#    ((?!\b({reservadas})\b)[a-zA-Z_]\w*)   # Nombre de la var: evita palabras reservadas y empieza con letra/guión
#    inX                                  # Reconoce una asignación directa de un dato básico, arrayOf o (Int|Float|Double)Array
#    deX                                  # Reconoce una declaración de un dato básico o tipo array
#

### CARGA_ARCHIVO: función para cargar el archivo a evaluar ###
def carga_archivo():
    ventana = tk.Tk()  # creamos la ventana principal de la "aplicación" para la UI
    ventana.withdraw()  # no queremos enseñar la ventana, sólo el diálogo que pide el archivo
    path_archivo = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )  # abre el diálogo para archivo .txt y lo asigna a un path
    if path_archivo:  # si el usuario seleccionó un archivo
        try:
            with open(path_archivo, "r") as archivo:  # abre el archivo seleccionado para leerlo (r)
                contenido = archivo.read()  # lee el archivo
                return contenido  # la función regresa el contenido
        except Exception as e:
            print(f"Error leyendo archivo: {e}")  # manejamos errores potenciales al seleccionar el archivo
            return None  # la función regresa None
    else:  # el usuario no seleccionó el archivo
        print("No se seleccionó un archivo.")
        return None  # la función regresa None


indicesTipoExplicito = [16] + list(range(17, 32, 2))
indicesArrayOf = range(11, 16)
indicesTipoImplicito = range(6, 10)


def analiza_archivo():
    ### DECLARACIÓN DE VARIABLES ###
    """
    Uno de los propósitos del código es contar las instancias de diferentes tipos de variables.
    Para eso, se necesitan variables para guardar la cantidad y nombres de los tipos.
    variables: arreglo con los nombres de los tipos de variables.
    contador_tipos: diccionario para contar cuántas instancias hay de cada tipo.
    categorias_tipos: diccionario para categorizar las variables por tipo (Int, Float, String, etc).
    cont_inicializadas: contador de variables inicializadas.
    cont_arreglo: contador de variables tipo arreglo.
    cont_constantes: contador de variables constantes.
    """
    variables = []
    contador_tipos = defaultdict(int)
    categorias_tipos = defaultdict(list)
    cont_inicializadas = 0
    cont_arreglo = 0
    cont_constantes = 0

    ### EXTRACCIÓN DE DECLARACIONES ###
    contenido = carga_archivo()  # pedimos un archivo para analizar
    print(contenido)

    if contenido:  # si el usuario ingresó un archivo (caso contrario sería None)
        # se separan las declaraciones de texto usando RegEx
        for linea in re.split(r"(\r\n|\r|\n|;)+", contenido):
            aceptacion = er_compilada.match(linea)

            # analizamos cada declaración válida
            if aceptacion:
                # en los grupos hay muchos marcadores sobre el tipo de dato de la declaración
                marcadores = aceptacion.groups()

                # si el tipo de declaración es val, por como es Kotlin sabemos que es constante
                tipo_dec = marcadores[0]
                if re.match(r"val", tipo_dec):
                    cont_constantes += 1

                # añade el nombre de cada declaración a la lista
                nombre = marcadores[1]
                variables.append(nombre)

                # revisamos si hubo inicialización
                if re.match(r".*=.*", linea):
                    cont_inicializadas += 1

                # se busca si se declaró el tipo de dato de forma explícita
                tipo_var = None
                for i in indicesTipoExplicito:
                    if marcadores[i]:
                        tipo_var = marcadores[i]

                if not tipo_var:
                    # si no se encontró un tipo explícito, primero se busca si es un 'arrayOf'
                    if marcadores[10]:
                        # si es un arrayOf, se busca el tipo de datos del arreglo
                        for i in indicesArrayOf:
                            if marcadores[i]:
                                tipo_var = marcadores[10] + marcadores[i]
                    # si no es arrayOf, se determina el tipo de dato de forma implícita
                    else:
                        # los marcadores del 2 al 5 son de Float, Double, Char y String, respectivamente
                        if marcadores[2]:
                            tipo_var = "Float"
                        elif marcadores[3]:
                            tipo_var = "Double"
                        elif marcadores[4]:
                            tipo_var = "Char"
                        elif marcadores[5]:
                            tipo_var = "String"
                        # el resto de marcadores de tipo implícito ya son el nombre del tipo de dato
                        else:
                            for i in indicesTipoImplicito:
                                if marcadores[i]:
                                    tipo_var = marcadores[i]
                        # si no hay marcador de tipo implícito que no sea None, el tipo es necesariamente Int
                        if not tipo_var:
                            tipo_var = "Int"

                # se añade la variable a su grupo de tipos de dato
                categorias_tipos[tipo_var].append(nombre)
                contador_tipos[tipo_var] += 1

                # revisamos si el tipo es un arreglo
                if re.match(r".*[aA]rray", tipo_var):
                    cont_arreglo += 1

        ### IMPRESIÓN DE RESULTADOS ###
        print(f"Número total de variables declaradas: {len(variables)}")
        print(f"Número total de tipos utilizados en las declaraciones encontradas: {len(contador_tipos)}")
        print("Número total de variables declaradas de cada tipo:")
        for nombre_tipo, contador_tipo in contador_tipos.items():
            print(f"{nombre_tipo}: {contador_tipo}")
        print(f"Número total de variables inicializadas: {cont_inicializadas}")
        print(f"Número total de variables de tipo arreglo: {cont_arreglo}")
        print(f"Número total de declaraciones constantes: {cont_constantes}")
        print("\nClasificación de todos los nombres de variables por tipo declarado:")
        for var_tipo, var_nombres in categorias_tipos.items():
            print(f"{var_tipo}: {', '.join(var_nombres)}")


### EJECUCIÓN ###
if __name__ == "__main__":
    analiza_archivo()
