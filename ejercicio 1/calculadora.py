# definir la funcion
def calculadora():
    # guardar un valor tipo float
    num1 = float(input("Ingrese el primer número: ")) # convertir el string en float agregando un input
    # guardar un valor tipo float
    num2 = float(input("Ingrese el segundo número: ")) # convertir el string en float agregando un input
    # escoger una operacion matematica suma, resta, multiplicacion o division
    operacion = input("Ingrese la operación (+, -, *, /): ")
    # condicion si el usuario escoge +
    if operacion == '+':
        #operacion si se cumple la condicion
        resultado = num1 + num2 # falta colocar el 1
    # condicion si el usuario escoge -
    elif operacion == '-':
        #operacion si se cumple la condicion
        resultado = num1 - num2
    # condicion si el usuario escoge *
    elif operacion == '*':
        #operacion si se cumple la condicion
        resultado = num1 * num2
    # condicion si el usuario escoge /
    elif operacion == '/':
        #operacion si se cumple la condicion
        resultado = num1 / num2 # falta colocar el 1
    # sino se cumple ninguna condicion anterior entonces escribir el mensaje
    else:
        resultado = "Operación no válida"
    # imprimir el resultado de la opracion matematica
    print(resultado) # quitar los caracteres Resultado:  

calculadora() # a esta funcion le falta un caracter para quedar igual que el inicio del ejercicio
