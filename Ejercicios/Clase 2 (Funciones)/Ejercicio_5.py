import math
math.pi

def area_circulo():
    radio = input("Ingrese el radio del círculo en cm: ")
    radio = float(radio)

    area = math.pi*(radio**2)

    return area

area_del_circulo = area_circulo()
print(f"El área del círculo es: {area_del_circulo}cm2")