"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.

    Ejemplo:
    - [3, 1, 3, 2, 1] -> [3, 1, 2]

    Requisito:
    - No modifiques la lista original.
    """
    l=[]
    for v in values:
        if v not in l: #Si el valor no está en la lista, lo añade
            l.append(v)
    return l

    #raise NotImplementedError("Implementa unique_preserve_order(values)")
