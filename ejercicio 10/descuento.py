# Definición de la función 'calcular_precio_con_descuento' y dos puntos al final.
def calcular_precio_con_descuento(precio_base, porcentaje_descuento):  # Corrección: Agregar paréntesis y dos puntos.
    # Calcula el valor del descuento.
    descuento = precio_base * (porcentaje_descuento / 100)
    # Calcula el precio final después de aplicar el descuento.
    precio_final = precio_base - descuento
    # Retorna el precio final.
    return precio_final  # Corrección: Corregir 'retunr' a 'return'.

# Solicita al usuario ingresar el precio base del producto y lo guarda en 'precio_base'.
# Corrección: Asegurarse de que la función 'input' esté presente para capturar la entrada del usuario.
precio_base = float(input("Ingrese el precio base del producto: "))  # Corrección aquí

# Solicita al usuario ingresar el porcentaje de descuento y lo guarda en 'porcentaje_descuento'.
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Llamada a la función 'calcular_precio_con_descuento' con los argumentos 'precio_base' y 'porcentaje_descuento'.
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)

# Muestra el precio final después de aplicar el descuento.
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
