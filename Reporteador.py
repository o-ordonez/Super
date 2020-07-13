# Reporte Unidades venididas, venta$,  por articul
LisdeProd = [1, 2, 3, 4]
for Prod in LisdeProd:
    Sumcant = 0
    Sumdinero = 0
    with open("Cons_ventas.txt") as file:
        for line in file:
            try:
                s = line.split(",")
                comparable = int(s[1])
            except:
                comparable = 0

            finally:
                if comparable == Prod:
                    Sumcant += int(s[5])
                    Sumdinero += int(s[6])
                    Prodnom = s[2]
    Inventario = 0
    with open("Cons_entradas.txt") as file:
        for line in file:
            try:
                s = line.split(",")
                comparable = int(s[1])
            except:
                comparable = 0
            finally:
                if comparable == Prod:
                    Inventario += int(s[5])
    print(
        f"Ingresaron {Inventario} pzas de {Prodnom} y se vendieron {Sumcant} pzas por un total de ${Sumdinero} hay un I.final de {Inventario-Sumcant} pzas "
    )
