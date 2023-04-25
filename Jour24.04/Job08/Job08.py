class Livre:
    def __init__(self,nom,auteur,disponible=True):
        self.__nom=nom
        self.__auteur=auteur
        self.__disponible=disponible
    
    def get_nom(self):
        return self.__nom
    
    def get_auteur(self):
        return self.__auteur

    def get_disponible(self):
        return self.__disponible
       
    def emprunter(self):
        if self.disponible():
            self.__disponible= False
            print("Le Livre " , self.__nom, "a été emprunté")
        else:
            print("Desolé, le livre", self.__nom, "n'est pas disponible")

    def rendre(self):
        if not self.disponible(): 
            self.__disponible = True 
            print("Le livre", self.__nom, "a été rendu.")
        else:
            print("Erreur : le livre", self.__nom, "n'a pas été emprunté auparavant.")
    
livre=Livre("God of Thunder", "Thor",)
print("Titre :",livre.get_nom())
print("Auteur :",livre.get_auteur())
print("Status :",livre.get_disponible())