from datetime import datetime
#for date and time

class Record:
    def __init__(self, forename, surname, age, gender, CS_student):
        self.__created = datetime.now()
        self.__forename = str(forename)
        self.__surname = str(surname)
        try:
            self.__age = int(age)
        except:
            self.__age = 0
        self.__gender = str(gender)
        self.__CS_student = CS_student

    def getForename(self):
        return self.__forename

    def getSurname(self):
        return self.__surname

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def getCS_student(self):
        return self.__CS_student


    def setForename(self, name):
        self.__forename = str(name)

    def setSurname(self, name):
        self.__surname = str(name)

    def setAge(self, age):
        try:
            self.__age = int(age)
        except:
            print("invalid age")

    def setGender(self, gender):
        if gender == "m" or gender == "f":
            self.__gender = gender
        else:
            print("invalid gender: m / f")

    def setCS_student(self,bool):
        if type(bool) == type(True):
            self.__CS_student = bool
        else:
            print("invalid: True / False")

    def getCreated(self):
        return self.__created

    def dayBorn(self):
        dob = input("enter your date of birth: xx.xx.xxxx ")
        dob = dob.split(".").reverse # here______________________
        print(dob)



myPupil = Record("Tom", "Rietjens", 17, "m", True)
print(myPupil.getCreated())
myPupil.dayBorn()
