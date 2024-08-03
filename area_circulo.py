import math
from typing import Union

def area_circulo_v4(radio: Union[int, float]) -> float:
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

# Ejemplo de uso
radio = 5
area = area_circulo_v4(radio)
print(f"Versión 4: El área del círculo con radio {radio} es {area}")
