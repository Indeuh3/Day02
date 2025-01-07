
from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    def calculer_salaire(self):
        return self.salaire_base

class EmployeHoraire(Employe):
    def calculer_salaire(self, nbr_heure):
        return self.salaire_base * nbr_heure

class Entreprise:
    def __init__(self, liste_employes):
        self.liste_employes = liste_employes

    def masse_salariale(self, heure):
        msalaire = 0
        for i in  self.liste_employes:
            if isinstance(i, EmployeMensuel):
                msalaire += i.calculer_salaire()
            if isinstance(i, EmployeHoraire):
                msalaire += i.calculer_salaire(heure)
        return msalaire


employe_M1 = EmployeMensuel("Luca", 5000)
employe_M2 = EmployeMensuel("Patrick", 7000)
employe_H = EmployeHoraire("Arthur", 200)

entreprise = Entreprise([employe_M1, employe_M2, employe_H])

print(employe_M1.calculer_salaire(),employe_M2.calculer_salaire(), employe_H.calculer_salaire(50))

print(entreprise.masse_salariale(50))