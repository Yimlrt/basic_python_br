
curso = "Introducción a Python"
semestre = "2026-2"
nombre = "Yimileth"  

print("=== Punto 1: Variables básicas ===")
print(f"Curso: {curso}")
print(f"Semestre: {semestre}")
print(f"Nombre: {nombre}")
print()



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



print("=== Punto 3: Par o impar ===")
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    siguiente_par = numero + 1
    print(f"El número es impar. El siguiente número par es: {siguiente_par}")
print()



print("=== Punto 4: Números del 1 al 20 ===")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
print()



print("=== Punto 5: Función multiplicar ===")

def multiplicar(a, b):
    return a * b

a = float(input("Ingrese el primer número a multiplicar: "))
b = float(input("Ingrese el segundo número a multiplicar: "))
resultado = multiplicar(a, b)
print(f"El resultado de multiplicar {a} x {b} es: {resultado}")
