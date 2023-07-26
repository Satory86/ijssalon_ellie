mijn_lijst = [220, 430, 125, 160, 205, 90, 430]
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = f'''Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.'''
    return uitvoer
btw_procentage = 0.09
result = (inkomsten_totaal(mijn_lijst, btw_procentage))
print(result)