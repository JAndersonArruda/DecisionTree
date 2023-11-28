from date import Subjects as S

class Gerency():
    def __init__(self, classes, test, subjects):
        self.classes = classes
        self.test = test
        self.subjects = subjects
    
    def probalityCalculate(self, date):
        self.date = date
        self.dicDate = S.dateDict()
        pass
    
    def desissionVerification(self):
        if (self.classes):
            if (self.test):
                print("Você deve ir para a aula hoje, para não perder o teste")
            elif (self.probalityCalculate(self.subjects) >= 4.1):
                print(f"Você deve ir a aula hoje, há a probabilidade de importancia de {self.probalityCalculate(self.subjects)}")
            else:
                print(f"Você não deve ir aula hoje, há a probabilidade de importancia de {self.probalityCalculate(self.subjects)}")
        else:
            print("Você não deve ir!")
                