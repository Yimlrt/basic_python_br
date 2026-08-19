# 3. Solicitar un número entero y validar si es par o impar
print("=== Punto 3: Par o impar ===")
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    siguiente_par = numero + 1
    print(f"El número es impar. El siguiente número par es: {siguiente_par}")
print()
