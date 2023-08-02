import csv
from helper import *
from presentatie import *

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}   

keys = inkomsten.keys()
values = inkomsten.values()

inkomsten_totaal = som(inkomsten)
print()
uitvoer = presenteer(inkomsten, inkomsten_totaal)
print()

with open ('boekhouding.csv', 'w', newline= '') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key, value])