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
