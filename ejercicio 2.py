# 2. Solicitar dos números y mostrar operaciones básicas
print("=== Punto 2: Operaciones aritméticas ===")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Indefinido (división por cero)"
division_entera = num1 // num2 if num2 != 0 else "Indefinido (división por cero)"
modulo = num1 % num2 if num2 != 0 else "Indefinido (división por cero)"
potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")
print()
