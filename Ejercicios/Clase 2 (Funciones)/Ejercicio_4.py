def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input("Error. {mensaje}")

    return numero


def get_float(mensaje: str, minimo: float, maximo: float) -> float:
    numero_flotante = input(mensaje)
    numero_flotante = float(numero_flotante)
    while numero_flotante < minimo or numero_flotante > maximo:
        numero_flotante = input("Error. {mensaje}")

        return numero_flotante
    

def get_str(mensaje: str) -> str:
    texto = input(mensaje)

    return texto