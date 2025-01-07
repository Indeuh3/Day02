import time


class Personnage:
    def __init__(self, nom, pv, force):
        self.nom = nom
        self.pv = pv
        self.force = force

    def attaquer(self, cible):
        cible.pv -= self.force
        print("{0} attaque {1}!".format(self.nom,cible.nom))

class Guerrier(Personnage):
    def __init__(self, nom, pv, force):
        super().__init__(nom, pv, force)
        self.force *= 1.10

class Mage(Personnage):
    def attaquer(self, cible):
        cible.pv -= (self.force + 5)
        print("{0} attaque {1}!".format(self.nom,cible.nom))


class Combat:
    def __init__(self, perso1, perso2):
        self.perso1 = perso1
        self.perso2 = perso2

    def afficher_pv(self):
        print("{0} : {1} pv    |    {2} : {3} pv".format(self.perso1.nom, round(self.perso1.pv), self.perso2.nom, round(self.perso2.pv)))

    def lancer_combat(self):
        n = 1
        while self.perso1.pv > 0 and self.perso2.pv > 0:
            print("ROUND ", n)
            self.afficher_pv()
            time.sleep(0.5)
            self.perso1.attaquer(self.perso2)
            if self.perso2.pv <= 0:
                return "{0} est le gagnant!".format(self.perso1.nom)
            time.sleep(0.5)
            self.perso2.attaquer(self.perso1)
            if self.perso1.pv <= 0:
                return "{0} est le gagnant!".format(self.perso2.nom)
            n += 1
            time.sleep(0.5)


A = Guerrier("Arthur", 160, 50)
B = Mage("Pepito", 200, 48)
C = Personnage("Villageois", 140, 10)

print(A.force, B.force, C.force)
huh = Combat(A,B)
print(huh.lancer_combat())
    