class Plat:
    def __init__(self, nom, prix, temps_preparation):
        self.nom = nom
        self.prix = prix
        self.temps_preparation = temps_preparation

    def afficher_details(self):
        print("Plat: {0}, prix: {1}, Temps: {2} minutes".format(self.nom, self.prix, self.temps_preparation))

class Serveur:
    def __init__(self, nom):
        self.nom = nom
        self.commandes_prises = []

    def prendre_commande(self, plat, client):
        self.commandes_prises.append([plat, client])

class Restaurant:
    def __init__(self):
        self.plats_disponibles = []
        self.serveurs = []

    def ajouter_plat(self, plat):
        self.plats_disponibles.append(plat)

    def ajouter_serveur(self, serveur):
        self.serveurs.append(serveur)

    def afficher_menu(self):
        for i in self.plats_disponibles:
            i.afficher_details()

    def gerer_commandes(self, serveur, plats, client):
        for i in plats:
            serveur.prendre_commande(i, client)

restaurant = Restaurant()

Client1 = "Pepos"
Client2 = "Peposou"

plat1 = Plat("Pizza", 10, 20)
plat2 = Plat("Poisson", 20, 20)
plat3 = Plat("Pates", 14, 30)
plat4 = Plat("Viande", 10, 25)

serveur1 = Serveur("Patrick")
serveur2 = Serveur("Patrickos")

restaurant.ajouter_plat(plat1)
restaurant.ajouter_plat(plat2)
restaurant.ajouter_plat(plat3)
restaurant.ajouter_plat(plat4)

restaurant.ajouter_serveur(serveur1)
restaurant.ajouter_serveur(serveur2)

restaurant.afficher_menu()

restaurant.gerer_commandes(serveur1, [plat1, plat2], Client2)
restaurant.gerer_commandes(serveur2, [plat3, plat4], Client1)

print("\nCommandes par serveurs:")
for i in restaurant.serveurs:
    print("{0} a pris la commande {1} pour {2}".format(i.nom, [j[0].nom for j in i.commandes_prises], i.commandes_prises[1][1]))
