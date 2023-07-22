def fooi_pp(bedrag, personen) :
    try:
        bedrag_pp = bedrag / personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per person is {bedrag_pp} euro"

b = int(input("Welke bedrag zit er in de fooienpot? ")) 
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? ")) 

print(fooi_pp(b, p))