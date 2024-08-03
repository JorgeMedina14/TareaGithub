import math

def area_circulo_v3(radio):
    try:
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        return math.pi * (radio ** 2)
    except TypeError:
        print("El radio debe ser un número.")

# Ejemplo de uso
radio = -5
area = area_circulo_v3(radio)
print(f"Versión 3: El área del círculo con radio {radio} es {area}")
