'''
mi_lista = [] #acá la lista está vacía, estoy obligado a cargar la lista con un método
'''

mi_lista = [0] * 5 #cargo un elemento en base a algo que ya existe, a una posición en memoria que tiene un cero adentro

for i in range(len(mi_lista)):
    mi_lista[i] = int(input("Ingrese un número: ")) # con este for cargué secuencialmente la lista

for i in range(len(mi_lista)):
    print(mi_lista[i]) # con este for muestro la lista