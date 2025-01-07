class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee 
        self.kilometrage = kilometrage

    def afficher_details(self):
        return self.marque, self.modele, self.annee, self.kilometrage
    
    def augmenter_kilometrage(self, x):
        if x >= 0:
            self.kilometrage += x
            return self.kilometrage
        return "Le nombre ne peut pas etre négatif"

Voiture1 = Voiture("Fiat", "500", 2012, 150000)
Voiture2 = Voiture("Fiat", "500 X", 2013, 160000)

Voiture1.augmenter_kilometrage(10000)
Voiture2.augmenter_kilometrage(25000)
print(Voiture1.afficher_details(), Voiture2.afficher_details())


