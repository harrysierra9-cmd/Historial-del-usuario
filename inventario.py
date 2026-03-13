print("registro de producto")
cantidad = 0
nombre = input("ingrese el nombre del producto")
while True:
    try:
        precio = float(input("ingrese el precio del producto: "))
        break
    except:
        print("valor invalido. ingrese un numero para el precio.")

while True:
    try:
        cantidad = int(input("ingrese la cantidad del producto: "))
        break
    except:
        print("valor invalido. ingrese un numero entero para la cantidad.")

        costototal = precio * cantidad

        print("resultado")
        print("nombre del producto")
        print("precio")
        print("cantidad")
        print("costo total")
