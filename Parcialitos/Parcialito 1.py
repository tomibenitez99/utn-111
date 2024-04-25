'''
PARCIALITO 1

Consigna:
Desarrollar una función que reciba como parámetros el precio de un producto, la cantidad y el porcentaje de descuento que se aplicara si la cantidad de productos supera las 10 unidades. La función retornara el precio de la compra con descuento (si corresponde).
'''

def precio_compra(precio: float, cantidad: int, porcentaje_descuento: int) -> float:
    if cantidad > 10:
        precio_total = precio * cantidad
        descuento = precio_total * (porcentaje_descuento / 100)
        precio_con_descuento = precio_total - descuento
        return precio_con_descuento
    else:
        return precio * cantidad
    
precio = float(input("Ingrese un precio: "))
cantidad = int(input("Ingrese la cantidad: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))

precio_final = precio_compra(precio, cantidad, porcentaje_descuento)
print("Precio final con descuento: ", precio_final)