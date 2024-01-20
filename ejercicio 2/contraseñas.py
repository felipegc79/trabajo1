#libreria de aleatoriedad
import random # falta el caracter m
#libreria de texto
import string
#define una funcion llamada generar_contrasena que toma un argumento (longitud) con un valor predeterminado
def generar_contrasena(longitud=8): #se corrigió el nombre y se agregó el tipo de parametro
    #Crea una cadena de caracteres que contiene letras mayusculas y minusculas
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #Genera una contraseña aleatoria usando la funcion random.choice
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    #Devuelve la contraseña creada por la funcion
    return contraseña # palabra return mal escrita
#imprime la contraseña generada
print(generar_contrasena())
