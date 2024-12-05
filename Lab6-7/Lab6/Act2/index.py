# 1. Determinar si un número es par o impar usando condicionales
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

# 2. Iterar sobre una lista de números e imprimir sus cuadrados usando un bucle for
lista_numeros = [2, 4, 6, 8, 10]

for numero in lista_numeros:
    cuadrado = numero ** 2
    print("El cuadrado de", numero, "es", cuadrado)

# 3. Bucle while para solicitar entrada hasta que se ingrese un número negativo
numero = 0
while numero >= 0:
    numero = int(input("Ingrese un número (negativo para salir): "))
    if numero >= 0:
        print("El número ingresado es positivo o cero.")
