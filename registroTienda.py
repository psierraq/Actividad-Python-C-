cantidad = 0
productosRegistrados = 0
productosConDescuento = 0


precio= 0.0
totalProducto= 0.0
descuento= 0.0
totalCompras = 0.0
totalPagado = 0.0




producto=int(print("Ingrese el nombre del producto (FIN para terminar): "))


while (producto != "FIN"):


    cantidad=int(input("Ingrese la cantidad: "))


    precio=float(input("Ingrese el precio unitario: "))


    productosRegistrados+=1


    totalProducto = cantidad * precio
    descuento = 0


    if (totalProducto >= 100000):
        descuento = totalProducto * 0.10
        productosConDescuento+=1
   
    elif(totalProducto >= 50000):
        descuento = totalProducto * 0.05
        productosConDescuento+=1
   


    valorFinal = totalProducto - descuento


    print("\nProducto: ")
    print("Valor original: $")
    print("Descuento: $")
    print( "Valor a pagar: $")


    totalCompras += totalProducto;
    totalPagado += valorFinal;
    producto=int(print("\nIngrese el nombre del producto (FIN para terminar): "))
   




print("\n--- RESUMEN DE LA COMPRA ---")
print("Productos registrados: ")
print("Productos con descuento: ")
print("Valor original de las compras: $")
print("Valor final a pagar: $")



