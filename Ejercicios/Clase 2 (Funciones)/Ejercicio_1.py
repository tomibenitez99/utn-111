def get_int() -> int: #inicializo la función get_int() que me devuelve un int
    numero = input("Ingrese un número: ") #Pido que ingrese un número
    numero = int(numero) #El número ingresado tiene que ser de tipo int

    return numero #me devuelve el numero ingresado de tipo número

numero_solicitado = get_int() # llamo a la función get_int() y la asigno a la variable numero_solicitado

print(f"El número ingresado es: {numero_solicitado}") #muestro en consola la variable que contiene la función dentro