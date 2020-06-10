from Base import Productos
import datetime

# variables que se van a usar
Titulos = ["ID", "Articulo", "Unidad", "P.Unit", "Cantidad", "Total"]
Total = 0
Venta_tot = []
Articulo = str(input("Que articulo desea registrar: ").upper())
Fecha = str(datetime.date.today())
# loop para introducir todos los articulos que se van a vender
while Articulo != "PAGAR":
    try:
        PUnitario = Productos[Articulo][4]
        Cantidad = int(input("Cuantos articulos: "))
        Venta = Productos[Articulo]
        Sub_total = PUnitario * Cantidad
        Venta.extend((Cantidad, Sub_total, Fecha))
        Total += Sub_total
        Venta_tot.append(Venta)

    except:
        print("Este articulo no existe, intenta con otro")
    finally:
        Articulo = str(input("Siguiente articulo o pagar: ").upper())

# finaliza la lista añade el total de la venta e imprime
Cuenta = ["", 0, "Total", "", "", Total]
Venta_tot.append(Cuenta)
print(Titulos)
bd = open("Cons_ventas.txt", "a")
for item in Venta_tot:

    bd.write("\n")
    item = str(item)
    bd.write(item)
    print(item)
bd.close()
