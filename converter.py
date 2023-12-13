def convertir_base(numero, base_origen, base_destino):
    if base_origen < 2 or base_destino < 2:
        return "Las bases deben ser mayores o iguales a 2."

    # Convertir a decimal primero
    decimal = 0
    exp = 0
    for digito in reversed(str(numero)):
        decimal += int(digito) * (base_origen ** exp)
        exp += 1

    # Convertir a la base de destino
    resultado = ""
    while decimal > 0:
        resto = decimal % base_destino
        resultado = str(resto) + resultado
        decimal //= base_destino

    return resultado

# Solicitar entrada al usuario
numero = input("Ingrese el número a convertir: ")
base_origen = int(input("Ingrese la base de origen (entero mayor o igual a 2): "))
base_destino = int(input("Ingrese la base de destino (entero mayor o igual a 2): "))

# Llamar a la función con los valores proporcionados por el usuario
resultado = convertir_base(numero, base_origen, base_destino)

# Imprimir el resultado
print(f"El resultado de convertir {numero} de base {base_origen} a base {base_destino} es: {resultado}")
