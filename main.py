from Calculadora import *


def menu():
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo...")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida, intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: debes ingresar números válidos.")
            continue

        if opcion == "1":
            print(f"El resultado es {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"El resultado es {restar(num1, num2)}")
        elif opcion == "3":
            print(f"El resultado es {multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"El resultado es {dividir(num1, num2)}")


if __name__ == "__main__":
    menu()
