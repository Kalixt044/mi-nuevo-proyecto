import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Adivina un número entre 1 y 100.")

    while True:
        intentos += 1
        intento = int(input("Tu intento: "))

        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

juego_adivinanza()

