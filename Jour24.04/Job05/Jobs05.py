class Animal:
    def __init__(self,nom):
        self.nom=nom
        self.age = 0
        
    def vieillir(self):
        self.age += 1
    
    def nommer(self):
        return "l'animal se nomme {}".format(self.nom)
    
animal = Animal("Luna")
print("l'age de l'animal" , animal.age , "ans") 
animal.vieillir()
print("l'age de l'animal" , animal.age , "ans") 
print(animal.nommer())