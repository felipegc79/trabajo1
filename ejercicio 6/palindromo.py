# Definición de la función 'es_palindromo' que toma un parámetro 'texto'.
def es_palindromo(texto):
    # Limpia el texto eliminando caracteres no alfanuméricos y convirtiendo a minúsculas.
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comprueba si el texto limpio es igual a su inverso
    return texto == texto[::-1]

# Solicita al usuario ingresar una palabra o frase y la guarda en 'palabra_frase'.
palabra_frase = input("Ingrese una palabra o frase: ")
# Llamada a la función 'es_palindromo' con 'palabra_frase' como argumento. 
if es_palindromo(palabra_frase):  # se agregó 'palabra_frase'
    # Imprime que la entrada es un palíndromo si la condición es verdadera.
    print(f"{palabra_frase} es un palíndromo.")
else:
    # Imprime que la entrada no es un palíndromo si la condición es falsa.
    print(f"{palabra_frase} no es un palíndromo.")
