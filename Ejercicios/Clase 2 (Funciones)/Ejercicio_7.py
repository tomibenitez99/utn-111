def numero_maximo(primer_numero: int, segundo_numero: int, tercer_numero: int):
    if primer_numero > segundo_numero and primer_numero > tercer_numero:
        mensaje = f"El número {primer_numero} es el más grande"
    elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
        mensaje = f"El número {segundo_numero} es el más grande"
    else:
        mensaje = f"El número {tercer_numero} es el más grande"
    
    return mensaje

numeros_ingresados = numero_maximo(1, 5, 90)
print(numeros_ingresados)