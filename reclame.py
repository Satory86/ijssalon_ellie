from algemene_functies import mijn_functie_2

def aanbieding_1() :
    uitvoer = prijs * korting
    return uitvoer
smaak = "aarbei"
prijs = 4
korting = 0.1
totaal = prijs - aanbieding_1()
reklama_tekst = f"Vaandag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {totaal} euro."
print(reklama_tekst)

mijn_lijst = [220, 430, 125, 160, 205, 90, 430]
def inkomsten_totaal():
    uitvoer = sum(mijn_lijst)
    return uitvoer
inkomsten = inkomsten_totaal()
Btw = 0.09
bedrag = inkomsten * Btw
tekst = f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden."
print(tekst)

def laag_en_hoog():
    uitvoer = min_val, max_val
    return uitvoer
min_val = min(mijn_lijst)
max_val = max(mijn_lijst)
print("Minimum:", min_val)
print("Maximum:", max_val)

def gemiddelde():
    totaal_sum = sum(mijn_lijst)
    variable = len(mijn_lijst)
    gemiddelde = totaal_sum / variable
    return gemiddelde
bedrag = gemiddelde()
tekst = f"De gemiddelde inkomsten deze week zijn {bedrag} euro." 
print(tekst)

invoer = [10, 5, 3, 2, 4, 2, 9]
def meervouding(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
def laag_en_hoog(lijst):
    laagste = min(lijst)
    hoogste = max(lijst)
    return [laagste, hoogste]
uitvoer = meervouding(invoer)
print(uitvoer)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(uitvoer))