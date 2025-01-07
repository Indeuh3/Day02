class Livre:
    def __init__(self, titre, auteur, dispo):
        self.titre = titre
        self.auteur = auteur
        self.dispo = dispo

    def emprunter(self):
        if not self.dispo:
            print("Le livre n'est pas disponible")
        else:
            self.dispo = False
            print("Livre emprunté")

    def rendre(self):
        if self.dispo:
            print("vous n'avez pas emprunté ce livre, menteur >:(")
        else:
            self.dispo = True
            print("Livre rendu")

    
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livre_empruntes = []

    def emprunter_livre(self, livre):
        if livre.dispo:
            self.livre_empruntes.append(livre)
        livre.emprunter()
            

    def rendre_livre(self, livre):
        if livre in self.livre_empruntes:
            livre.rendre()
            self.livre_empruntes.remove(livre)

class Bibliotheque:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self, livre):
        self.liste_livres.append(livre)

    def afficher_livres(self):
        for i in self.liste_livres:
            print(i.titre,i.auteur,i.dispo)

    def gerer_emprunt(self,livre,utilisateur,action):
        if action == "emprunter":
            utilisateur.emprunter_livre(livre)
        elif action == "rendre":
            utilisateur.rendre_livre(livre)

        
livre1 = Livre("Python sans stress", "Moi", True)
livre2 = Livre("Les Secrets Cachés du Debugging", "Max loops", True)
livre3 = Livre("Python pour les nuls", "Honri Gaule", True)
livre4 = Livre("Les Misérables", "Victor Hugo", True)

utilisateur1 = Utilisateur("Arthur")
utilisateur2 = Utilisateur("Jean")
utilisateur3 = Utilisateur("UnGarsSansPrenom")

bibliotheque = Bibliotheque()

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)
bibliotheque.ajouter_livre(livre4)

print("\nListe initiale des livres :")
bibliotheque.afficher_livres()

print("\nArthur emprunte Python sans stress :")
bibliotheque.gerer_emprunt(livre1, utilisateur1, "emprunter")

print("\nJean essaie d'emprunter Python sans stress (déjà emprunté) :")
bibliotheque.gerer_emprunt(livre1, utilisateur2, "emprunter")

print("\nUnGarsSansPrenom emprunte Les Secrets Cachés du Debugging :")
bibliotheque.gerer_emprunt(livre2, utilisateur3, "emprunter")

print("\nListe des livres après les emprunts :")
bibliotheque.afficher_livres()

print("\nArthur rend Python sans stress :")
bibliotheque.gerer_emprunt(livre1, utilisateur1, "rendre")

print("\nArthur rend Python sans stress (déjà rendu) :")
bibliotheque.gerer_emprunt(livre1, utilisateur1, "rendre")

print("\nJean emprunte Python sans stress (maintenant disponible) :")
bibliotheque.gerer_emprunt(livre1, utilisateur2, "emprunter")

print("\nUnGarsSansPrenom rend Les Secrets Cachés du Debugging :")
bibliotheque.gerer_emprunt(livre2, utilisateur3, "rendre")
 
print("\nUnGarsSansPrenom emprunte Python pour les nuls :")
bibliotheque.gerer_emprunt(livre3, utilisateur3, "emprunter")

print("\nListe finale des livres :")
bibliotheque.afficher_livres()

print("\nLivres empruntés par Arthur :", [livre.titre for livre in utilisateur1.livre_empruntes])
print("Livres empruntés par Jean :", [livre.titre for livre in utilisateur2.livre_empruntes])
print("Livres empruntés par UnGarsSansPrenom :", [livre.titre for livre in utilisateur3.livre_empruntes])

