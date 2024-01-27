# Definición de la función 'contar_palabras_en_archivo' que toma 'nombre_archivo' como parámetro.
def contar_palabras_en_archivo(nombre_archivo):  # Corrección: Agregar dos puntos (:) al final.
    try:
        # Intenta abrir el archivo en modo lectura.
        with open(nombre_archivo, 'r') as archivo:
            # Lee el contenido del archivo.
            contenido = archivo.read()
            # Separa el contenido en palabras.
            palabras = contenido.split()
            # Retorna el número de palabras.
            return len(palabras)
    except FileNotFoundError:
        # Retorna un mensaje si el archivo no se encuentra.
        return f"El archivo {nombre_archivo} no fue encontrado."  # Corrección: Corregir 'retunr' a 'return'.

# Solicita al usuario ingresar el nombre del archivo y lo guarda en 'archivo_nombre'.
archivo_nombre = input("Ingrese el nombre del archivo de texto: ")
# Llamada a la función 'contar_palabras_en_archivo' con 'archivo_nombre' como argumento y muestra el resultado.
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")
