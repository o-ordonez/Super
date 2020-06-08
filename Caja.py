from Base import Productos

Articulo = input("Que articulo desea registrar: ")
while Articulo != "PAGAR":
    try:
        PUnitario = Productos[Articulo][3]
        Cantidad = 10
        Venta = Productos[Articulo]
        Venta.append(PUnitario * Cantidad)
        print(Venta)
        Articulo = "PAGAR"
    except:
        print("Este articulo no existe, intenta con otro")
    finally:
        Articulo = input("Siguiente articulo o pagar: ")
