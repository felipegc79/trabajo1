# llamar a la funcion
def celsius_a_fahrenheit(celsius):  # Se agregó el caracter : al final de la línea
    # Devolver el resultado de la operación 
    return (celsius * 9/5) + 32  # se añadió el símbolo + para realizar la suma

# Solicitar al usuario que ingrese la temperatura en Celsius y convertir a float
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))  # Se agrego el input

# Llamar a la función y guardar el resultado en la variable temperatura_fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Imprimir el resultado
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
