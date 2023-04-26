class Livre:
    def __init__(self, titre, nbpage):
        self.titre = titre
        self.nbpage = nbpage
        self.disponible = True
    
    def get_titre(self):
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre
    
    def get_nbpage(self):
        return self.nbpage
    
    def set_nbpage(self, nbpage):
        self.nbpage = nbpage
    
    def verification(self):
        return self.disponible
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print("Livre emprunté!")
        else:
            print("Le livre est déjà emprunté.")
    
    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print("Livre rendu!")
        else:
            print("Le livre n'a pas été emprunté.")

livre = Livre("La Guerre des mondes !", 320)
print(f"Le Titre du livre est : {livre.titre}")
print(f"Son nombre de page est : {livre.nbpage}")
livre.emprunter() 
livre.rendre() 