def presentar_alumno(nombre: str, edad: int, altura: float) -> int:
    """mostrar los datos de un alumno

    Args:
        nombre (str): nombre del alumno
        edad (int): edad del alumno
        altura (float): altura del alumno

    Returns:
        int: (1:si esta todo bien | 0:si hubo error)
    """

    print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura}")
    return 1

retorno = presentar_alumno("Juan", 22, 1.75)

