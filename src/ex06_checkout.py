"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float]= {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    # cart es la lista de tuplas (producto, unidades)
    costes: dict[str, float] = {} # Inicializa el diccionario de costes por producto
    suma_total = 0.0
    for producto, unidades in cart:
        if unidades < 0:
            raise ValueError(f"Unidades negativas para el producto {producto}") #Si las unidades son negativas, lanza ValueError
        if producto not in PRICES:
            raise ValueError(f"Producto {producto} no existe en PRICES") #Si el producto no existe en PRICES, lanza ValueError
        if producto in costes:
            #print(PRICES[producto], " ", unidades)
            costes[producto] += PRICES[producto] * unidades #Acumula el coste si el producto ya está en el diccionario
            costes[producto] = round(costes[producto], 2)
        else:
            costes[producto] = PRICES[producto] * unidades #Añade el coste si el producto no está en el diccionario
            costes[producto] = round(costes[producto], 2) #Redondea el coste a 2 decimales
        suma_total = sum(costes.values()) #Calcula el total general redondeado a 1 decimal
    return costes, suma_total