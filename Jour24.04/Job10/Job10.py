class Voiture :
    def __init__(self,marque,modele,annee,kilometrage):
        self.__marque=marque
        self.__modele=modele
        self.__annee=annee
        self.__kilometrage=kilometrage
        self.__en_marche=False
        self._reservoir = 50
    
    def get_marque(self):
        return self._marque
        
    def set_marque(self, marque):
        self._marque = marque
        
    def get_modele(self):
        return self._modele
        
    def set_modele(self, modele):
        self._modele = modele
        
    def get_annee(self):
        return self._annee
        
    def set_annee(self, annee):
        self._annee = annee
        
    def get_kilometrage(self):
        return self._kilometrage
        
    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage
        
    def get_en_marche(self):
        return self._en_marche
    
    def demarrer(self):
        if self.verifier_plein():
            self.__en_marche=True
            print("La voiture demarre.")
        else:
            print("Le réservoir est presque vide, il faut faire le plein avant de démarrer.")

    def arreter(self):
                self._en_marche = False
                print("La voiture s'arrête.")
        
    def verifier_plein(self):
                return self.__reservoir > 5
            
voiture=Voiture("Bugatti","Chiron",2022,400)