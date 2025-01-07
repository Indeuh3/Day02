class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def parler(self):
        return "Je suis un animal."
    
class Chien(Animal):
    def parler(self):
        return "Wouf"
    
class Chat(Animal):
    def parler(self):
        return "Miaou"
    
class Zoo:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self,animal):
        self.animaux.append(animal)

    def faire_parler_tout_le_monde(self):
        for i in self.animaux:
            print(i.parler())

zoo1 = Zoo()
zoo1.ajouter_animal(Animal("Hitler","Cheval"))
zoo1.ajouter_animal(Chat("Marc Dutroux","Chat"))
zoo1.ajouter_animal(Chien("Jeffrey Dahmer","Chien"))

zoo1.faire_parler_tout_le_monde()
