def cuenta_regresiva(iteraciones) -> int:
    if iteraciones != -1:
        print(iteraciones)
        cuenta_regresiva(iteraciones - 1)
    return iteraciones

cuenta_regresiva(10)


for i in range(10, -1, -1):
    print(i)