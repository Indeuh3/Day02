from datetime import *
import time
class Message:
    def __init__(self, expediteur, destinataire, contenu, date):
        self.expediteur = expediteur
        self.dest = destinataire
        self.contenu = contenu
        self.date = date

    def afficher_message(self):
        print("De: {0} | À: {1} | Date: {2} \nContenu: {3}".format(self.expediteur, self.dest, self.date, self.contenu))

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.mess_envoyes = []
        self.mess_recus = []

    def envoyer_message(self, contenu, dest):
        message = Message(self.nom, dest.nom, contenu, datetime.today().replace(microsecond=0))
        self.mess_envoyes.append(message)
        dest.mess_recus.append(message)
        print("Le message à bien été envoyé")

    def lire_boite(self):
        print("\n Boite de reception de {0}".format(self.nom))
        for i in self.mess_recus:
            i.afficher_message()


User1 = Utilisateur("Arthur")
User2 = Utilisateur("Luca")
User3 = Utilisateur("Matt")

User2.envoyer_message("J'aime bien les cookies", User3)
time.sleep(1.4)
User3.envoyer_message("Mec, luca aime les cookies", User1)
time.sleep(1.4)
User1.envoyer_message("Mais non, c'est pas vrai tu mens", User3)
time.sleep(1.4)
User3.envoyer_message("Si si jte jure", User1)

User1.lire_boite()
User2.lire_boite()
User3.lire_boite()