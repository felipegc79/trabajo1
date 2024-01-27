# Definición de la función 'factorial' con un parametro n
def factorial(n):  # Corrección: Agregar dos puntos (:) al final.
    # Comprueba si n es igual a 0 o 1.
    if n == 0 or n == 1:  # Corrección: Cambiar '=' a '==' en la segunda condición.
        # Retorna 1 si la condición es verdadera.
        return 1  # Corrección: Corregir 'retunr' a 'return'.
    else:
        # Retorna el producto de n y el factorial de n-1 si la condición es falsa
        return n * factorial(n - 1)  # Corrección: Corregir 'retunr' a 'return'.

# Solicita al usuario ingresar un número y lo guarda en 'numero'.
numero = int(input("Ingrese un número para calcular su factorial: "))
# Llamada a la función 'factorial' con 'numero' como argumento y muestra el resultado.
print(f"El factorial de {numero} es {factorial(numero)}")  # Corrección: pasar 'numero' como argumento.
