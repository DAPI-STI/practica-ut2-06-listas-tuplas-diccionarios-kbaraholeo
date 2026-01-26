"""
EX04 (Tuplas)
Trabajar con una lista de tuplas (nombre, nota) y devolver una tupla.
"""

def best_student(records: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve la tupla del alumno con mayor nota.

    - Si records está vacío, lanza ValueError.
    - Si hay empate, devuelve el primero que aparezca con esa nota.

    Ejemplo:
    [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)] -> ("Luis", 9.0)
    """
    if records == []: #si la lista recods está vacía, lanzamos un raise VlueError
        raise ValueError("La lista de registros está vacía")
    mejor_nota= records[0] #Mejor nota en el primer elemento de la lista
    for alumno in records:
        if alumno[1]> mejor_nota[1]: #Compara la nota del alumno con la mejor nota
            mejor_nota= alumno #Si la nota del alumno es mayor, actualiza la mejor nota
        if alumno[1]== mejor_nota[1]:
            continue #Si hay empate, se queda con el primero que apareció
    return mejor_nota
    raise NotImplementedError("Implementa best_student(records)")

