from Base import Productos

# variables que se van a usar
Total = 0
Venta_tot = []
Articulo = str(input("Que articulo desea registrar: ").upper())

# loop para introducir todos los articulos que se van a vender
while Articulo != "PAGAR":
    try:
        PUnitario = Productos[Articulo][3]
        Cantidad = int(input("Cuantos articulos: "))
        Venta = Productos[Articulo]
        Sub_total = PUnitario * Cantidad
        Venta.append(Sub_total)
        Total += Sub_total
        Venta_tot.append(Venta)
    except:
        print("Este articulo no existe, intenta con otro")
    finally:
        Articulo = str(input("Siguiente articulo o pagar: ").upper())

# finaliza la lista añade el total de la venta e imprime
Cuenta = ["", "Total", "", "", Total]
Venta_tot.append(Cuenta)
Titulos = ["ID", "Articulo", "Unidad", "P.Unit", "Total"]
print(Titulos)
for item in Venta_tot:
    print(item)
