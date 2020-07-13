# Reporte Unidades venididas, venta$,  por articul
LisdeProd = [1, 2, 3, 4]
# Fecha = str(input("Introduce fecha('aaaa-mm-dd') de reporte: "))
for Prod in LisdeProd:
    Sumcant = 0
    Sumdinero = 0
    with open("Cons_ventas.txt") as file:
        for line in file:
            try:
                s = line.split(",")
                comparable = int(s[1])
                # fechcomp = str(s[7])
            except:
                comparable = 0
            finally:
                if (
                    comparable == Prod
                ):  # preguntar como puede ponerlo como intervalo para el reporte
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
    Defectos = 0
    with open("Cons_defectos.txt") as file:
        for line in file:
            try:
                s = line.split(",")
                comparable = int(s[1])
            except:
                comparable = 0
            finally:
                if comparable == Prod:
                    Defectos += int(s[5])
    print(
        f"Articulo: {Prodnom} -Entradas= {Inventario} -Ventas= {Sumcant} pzas  ${Sumdinero} -Def o dev= {Defectos} pzas -I.final= {Inventario-Sumcant-Defectos} pzas "
    )
