class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    
    def get_longueur(self):
        return self.get_longueur
    
    def set_longueur(self,longueur):
        self.longueur=longueur

    def get_lageur(self):
        return self.get_lageur
    
    def set_largeur(self,largeur):
        self.largeur=largeur

rectangle=Rectangle(10,5)
print("Longueur : " , rectangle.longueur)
print("Largeur : " , rectangle.largeur)

rectangle.set_longueur(20)
rectangle.set_largeur(12)
print("NEWLongueur : " , rectangle.longueur)
print("NEWLargeur : " , rectangle.largeur)