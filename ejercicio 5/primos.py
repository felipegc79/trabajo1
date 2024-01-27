# llamar a la funcion
def es_primo(numero):  # Se añadió el ":" al final de la línea de definicion
    # condicion
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Se añadió el ":" al final de la línea
        # condicion
        if numero % i == 0: # se agregó el ":" al final de la condicion
            return False
    return True  # Se corrigió la palabra "retunr" a "return"
# solicitar al usuario que digite el limite superior
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
# creacion de la lista de los numeros primos desde 2 hasta el limite ingresado por el usuario
primos = [num for num in range(2, limite + 1) if es_primo(num)]  # Se añadió el argumento "num" a la función es_primo
# imprimir la lista de numeros primos
print("Números primos:", primos)
