class Livre:
    def __init__(self, titre, nbpage):
        self.titre = titre
        self.nbpage = nbpage
    
    def get_titre(self):
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre
    
    def get_nbpage(self):
        return self.nbpage
    
    def set_nbpage(self, nbpage):
        self.nbpage = nbpage

livre = Livre("La Guerre des mondes !", 320)
print(f"Le Titre du livre est : {livre.titre}")
print(f"Son nombre de page est : {livre.nbpage}")