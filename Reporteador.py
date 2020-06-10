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
        f"El total de {Prodnom} es: {Sumcant} por un total de ${Sumdinero} e ingresaron {Inventario}, I.final {Inventario-Sumcant} "
    )
