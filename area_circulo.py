import math
from typing import Union

def area_circulo_v5(radio: Union[int, float] = 1) -> float:
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo. Debe ser un número positivo.
    :return: El área del círculo.
    :raises ValueError: Si el radio es negativo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

# Ejemplo de uso
area_default = area_circulo_v5()
area_custom = area_circulo_v5(5)
print(f"Versión 5: El área del círculo con radio predeterminado es {area_default}")
print(f"Versión 5: El área del círculo con radio 5 es {area_custom}")
