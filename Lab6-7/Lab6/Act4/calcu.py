def calculadora():
    while True:
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese su opción (1-5): ")

        if opcion == '5':
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
        elif opcion == '2':
            resultado = num1 - num2
        elif opcion == '3':
            resultado = num1 * num2
        elif opcion == '4':
            if num2 == 0:
                print("No se puede dividir por cero.")
            else:
                resultado = num1 / num2
        else:
            print("Opción inválida.")

        print("Resultado:", resultado)

calculadora()
