import random

class Equipe:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def marquer_point(self, nb):
        self.score += nb
        return self.score

class Match:
    def __init__(self, equipe1, equipe2, score_e1, score_e2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.score_e1 = score_e1
        self.score_e2 = score_e2

    def jouer(self):
        self.score_e1 = self.equipe1.marquer_point(random.randint(1,5))
        self.score_e2 = self.equipe2.marquer_point(random.randint(1,5))

    def afficher_res(self):
        print("{0} points pour {1}  |  {2} points pour {3}".format(self.score_e1, self.equipe1.nom, self.score_e2, self.equipe2.nom))
        print("Les Vainqueurs sont {0}!\n".format(self.equipe1.nom if self.score_e1 > self.score_e2 else self.equipe2.nom))
        return self.equipe2 if self.score_e1 > self.score_e2 else self.equipe1      # Je renvoie l'équipe perdante pour la supprimer de la liste gagnants dans la methode de la classe Tournoi

class Tournoi:
    def __init__(self, equipes):
        self.equipes = equipes
    
    def demarrer(self):
        gagnants = [i for i in self.equipes]                # On met toutes les equipes dans la liste des gagnants, et chaque equipe perdante est supprimée de cette liste
        Matchs = []
        while len(gagnants) > 1:

            gagnants[0].score = 0                   # Mise des scores à 0
            gagnants[1].score = 0

            nouveau_match = Match(gagnants[0], gagnants[1], 0, 0)       # Création d'un match
            while nouveau_match.score_e1 == nouveau_match.score_e2: 
                nouveau_match.jouer()
            Matchs.append(nouveau_match)                                # On ajoute ce match dans une liste

            print("Le match {0} s'est terminé".format(len(Matchs)))     # On accede au numero du match avec la longueur de la liste contenant les matchs
            gagnants.remove(nouveau_match.afficher_res())               # On supprime l'équipe perdante de la liste des gagnants
            
        print("Les gagnants du tournoi sont {0}!".format(gagnants[0].nom))

    
    
A = Equipe("Les Patrick", 0)
B = Equipe("Les Pepos", 0)
C = Equipe("Les Autres", 0)
D = Equipe("Ces gars là", 0)

Tour = Tournoi([A,B,C,D])
Tour.demarrer()