class Article:
    def __init__(self, nom, prix, quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock

    def retirer_stock(self, nb):
        if self.quantite_stock - nb >= 0:
            self.quantite_stock -= nb


class Commande:
    def __init__(self, client):
        self.client = client
        self.articles_commandes = []

    def creer_commande(self, liste_article_quantite):
        for i in liste_article_quantite:
            self.articles_commandes.append([i[0], i[1]])


    def valider_commande(self):
        for i in self.articles_commandes:
            i[0].retirer_stock(i[1])

    def calculer_total(self):
        montant = 0
        for i in self.articles_commandes:
            if i[1] <= i[0].quantite_stock:
                montant += i[1]*i[0].prix
            else:
                return "Erreur, le stock de {0} n'est pas suffisant".format(i[0].nom)
        self.valider_commande()
        return "Le montant total est de {0} euros".format(montant)
    
            

art1 = Article("Manette", 60, 4)
art2 = Article("Ordinateur", 149, 2)
art3 = Article("Ecrans", 79, 6)

print("\nPatrick creer une commande pour 3 manettes et 1 ordinateur")
com1 = Commande("Patrick")
com1.creer_commande([[art1, 3], [art2, 1]])
print(com1.calculer_total())

print("\nLa commande est validée")
print(art1.quantite_stock)
print("\nMatt creer une commande pour 1 manette et 1 ecran")
com2 = Commande("Matt")
com2.creer_commande([[art3, 1], [art1, 2]])
print(com2.calculer_total())
