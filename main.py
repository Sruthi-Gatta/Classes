from datetime import date


class Pet:
    __name = ""
    __species = ""
    __breed = ""
    __color = ""
    __gender: bool
    __owner = ""
    __address = ""
    birthdate: date

    # Object constructor
    def __init__(self, name, species, breed, color, gender, owner, address, birthdate):
        self.__name = name
        self.__species = species
        self.__breed = breed
        self.__color = color
        self.__gender = gender
        self.__owner = owner
        self.__address = address
        self.birthdate = birthdate

    # Methods
    def setName(self, name):
        self.__name = name

    def setSpecies(self, species):
        self.__species = species

    def setBreed(self, breed):
        self.__breed = breed

    def setColor(self, color):
        self.__color = color

    def setGender(self, gender):
        self.__gender = gender

    def setOwner(self, owner):
        self.__owner = owner

    def setAddress(self, address):
        self.__address = address

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getName(self):
        return self.__name

    def getSpecies(self):
        return self.__species

    def getBreed(self):
        return self.__breed

    def getColor(self):
        return self.__color

    def getGender(self):
        if self.__gender:
            return "male"
        else:
            return "female"

    def getOwner(self):
        return self.__owner

    def getAddress(self):
        return self.__address

    def getBirthdate(self):
        return self.birthdate

    def getAge(self):
        days_in_year = 365.2425
        age = int((date.today() - self.birthdate).days / days_in_year)
        return age

    def __str__(self):
        return "{} is a {} and is {} years old and of color {} with {} gender".format(self.__name, self.__species, self.getAge(), self.__color, self.getGender())


class Dog(Pet):
    def __init__(self, name, breed, color, gender):
        self.__name = name
        self.__breed = breed
        self.__color = color
        self.__gender = gender
        self.species = "canis familaris"


class Puppy(Dog):
    dob: date

    def __init__(self, name, breed, color, gender, birthdate):
        super().__init__(name, breed, color, gender)
        self.dob = birthdate

    def getAge(self):
        days_in_year = 365.2425
        age = int((date.today() - self.dob).days / days_in_year)
        print("Age of puppy in Months ", age * 12)

    def play(self):
        return " (___()'`;\n      /,    /`\n      \\\\\"--\\\\"


name = input("What is your pet's name?\n")
birth_day = int(input("what is your pet's birth day "))
birth_month = int(input("what is your pet's birth month"))
birth_year = int(input("what is your pet's birth year"))
# Call object from class attributes
myPet = Pet(name, "Canis Familiaris", "PUG", "Brown", True, "sruthi", "CASA", date(birth_year, birth_month, birth_day))
print(myPet.__str__())
myPuppy = Puppy(name, "PUG", "Black", True, date(birth_year, birth_month, birth_day))
print("Puppy class")
print(myPuppy.play())
print(myPuppy.getAge())
