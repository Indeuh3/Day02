class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def afficher_produit(self):
        return self.nom, self.prix, self.quantite
    
class Magasin:
    def __init__(self):
        self.liste = []

    def ajouter_produit(self,produit):
        self.liste.append(produit)

    def rechercher_produit(self, produit):
        for i in self.liste:
            if i == produit:
                return i.afficher_produit()
            
    def afficher_inventaire(self):
        for i in self.liste:
            print(i.nom)
            
    def vendre_produit(self, produit):
        if produit.quantite > 0:
            produit.quantite -= 1
        else:
            print("Rupture de stock")

Pomme = Produit("Pomme",4,8)
Banane = Produit("Banane",678,12)
Poire = Produit("Poire",1,3)
Prune = Produit("Prune",4,0)

magasin = Magasin()

magasin.ajouter_produit(Pomme)
magasin.ajouter_produit(Banane)
magasin.ajouter_produit(Poire)
magasin.ajouter_produit(Prune)

magasin.afficher_inventaire()
print(magasin.rechercher_produit(Pomme))
magasin.vendre_produit(Banane)
magasin.vendre_produit(Prune)

print(Banane.afficher_produit())
print(Prune.afficher_produit())