# Encapsulation
class Student:
    def __init__(self):
        self.__codesis = 2022   #private
        self.codesis = 2020     #public

    def getcodesis(self):
        return self.__codesis

    def __paymentaccount(self):
        print("BNB-35336RRRRR")

person = Student()
print(person.__codesis)
person._Student__paymentaccount()
