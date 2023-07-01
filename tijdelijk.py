prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = 0.8 
aanbieding_prijs =(prijzen["aardbei"]) * aanbieding 
reclame_tekst = f"Vaandag is de aanbieding: aardbei-ijs, 1-liter - slechts € {aanbieding_prijs} "
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
list = reclame_tekst3.split()
for el in list:
   if len(el) >=5:
      print(el.upper())
   else:
      print(el.lower())