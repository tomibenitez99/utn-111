def get_float() -> float: #inicializo la función get_float() que me devuelve un float
    numero = input("Ingrese un número (puede ser con coma): ") #pido que ingrese un número
    numero = float(numero) #el numero se convierte a tipo float

    return numero

numero_solicitado = get_float()
print(f"El numero ingresado es: {numero_solicitado}")
