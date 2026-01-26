"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    if prices==[]:
        raise ValueError("La lista está vacía")
    else:
        min_price= min(prices)
        max_price= max(prices)
        return (min_price, max_price)
    raise NotImplementedError("Implementa min_max_prices(prices)")
