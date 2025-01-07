class Reservation:
    def __init__(self, id, client, date, place):
        self.id = id
        self.client = client
        self.date = date
        self.place = place
        self.statut = False

    def confirmer(self):
        self.statut = True
    

class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.reservations = []

    def effectuer_reservation(self, res):
        self.reservations.append(res)


class SystemeDeReservation:
    def __init__(self):
        self.reservations = []

    def ajouter_reservation(self, res):
        self.reservations.append(res)

    def annuler_reservation(self, res):
        self.reservations.remove(res)

    def afficher_reservations(self):
        for i in self.reservations:
            print(i.id, i.client, i.date, i.place)


client1 = Client("Arthur", "arthur@gmail.com")
client2 = Client("Luca", "luca@gmail.com")
client3 = Client("Matt", "matt@gmail.com")
client4 = Client("Patrick", "patrick@gmail.com")


reservation1 = Reservation(1, client1.nom, "2025-01-10", "Hotel 1")
reservation2 = Reservation(2, client2.nom, "2025-01-11", "Restaurant 1")
reservation3 = Reservation(3, client3.nom, "2025-01-12", "Restaurant 2")
reservation4 = Reservation(4, client4.nom, "2025-01-13", "Velo electrique")

systeme = SystemeDeReservation()

client1.effectuer_reservation(reservation1)
client2.effectuer_reservation(reservation2)
client3.effectuer_reservation(reservation3)
client4.effectuer_reservation(reservation4)

systeme.ajouter_reservation(reservation1)
systeme.ajouter_reservation(reservation2)
systeme.ajouter_reservation(reservation3)
systeme.ajouter_reservation(reservation4)

print("\nListe initiale des réservations :")
systeme.afficher_reservations()

print("\nConfirmation :")
reservation1.confirmer()
reservation3.confirmer()
systeme.afficher_reservations()

print("\nAnnulation :")
systeme.annuler_reservation(reservation2)
client2.reservations.remove(reservation2)
systeme.afficher_reservations()

print("\nRéservations par client :")
for client in [client1, client2, client3, client4]:
    print("Client: {0}, Réservations: {1}".format(client.nom, [res.id for res in client.reservations]))