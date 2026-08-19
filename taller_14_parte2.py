
# 6. Diccionario persona con nombre, edad, carrera y ciudad

print("=== Punto 6: Diccionario persona ===")

persona = {
    "nombre": "Yimileth",
    "edad": 21,
    "carrera": "Ingeniería de Sistemas",
    "ciudad": "Barranquilla"
}

print("Información de la persona:")
print(persona)
print()


# 7. Recorrer el diccionario mostrando claves, valores y pares

print("=== Punto 7: Recorrer el diccionario ===")

print("--- Claves ---")
for clave in persona.keys():
    print(clave)

print("\n--- Valores ---")
for valor in persona.values():
    print(valor)

print("\n--- Pares clave-valor ---")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
print()



# 8. Clase Producto con nombre, precio, cantidad

print("=== Punto 8: Clase Producto ===")

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad


producto1 = Producto("Cuaderno", 3500, 10)
producto2 = Producto("Lapicero", 1200, 25)

print(f"Producto: {producto1.nombre} | Precio: {producto1.precio} | Cantidad: {producto1.cantidad}")
print(f"Valor total del inventario de {producto1.nombre}: {producto1.valor_total()}")

print(f"\nProducto: {producto2.nombre} | Precio: {producto2.precio} | Cantidad: {producto2.cantidad}")
print(f"Valor total del inventario de {producto2.nombre}: {producto2.valor_total()}")
print()


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



# 10. Lista del 1 al 10: lista completa, primer y último elemento,y cantidad de elementos
print("=== Punto 10: Lista del 1 al 10 ===")

numeros = list(range(1, 11))

print(f"Lista completa: {numeros}")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Cantidad de elementos: {len(numeros)}")
