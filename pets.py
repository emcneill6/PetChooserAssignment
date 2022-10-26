# Pet class

class Pet:
    def __init__(self, petName, ownerName, petAge, animalType):
        self.petName = str(petName)
        self.ownerName = str(ownerName)
        self.petAge = int(petAge)
        self.animalType = str(animalType)

    def getAnimalType(self) -> str:
        return self.__animalType

    def getPetAge(self) -> int:
        return self.__petAge

    def getPetName(self) -> str:
        return self.__petName

    def getAnimalType(self) -> str:
        return self.__type

    def getOwnerName(self) -> str:
        return self.__owner


    def setPetName(self, name: str) -> None:
        try:
            self.__petName = name
        except ValueError as e:
            print("Invalid input.")

    def setPetAge(self, age: int) -> None:
        try:
            self.__petAge = age
        except ValueError as e:
            print("Invalid input.")

    def setAnimalType(self, animalType: str) -> None:
        try:
            self.__animalType = animalType
        except ValueError as e:
            print("Invalid input.")

    def setOwnerName(self, ownerName: str) -> None:
        try:
            self.__ownerName = ownerName
        except ValueError as e:
            print("Invalid input.")