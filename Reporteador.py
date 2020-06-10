# Reporte Unidades venididas, venta$,  por articul
LisdeProd = [1, 2, 3, 4]
for Prod in LisdeProd:
    Prodsum = 0
    Prodvent = 0
    with open("Cons_ventas.txt") as file:
        for line in file:
            try:
                s = line.split(",")
                comparable = int(s[1])
            except:
                comparable = 0
            finally:
                if comparable == Prod:
                    Prodsum += int(s[5])
                    Prodvent += int(s[6])
                    Prodnom = s[2]
        print(f"El total de {Prodnom} es: {Prodsum} por un total de ${Prodvent}")
