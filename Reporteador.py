# Abre archivo y añade las ventas realizadas
LisdeProd = ["PEPITA", "CACAHUATE"]
for Prod in LisdeProd:
    Prodsum = 0
    with open("Cons_ventas.txt") as file:
        print(Prod)
        for line in file:
            s = line.split(",")
            comparable = str(s[1]).upper()
            if comparable == Prod:
                Prodsum += int(s[4])
        print(f"El total de {Prod} es: {Prodsum}")
