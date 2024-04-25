vector = [1, 4, 6, 8, 2]

#print(vector[3]) 

for i in range(len(vector)): #range me devuelve un rango. len me dice cuántos elementos tengo en mi lista

    if vector[i] % 2 == 0: #me muestra los pares

        print(vector[i], end = " ") #vector[i] me muestra la lista en la posición de i, o sea el de la lista que yo tengo. end = " ": sirve para mostrarme la lista en horizontal separado cada índice por un espacio.