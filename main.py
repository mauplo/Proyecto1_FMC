### IMPORTACIÓN DE PAQUETES ###
import re # Importar paquete para manejo de expresiones regulares
import tkinter as tk # Importar y renombrar paquete para la GUI 
from tkinter import filedialog # Importa módulo para la selección de archivos

### CARGA_ARCHIVO: función para cargar el archivo a evaluar ###
def carga_archivo():
    ventana = tk.Tk()   # creamos la ventana principal de la "aplicación" para la UI
    ventana.withdraw()  # no queremos enseñar la ventana, sólo el diálogo que pide el archivo
    path_archivo = filedialog.askopenfilename() # abre el diálogo para el archivo y lo asigna a un path
    if path_archivo: # si el usuario seleccionó un archivo
        try: 
            with open(path_archivo, 'r') as archivo: # abre el archivo seleccionado para leerlo (r)
                contenido = archivo.read() # lee el archivo
                return contenido #la función regresa el contenido 
        except Exception as e:
            print(f"Error reading file: {e}") # manejamos eorrres potenciales al seleccionar el archivo
            return None # la función regresa None
    else: # el usuario no seleccionó el archivo
        print("No se seleccionó un archivo.") #Imprimimos en la consola que no hay archivo para analizar
        return None # la función regresa None

# Pedimos archivo a evaluar
file_contents = carga_archivo()
if file_contents:
    print('yep')
    #pass 
