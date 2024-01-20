#llama a la funcion 
def contar_palabra(texto, palabra): #falta colocar el caracter :
    #devolver 
    return texto.lower().split().count(palabra.lower())
#mostrar el mensaje
texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
#variable de tipo string
palabra_buscada = "texto"
#imprimir el mensaje concatenado
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") #faltaba cerrar la llave y comilla simple de la variable palabra_buscada y abrir la llave en la funcion contar_palabra
