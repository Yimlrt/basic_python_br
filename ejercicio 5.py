
# 5. Función multiplicar(a, b)
print("=== Punto 5: Función multiplicar ===")

def multiplicar(a, b):
    return a * b

a = float(input("Ingrese el primer número a multiplicar: "))
b = float(input("Ingrese el segundo número a multiplicar: "))
resultado = multiplicar(a, b)
print(f"El resultado de multiplicar {a} x {b} es: {resultado}")
