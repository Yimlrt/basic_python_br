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
