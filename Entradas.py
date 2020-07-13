from Base import Productos
import datetime

# variables que se van a usar
Titulos = ["", "ID", "Articulo", "Unidad", "P.Venta", "Cantidad", "Costo", "C.Total"]
Total = 0
Lisent = []
Artent = str(input("Que articulo desea registrar: ").upper())
Fecha = str(datetime.date.today())
# loop para introducir todos los articulos que se van a vender
while Artent != "FINALIZAR":
    try:
        PCompra = int(input("Precio de compra: "))
        Cantidad = int(input("Cuantos articulos van a ingresar: "))
        Ctot = PCompra * Cantidad
        Ent = Productos[Artent]
        Ent.extend((Cantidad, PCompra, Ctot))
        Lisent.append(Ent)
    except:
        print("Este articulo no existe, intenta con otro")
    finally:
        Artent = str(input("Siguiente articulo o finalizar: ").upper())
# finaliza la lista añade el total de la venta e imprime
print(Titulos)
bd = open("Cons_entradas.txt", "a")
for item in Lisent:
    bd.write("\n")
    item = str(item)
    bd.write(item)
    print(item)
bd.close()
