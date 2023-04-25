class Student:
    def __init__(self,nom,prenom,numero,credit):
        self.__nom=nom
        self.__prenom=prenom
        self.__numero=numero
        self.__credit=credit
        self.__level=self.__student_eval()

    def add_credits(self,credits):
        if credits>0:
            self.__credit+=credits
        self.__level=self.__student_eval()
    
    def __student_eval(self):
        if self.__credit >=90:
            return "Excellent"
        elif self.__credit >=80:
            return "Tres bien"
        elif self.__credit >=70:
            return "Bien"
        elif self.__credit >=60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def display_credit(self):
        print("Le nombre de credits de",self.__prenom,"avec Identifiant",self.__numero,"est",self.__credit)

    def get_student_info(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__numero}")
        print(f"Niveau : {self.__level}")
    
student=Student("Doe","Jean",145,100)
student.display_credit()
student.get_student_info()