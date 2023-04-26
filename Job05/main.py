class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def Veillir(self):
        self.age += 1

    def Nommer(self, nom):
        self.nom = nom
        print(f"L'animal s'appelle : {self.nom}")


animal = Animal()
print("L'age initial de l'animal est :", animal.age)
animal.Veillir()
print("L'age après viellissement est :", animal.age)
animal.Nommer("Luna")