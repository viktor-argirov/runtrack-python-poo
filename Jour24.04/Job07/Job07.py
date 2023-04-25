class Livre:
    def __init__(self,nom,auteur,nombre):
        self.__nom=nom
        self.__auteur=auteur
        self.__nombre=nombre
    
    def get_nom(self):
        return self.__nom
    
    def set_nom(self,nom):
        self.__nom=nom

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self,auteur):
        self.set__auteur=auteur

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, int) and nombre > 0:
            self.__nombre = nombre
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

livre=Livre("God of Thunder", "Thor",300)
print("Titre :",livre.get_nom())
print("Auteur :",livre.get_auteur())
print("Nombre de pages :", livre.get_nombre())

livre.set_nombre(200)
print("Nouveau nombre de pages :", livre.get_nombre())

livre.set_nombre(-5)
print("Error Pages:" , livre.get_nombre())