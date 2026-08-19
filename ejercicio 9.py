# 9. División con try/except (división por cero o entrada inválida)

print("=== Punto 9: División con manejo de errores ===")

try:
    numero1 = float(input("Ingrese el numerador: "))
    numero2 = float(input("Ingrese el denominador: "))
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
except ValueError:
    print("Error: debe ingresar un número válido.")
print()
