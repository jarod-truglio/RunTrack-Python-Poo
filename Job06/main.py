class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def get_longueur(self):
        return self.longueur
    
    def set_longueur(self, longueur):
        self.longueur = longueur
    
    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, largeur):
        self.largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur du Rectangle : ", rectangle.get_longueur())
print("Largeur du Rectangle : ", rectangle.get_largeur())