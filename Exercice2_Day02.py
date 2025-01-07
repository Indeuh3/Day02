from datetime import *

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee 
        self.kilometrage = kilometrage

    def calculer_age(self):
        return datetime.today().year - self.annee
    
    def est_vielle(self):
        return self.calculer_age() > 10

Voiture1 = Voiture("Fiat", "500", 2012, 150000)
Voiture2 = Voiture("Fiat", "500 X", 2020, 160000)

print(Voiture1.calculer_age(),Voiture1.est_vielle())
print(Voiture2.calculer_age(),Voiture2.est_vielle())

