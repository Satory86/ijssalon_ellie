def decoreer(tekst="") :
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def onderstreep(tekst="") :
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(value):
    totaal = 0
    for value in value.values():
        totaal += value
    return totaal
