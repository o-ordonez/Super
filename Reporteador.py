# Abre archivo y añade las ventas realizadas
Prod = "CACahuate".upper()
Prodsum = 0
with open("Cons_ventas.txt") as file:
    for line in file:
        s = line.split(",")
        comparable = str(s[1]).upper()
        print(comparable)
        if comparable == Prod:
            Prodsum += int(s[4])
        else:
            print("no es igual")
            Prodsum += 0
    print(Prodsum)
