class Operation :
    def __init__(self,nombre1=0,nombre2=0):
        self.nombre1=nombre1
        self.nombre2=nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(result)

Operation=Operation(12,3)
Operation.addition()